from tkinter import *
from tkinter import ttk
from conexion_DB.consultas_db import *

class VistaCarrera(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def nuevo_carrera():
            self.entry_nombre.config(state= "normal")
            self.entry_duracion.config(state= "normal")
        
        #Inserta datos a la DB
        def insertar_datos():
            
            query = 'INSERT INTO carrera VALUES (NULL, ?, ?)'
            parametros = (self.entry_nombre.get(), self.entry_duracion.get())

            conexion = Conectar_db()
            conexion.run_db(query, parametros)
            
            #Limpiar campos
            self.entry_nombre.delete(0, END)
            self.entry_duracion.delete(0, END)
        
            #Actualizar tabla
            listar_datos()
        
        #Eliminar datos
        def eliminar_datos():
            codigo = self.tabla.item(self.tabla.selection())['text']
            query = 'DELETE FROM carrera WHERE codigo_c = ?'
            conexion = Conectar_db()
            conexion.run_db(query, (codigo,))

            #Actualizar tabla
            listar_datos()
        
        #Actualizar datos
        def editar_datos(codigo_n, codigo_a, nombre_nuevo, nombre_antiguo, duracion_nuevo, duracion_antigua):
            query = 'UPDATE carrera SET codigo_c = ?, nombre_c = ?, duracion_c = ? WHERE codigo_c = ? AND nombre_c = ? AND duracion_c = ?'
            parametros = (codigo_n, nombre_nuevo, duracion_nuevo, codigo_a, nombre_antiguo, duracion_antigua)
            conexion = Conectar_db()
            conexion.run_db(query, parametros)

            #Destruye la ventana 
            self.ventana_editar.destroy()

            #Actualizar tabla
            listar_datos()

        #================ LABEL TITULO REGISTRAR ================#
        self.label_titulo_registrar = Label(self, text="REGISTRAR NUEVA CARRERA")
        self.label_titulo_registrar.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        #================ LABEL Y CAMPO DE NOMBRE ================#
        self.label_nombre = Label(self, text="Nombre")
        self.label_nombre.grid(row=1, column=0, pady=10, padx=10)
        self.entry_nombre = Entry(self, state='readonly')
        self.entry_nombre.grid(row=1, column=1, pady=10, padx=10)

        #================ LABEL Y CAMPO DURACION ================#
        self.label_duracion = Label(self, text="Duracion")
        self.label_duracion.grid(row=2, column=0, pady=10, padx=10)
        self.entry_duracion = Entry(self, state='readonly')
        self.entry_duracion.grid(row=2, column=1, pady=10, padx=10)

        #================ BOTONES REGISTRAR Y GUARDAR  ================#
        self.boton_registrar = Button(self, text="REGISTRAR", command=nuevo_carrera)
        self.boton_registrar.grid(row=3, column=0, pady=10, padx=10)

        self.boton_guardar = Button(self, text="GUARDAR", command=insertar_datos)
        self.boton_guardar.grid(row=3, column=1, pady=10, padx=10)

        #================ LABEL TITULO LISTA ================#
        self.label_titulo_lista = Label(self, text="Lista de Carreras")
        self.label_titulo_lista.grid(row=4, column=0, columnspan=2, pady=10, padx=10)

        #================ TABLA ================#
        self.tabla = ttk.Treeview(self, columns=('', ''))
        self.tabla.grid(row=5, column=0, columnspan=2, pady=10, padx=10)
        self.tabla.heading("#0", text="Codigo")
        self.tabla.heading("#1", text="Nombre")
        self.tabla.heading("#2", text="Duracion")

        def editar_datos_ventana():
            
            codigo = self.tabla.item(self.tabla.selection())['text']
            nombre_antiguo = self.tabla.item(self.tabla.selection())['values'][0]
            duracion_antigua = self.tabla.item(self.tabla.selection())['values'][1]

            #ARRANQUE DE VENTANA EMERENTE
            self.ventana_editar = Toplevel()
            self.ventana_editar.title("Editar Carrera")
            
            #================ LABEL Y CAMPO DE CODIGO ================#
            self.label_codigo = Label(self.ventana_editar, text="Codigo de la Carrera:")
            self.label_codigo.grid(row=0, column=0, pady=10, padx=10)
            self.entry_codigo = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=codigo), state='readonly')
            self.entry_codigo.grid(row=0, column=1, pady=10, padx=10)

            #================ LABEL Y CAMPO DE NOMBRE ANTIGUO ================#
            self.label_nombre_antiguo = Label(self.ventana_editar, text="Nombre de la Carrera Antigua:")
            self.label_nombre_antiguo.grid(row=1, column=0, pady=10, padx=10)
            self.entry_nombre_antiguo = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=nombre_antiguo), state='readonly')
            self.entry_nombre_antiguo.grid(row=1, column=1, pady=10, padx=10)

            #================ LABEL Y CAMPO DE NOMBRE NUEVO ================#
            self.label_nombre_nuevo = Label(self.ventana_editar, text="Nombre de la Carrera Nueva:")
            self.label_nombre_nuevo.grid(row=2, column=0, pady=10, padx=10)
            self.entry_nombre_nuevo = Entry(self.ventana_editar)
            self.entry_nombre_nuevo.grid(row=2, column=1, pady=10, padx=10)

            #================ LABEL Y CAMPO DURACION ANTIGUO ================#
            self.label_duracion_antiguo = Label(self.ventana_editar, text="Duracion de la Carrera Antigua:")
            self.label_duracion_antiguo.grid(row=3, column=0, pady=10, padx=10)
            self.entry_duracion_antiguo = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=duracion_antigua), state='readonly')
            self.entry_duracion_antiguo.grid(row=3, column=1, pady=10, padx=10)

            #================ LABEL Y CAMPO DURACION NUEVA ================#
            self.label_duracion_nuevo = Label(self.ventana_editar, text="Duracion de la Carrera Nueva:")
            self.label_duracion_nuevo.grid(row=4, column=0, pady=10, padx=10)
            self.entry_duracion_nuevo = Entry(self.ventana_editar)
            self.entry_duracion_nuevo.grid(row=4, column=1, pady=10, padx=10)

            #================ BOTON ACTUALIZAR ================#
            self.boton_actualizar = Button(self.ventana_editar, text="ACTUALIZAR CARRERA", command = lambda: editar_datos(codigo, codigo, self.entry_nombre_nuevo.get(), nombre_antiguo, self.entry_duracion_nuevo.get(), duracion_antigua))
            self.boton_actualizar.grid(row=5, column=0, columnspan=2, pady=10, padx=10)

        #================ BOTONES EDITAR Y ELIMINAR ================#
        self.boton_editar = Button(self, text="EDITAR CARRERA", command=editar_datos_ventana)
        self.boton_editar.grid(row=6, column=0, pady=10, padx=10)

        self.boton_eliminar = Button(self, text="ELIMINAR CARRERA", command=eliminar_datos)
        self.boton_eliminar.grid(row=6, column=1, pady=10, padx=10)

        #Funcion Listar datos
        def listar_datos():
            #Eliminar datos de la tabla
            recorrer_tabla = self.tabla.get_children()
            for element in recorrer_tabla:
                self.tabla.delete(element)
            
            #Ejecutar la consulta y cargar los datos
            query = 'SELECT * FROM carrera'
            conexion = Conectar_db()
            datos = conexion.run_db(query)

            for carrera in datos:
                self.tabla.insert('', 0, text=carrera[0], value=(carrera[1], carrera[2]))
        
        listar_datos()