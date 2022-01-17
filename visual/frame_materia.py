from tkinter import *
from tkinter import ttk
from conexion_DB.consultas_db import *

class VistaMateria(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def nuevo():
            self.entry_nombre.config(state= "normal")
            self.entry_credito.config(state="normal")
        
        #Inserta datos a la DB
        def insertar_datos():
            
            query = 'INSERT INTO materia VALUES (NULL, ?, ?)'
            parametros = (self.entry_nombre.get(), self.entry_credito.get())

            conexion = Conectar_db()
            conexion.run_db(query, parametros)
            
            #Limpiar campos
            self.entry_nombre.delete(0, END)
            self.entry_credito.delete(0, END)
        
            #Actualizar tabla
            listar_datos()
        
        #Eliminar datos
        def eliminar_datos():
            codigo = self.tabla.item(self.tabla.selection())['text']
            query = 'DELETE FROM materia WHERE codigo_m = ?'
            conexion = Conectar_db()
            conexion.run_db(query, (codigo,))

            #Actualizar tabla
            listar_datos()
        
        #Actualizar datos
        def editar_datos(codigo_n, codigo_a, nombre_nuevo, nombre_antiguo, credito_nuevo, credito_antiguo):
            query = 'UPDATE materia SET codigo_m = ?, nombre_m = ?, creditos_m = ? WHERE codigo_m = ? AND nombre_m = ? AND creditos_m = ?'
            parametros = (codigo_n, nombre_nuevo, credito_nuevo, codigo_a, nombre_antiguo, credito_antiguo)
            conexion = Conectar_db()
            conexion.run_db(query, parametros)

            #Destruye la ventana 
            self.ventana_editar.destroy()

            #Actualizar tabla
            listar_datos()

        #================ LABEL TITULO REGISTRAR ================#
        self.label_titulo = Label(self, text="REGISTRAR NUEVA MATERIA")
        self.label_titulo.grid(row=0, column=0, columnspan=2)

        #================ CAMPO NOMBRE MATERIA ================#
        self.label_nombre = Label(self, text="Nombre")
        self.label_nombre.grid(row=1, column=0, pady=10, padx=10)
        self.entry_nombre = Entry(self, state='readonly')
        self.entry_nombre.grid(row=1, column=1, pady=10, padx=10)

        #================ CAMPO CREDITO MATERIA ================#
        self.label_credito = Label(self, text="Creditos")
        self.label_credito.grid(row=2, column=0, pady=10, padx=10)
        self.entry_credito = Entry(self, state='readonly')
        self.entry_credito.grid(row=2, column=1, pady=10, padx=10)

        #================ BOTONES REGISTRAR Y GUARDAR ================#
        self.boton_registrar = Button(self, text="REGISTRAR", command=nuevo)
        self.boton_registrar.grid(row=3, column=0, pady=10, padx=10)

        self.boton_guardar = Button(self, text="GUARDAR", command=insertar_datos)
        self.boton_guardar.grid(row=3, column=1, pady=10, padx=10)

        #================ LABEL TITULO LISTA ================#
        self.label_titulo_lista = Label(self, text="Lista de Materias")
        self.label_titulo_lista.grid(row=4, column=0, columnspan=2, pady=10, padx=10)

        #================ TABLA ================#
        self.tabla = ttk.Treeview(self, columns=('', ''))
        self.tabla.grid(row=5, column=0, columnspan=2, pady=10, padx=10)
        self.tabla.heading("#0", text="Codigo")
        self.tabla.heading("#1", text="Nombre")
        self.tabla.heading("#2", text="Credito")

        #================ FUNCION VENTANA EMERGENTE EDITAR ================#
        def editar_datos_ventana():
            
            codigo = self.tabla.item(self.tabla.selection())['text']
            nombre_antiguo = self.tabla.item(self.tabla.selection())['values'][0]
            credito_antiguo = self.tabla.item(self.tabla.selection())['values'][1]

            #ARRANQUE DE VENTANA
            self.ventana_editar = Toplevel()
            self.ventana_editar.title("Editar Carrera")
            
            #================ LABEL Y CAMPO DE CODIGO ================#
            self.label_codigo = Label(self.ventana_editar, text="Codigo de la Materia:")
            self.label_codigo.grid(row=0, column=0, pady=10, padx=10)
            self.entry_codigo = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=codigo), state='readonly')
            self.entry_codigo.grid(row=0, column=1, pady=10, padx=10)

            #================ LABEL Y CAMPO DE NOMBRE ANTIGUO ================#
            self.label_nombre_antiguo = Label(self.ventana_editar, text="Nombre de la Materia Antigua:")
            self.label_nombre_antiguo.grid(row=1, column=0, pady=10, padx=10)
            self.entry_nombre_antiguo = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=nombre_antiguo), state='readonly')
            self.entry_nombre_antiguo.grid(row=1, column=1, pady=10, padx=10)

            #================ LABEL Y CAMPO DE NOMBRE NUEVO ================#
            self.label_nombre_nuevo = Label(self.ventana_editar, text="Nombre de la Materia Nueva:")
            self.label_nombre_nuevo.grid(row=2, column=0, pady=10, padx=10)
            self.entry_nombre_nuevo = Entry(self.ventana_editar)
            self.entry_nombre_nuevo.grid(row=2, column=1, pady=10, padx=10)

            #================ LABEL Y CAMPO CREDITO ANTIGUO ================#
            self.label_credito_antiguo = Label(self.ventana_editar, text="Credito de la Materia Antigua:")
            self.label_credito_antiguo.grid(row=3, column=0, pady=10, padx=10)
            self.entry_credito_antiguo = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=credito_antiguo),state='readonly')
            self.entry_credito_antiguo.grid(row=3, column=1, pady=10, padx=10)

            #================ LABEL Y CAMPO CREDITO NUEVA ================#
            self.label_credito_nuevo = Label(self.ventana_editar, text="Credito de la Materia Nueva:")
            self.label_credito_nuevo.grid(row=4, column=0, pady=10, padx=10)
            self.entry_credito_nuevo = Entry(self.ventana_editar)
            self.entry_credito_nuevo.grid(row=4, column=1, pady=10, padx=10)

            #================ BOTON ACTUALIZAR ================#
            self.boton_actualizar = Button(self.ventana_editar, text="ACTUALIZAR MATERIA", command=lambda: editar_datos(codigo, codigo, self.entry_nombre_nuevo.get(), nombre_antiguo, self.entry_credito_nuevo.get(), credito_antiguo))
            self.boton_actualizar.grid(row=5, column=0, columnspan=2, pady=10, padx=10)

        #================ BOTONES EDITAR Y ELIMINAR ================#
        self.boton_editar = Button(self, text="EDITAR", command=editar_datos_ventana)
        self.boton_editar.grid(row=6, column=0, pady=10, padx=10)

        self.boton_eliminar = Button(self, text="ELIMINAR", command=eliminar_datos)
        self.boton_eliminar.grid(row=6, column=1, pady=10, padx=10)

        #Funcion Listar datos
        def listar_datos():
            #Eliminar datos de la tabla
            recorrer_tabla = self.tabla.get_children()
            for element in recorrer_tabla:
                self.tabla.delete(element)
            
            #Ejecutar la consulta y cargar los datos
            query = 'SELECT * FROM materia'
            conexion = Conectar_db()
            datos = conexion.run_db(query)

            for materia in datos:
                self.tabla.insert('', 0, text=materia[0], value=(materia[1], materia[2]))
        
        listar_datos()