from tkinter import *
from tkinter import ttk
from conexion_DB.consultas_db import *

class VistaProfe(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def nuevo():
            self.entry_nombre.config(state= "normal")
            self.entry_telefono.config(state= "normal")
            self.entry_direccion.config(state= "normal")

        #Inserta datos a la DB
        def insertar_datos():
            
            query = 'INSERT INTO profesor VALUES (NULL, ?, ?, ?)'
            parametros = (self.entry_nombre.get(), self.entry_telefono.get(), self.entry_direccion.get())

            conexion = Conectar_db()
            conexion.run_db(query, parametros)
            
            #Limpiar campos
            self.entry_nombre.delete(0, END)
            self.entry_telefono.delete(0, END)
            self.entry_direccion.delete(0, END)
        
            #Actualizar tabla
            listar_datos()
        
        #Eliminar datos
        def eliminar_datos():
            codigo = self.tabla.item(self.tabla.selection())['text']
            query = 'DELETE FROM profesor WHERE codigo_p = ?'
            conexion = Conectar_db()
            conexion.run_db(query, (codigo,))

            #Actualizar tabla
            listar_datos()
        
        #Actualizar datos
        def editar_datos(codigo_n, codigo_a, nombre_nuevo, nombre_antiguo, telefono_nuevo, telefono_antiguo, direccion_nuevo, direccion_antiguo):
            query = 'UPDATE profesor SET codigo_p = ?, nombre_p = ?, telefono_p = ?, direccion_p = ? WHERE codigo_p = ? AND nombre_p = ? AND telefono_p = ? AND direccion_p = ?'
            parametros = (codigo_n, nombre_nuevo, telefono_nuevo, direccion_nuevo, codigo_a, nombre_antiguo, telefono_antiguo, direccion_antiguo)
            conexion = Conectar_db()
            conexion.run_db(query, parametros)

            #Destruye la ventana 
            self.ventana_editar.destroy()

            #Actualizar tabla
            listar_datos()

        #================ LABEL TITULO REGISTRAR ================#
        self.label_titulo = Label(self, text="REGISTRAR NUEVO PROFESOR")
        self.label_titulo.grid(row=0, column=0, columnspan=2)

        #================ CAMPO NOMBRE DEL PROFESOR ================#
        self.label_nombre = Label(self, text="Nombre")
        self.label_nombre.grid(row=1, column=0, pady=10, padx=10)
        self.entry_nombre = Entry(self, state='readonly')
        self.entry_nombre.grid(row=1, column=1, pady=10, padx=10)

        #================ CAMPO NÚMERO DE TELEFONO ================#
        self.label_telefono = Label(self, text="Telefono")
        self.label_telefono.grid(row=2, column=0, pady=10, padx=10)
        self.entry_telefono = Entry(self, state='readonly')
        self.entry_telefono.grid(row=2, column=1, pady=10, padx=10)

        #================ CAMPO DIRECCION ================#
        self.label_direccion = Label(self, text="Direccion")
        self.label_direccion.grid(row=3, column=0, pady=10, padx=10)
        self.entry_direccion = Entry(self, state='readonly')
        self.entry_direccion.grid(row=3, column=1, pady=10, padx=10)

        #================ BOTONES REGISTRAR Y GUARDAR ================#
        self.boton_registrar = Button(self, text="REGISTRAR", command=nuevo)
        self.boton_registrar.grid(row=4, column=0, pady=10, padx=10)

        self.boton_guardar = Button(self, text="GUARDAR", command=insertar_datos)
        self.boton_guardar.grid(row=4, column=1, pady=10, padx=10)

        #================ LABEL TITULO LISTA ================#
        self.label_titulo_lista = Label(self, text="Lista de Profesores")
        self.label_titulo_lista.grid(row=5, column=0, columnspan=2, pady=10, padx=10)

        #================ TABLA ================#
        self.tabla = ttk.Treeview(self, columns=('', '', ''))
        self.tabla.grid(row=6, column=0, columnspan=2, pady=10, padx=10)
        self.tabla.heading("#0", text="Codigo")
        self.tabla.heading("#1", text="Nombre")
        self.tabla.heading("#2", text="Telefono")
        self.tabla.heading("#3", text="Direccion")

        #================ FUNCION VENTANA EMERGENTE EDITAR ================#
        def editar_datos_ventana():
            
            codigo = self.tabla.item(self.tabla.selection())['text']
            nombre_antiguo = self.tabla.item(self.tabla.selection())['values'][0]
            telefono_antiguo = self.tabla.item(self.tabla.selection())['values'][1]
            direccion_antiguo = self.tabla.item(self.tabla.selection())['values'][2]

            #ARRANQUE DE VENTANA
            self.ventana_editar = Toplevel()
            self.ventana_editar.title("Editar Carrera")
            
            #================ LABEL Y CAMPO DE CODIGO ================#
            self.label_codigo = Label(self.ventana_editar, text="Codigo del Profesor:")
            self.label_codigo.grid(row=0, column=0, pady=10, padx=10)
            self.entry_codigo = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=codigo), state='readonly')
            self.entry_codigo.grid(row=0, column=1, pady=10, padx=10)

            #================ LABEL Y CAMPO DE NOMBRE ANTIGUO ================#
            self.label_nombre_antiguo = Label(self.ventana_editar, text="Nombre del Profesor Antiguo:")
            self.label_nombre_antiguo.grid(row=1, column=0, pady=10, padx=10)
            self.entry_nombre_antiguo = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=nombre_antiguo), state='readonly')
            self.entry_nombre_antiguo.grid(row=1, column=1, pady=10, padx=10)

            #================ LABEL Y CAMPO DE NOMBRE NUEVO ================#
            self.label_nombre_nuevo = Label(self.ventana_editar, text="Nombre del Profesor Nuevo:")
            self.label_nombre_nuevo.grid(row=2, column=0, pady=10, padx=10)
            self.entry_nombre_nuevo = Entry(self.ventana_editar)
            self.entry_nombre_nuevo.grid(row=2, column=1, pady=10, padx=10)

            #================ LABEL Y CAMPO TELEFONO ANTIGUO ================#
            self.label_telefono_antiguo = Label(self.ventana_editar, text="Telefono del Profesor Antiguo:")
            self.label_telefono_antiguo.grid(row=3, column=0, pady=10, padx=10)
            self.entry_telefono_antiguo = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=telefono_antiguo), state='readonly')
            self.entry_telefono_antiguo.grid(row=3, column=1, pady=10, padx=10)

            #================ LABEL Y CAMPO CREDITO NUEVA ================#
            self.label_telefono_nuevo = Label(self.ventana_editar, text="Telefono del Profesor Nuevo:")
            self.label_telefono_nuevo.grid(row=4, column=0, pady=10, padx=10)
            self.entry_telefono_nuevo = Entry(self.ventana_editar)
            self.entry_telefono_nuevo.grid(row=4, column=1, pady=10, padx=10)

            #================ LABEL Y CAMPO DIRECCION ANTIGUO ================#
            self.label_direccion_antiguo = Label(self.ventana_editar, text="Direccion del Profesor Antiguo:")
            self.label_direccion_antiguo.grid(row=5, column=0, pady=10, padx=10)
            self.entry_direccion_antiguo = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=direccion_antiguo), state='readonly')
            self.entry_direccion_antiguo.grid(row=5, column=1, pady=10, padx=10)

            #================ LABEL Y CAMPO DIRECCION NUEVO ================#
            self.label_direccion_nuevo = Label(self.ventana_editar, text="Direccion del Profesor Nuevo:")
            self.label_direccion_nuevo.grid(row=6, column=0, pady=10, padx=10)
            self.entry_direccion_nuevo = Entry(self.ventana_editar)
            self.entry_direccion_nuevo.grid(row=6, column=1, pady=10, padx=10)

            #================ BOTON ACTUALIZAR ================#
            self.boton_actualizar = Button(self.ventana_editar, text="ACTUALIZAR PROFESOR", command=lambda: editar_datos(codigo, codigo, self.entry_nombre_nuevo.get(), nombre_antiguo, self.entry_telefono_nuevo.get(), telefono_antiguo, self.entry_direccion_nuevo.get(), direccion_antiguo))
            self.boton_actualizar.grid(row=7, column=0, columnspan=2, pady=10, padx=10)

        #================ BOTONES EDITAR Y ELIMINAR ================#
        self.boton_editar = Button(self, text="EDITAR", command=editar_datos_ventana)
        self.boton_editar.grid(row=7, column=0, pady=10, padx=10)

        self.boton_eliminar = Button(self, text="ELIMINAR", command=eliminar_datos)
        self.boton_eliminar.grid(row=7, column=1, pady=10, padx=10)

        #Funcion Listar datos
        def listar_datos():
            #Eliminar datos de la tabla
            recorrer_tabla = self.tabla.get_children()
            for element in recorrer_tabla:
                self.tabla.delete(element)
            
            #Ejecutar la consulta y cargar los datos
            query = 'SELECT * FROM profesor'
            conexion = Conectar_db()
            datos = conexion.run_db(query)

            for profesor in datos:
                self.tabla.insert('', 0, text=profesor[0], value=(profesor[1], profesor[2], profesor[3]))
        
        listar_datos()