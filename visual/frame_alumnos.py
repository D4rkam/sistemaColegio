from tkinter import *
from tkinter import ttk
from conexion_DB.consultas_db import *

class VistaAlumnos(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def nuevo():
            self.entry_nombre.config(state= "normal")
            self.entry_edad.config(state= "normal")
            self.entry_telefono.config(state= "normal")
        
        #Inserta datos a la DB
        def insertar_datos():
            query = 'INSERT INTO carrera VALUES (NULL, ?, ?, ?)'
            parametros = (self.entry_nombre.get(), self.entry_edad.get(), self.entry_telefono.get())

            conexion = Conectar_db()
            conexion.run_db(query, parametros)
            
            #Limpiar campos
            self.entry_nombre.delete(0, END)
            self.entry_edad.delete(0, END)
            self.entry_telefono.delete(0, END)
        
            #Actualizar tabla
            listar_datos()
        
        #Eliminar datos
        def eliminar_datos():
            codigo = self.tabla.item(self.tabla.selection())['text']
            query = 'DELETE FROM alumnos WHERE codigo_a = ?'
            conexion = Conectar_db()
            conexion.run_db(query, (codigo,))

            #Actualizar tabla
            listar_datos()

        #Actualizar datos
        def editar_datos(codigo_n, codigo_a, nombre_nuevo, nombre_antiguo, edad_nuevo, edad_antiguo, telefono_nuevo, telefono_antiguo, carrera_a_nuevo, carrera_a_antiguo):
            query = 'UPDATE alumno SET codigo_a = ?, nombre_a = ?,edad_a = ?, telefono_a = ? WHERE codigo_a = ? AND nombre_a = ? AND edad_a = ? AND telefono_a = ?'
            parametros = (codigo_n, nombre_nuevo, edad_nuevo, telefono_nuevo, carrera_a_nuevo ,codigo_a, nombre_antiguo, edad_antiguo, telefono_antiguo, carrera_a_antiguo)
            conexion = Conectar_db()
            conexion.run_db(query, parametros)

            #Destruye la ventana 
            self.ventana_editar.destroy()

            #Actualizar tabla
            listar_datos()
        
        #================ LABEL TITULO REGISTRAR ================#
        self.label_titulo_registrar = Label(self, text="REGISTRAR NUEVO ALUMNO")
        self.label_titulo_registrar.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        #================ LABEL Y CAMPO DE NOMBRE ================#
        self.label_nombre = Label(self, text="Nombre")
        self.label_nombre.grid(row=1, column=0, pady=10, padx=10)
        self.entry_nombre = Entry(self, state='readonly')
        self.entry_nombre.grid(row=1, column=1, pady=10, padx=10)

        #================ LABEL Y CAMPO DE EDAD ================#
        self.label_edad = Label(self, text="Edad")
        self.label_edad.grid(row=2, column=0, pady=10, padx=10)
        self.entry_edad = Entry(self, state='readonly')
        self.entry_edad.grid(row=2, column=1, pady=10, padx=10)

        #================ LABEL Y CAMPO DE TELEFONO ================#
        self.label_telefono = Label(self, text="Telefono")
        self.label_telefono.grid(row=3, column=0, pady=10, padx=10)
        self.entry_telefono = Entry(self, state='readonly')
        self.entry_telefono.grid(row=3, column=1, pady=10, padx=10)

        #================ LABEL Y CAMPO DE CARRERA ALUMNO ================#
        self.label_carrera_a = Label(self, text="Telefono")
        self.label_carrera_a.grid(row=3, column=0, pady=10, padx=10)
        self.entry_carrera_a = Entry(self, state='readonly')
        self.entry_carrera_a.grid(row=3, column=1, pady=10, padx=10)

        #================ BOTONES REGISTRAR Y GUARDAR ================#
        self.boton_nuevo = Button(self, text="REGISTRAR", command=nuevo)
        self.boton_nuevo.grid(row=4, column=0, pady=10, padx=10)

        self.boton_guardar = Button(self, text="GUARDAR", command=insertar_datos)
        self.boton_guardar.grid(row=4, column=1, pady=10, padx=10)

        #================ LABEL TITULO LISTA ================#
        self.label_titulo_lista = Label(self, text="Lista de Alumnos")
        self.label_titulo_lista.grid(row=5, column=0, columnspan=2, pady=10, padx=10)

        #================ TABLA ================#
        self.tabla = ttk.Treeview(self, columns=('', '', '', ''))
        self.tabla.grid(row=6, column=0, columnspan=2, pady=10, padx=10)
        self.tabla.heading("#0", text="Codigo")
        self.tabla.heading("#1", text="Nombre")
        self.tabla.heading("#2", text="Edad")
        self.tabla.heading("#3", text="Telefono")
        self.tabla.heading("#4", text="Carrera")

        #================ FUNCION VENTANA EMERGENTE EDITAR ================#
        def editar_datos_ventana():

            codigo = self.tabla.item(self.tabla.selection())['text']
            nombre_antiguo = self.tabla.item(self.tabla.selection())['values'][0]
            edad_antiguo = self.tabla.item(self.tabla.selection())['values'][1]
            telefono_antiguo = self.tabla.item(self.tabla.selection())['values'][2]
            carrera_a_antiguo = self.tabla.item(self.tabla.selection())['values'][3]

            #ARRANQUE DE VENTANA
            self.ventana_editar = Toplevel()
            self.ventana_editar.title("Editar Alumno")
            
            #================ LABEL Y CAMPO DE CODIGO ================#
            self.label_codigo = Label(self.ventana_editar, text="Codigo del Alumno:")
            self.label_codigo.grid(row=0, column=0, pady=10, padx=10)
            self.entry_codigo = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=codigo), state='readonly')
            self.entry_codigo.grid(row=0, column=1, pady=10, padx=10)

            #================ LABEL Y CAMPO DE NOMBRE ANTIGUO ================#
            self.label_nombre_antiguo = Label(self.ventana_editar, text="Nombre del Alumno Antiguo:")
            self.label_nombre_antiguo.grid(row=1, column=0, pady=10, padx=10)
            self.entry_nombre_antiguo = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=nombre_antiguo), state='readonly')
            self.entry_nombre_antiguo.grid(row=1, column=1, pady=10, padx=10)

            #================ LABEL Y CAMPO DE NOMBRE NUEVO ================#
            self.label_nombre_nuevo = Label(self.ventana_editar, text="Nombre del Alumno Nuevo:")
            self.label_nombre_nuevo.grid(row=2, column=0, pady=10, padx=10)
            self.entry_nombre_nuevo = Entry(self.ventana_editar)
            self.entry_nombre_nuevo.grid(row=2, column=1, pady=10, padx=10)

            #================ LABEL Y CAMPO EDAD ANTIGUO ================#
            self.label_edad_antiguo = Label(self.ventana_editar, text="Edad del Alumno Antiguo:")
            self.label_edad_antiguo.grid(row=3, column=0, pady=10, padx=10)
            self.entry_edad_antiguo = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=edad_antiguo), state='readonly')
            self.entry_edad_antiguo.grid(row=3, column=1, pady=10, padx=10)

            #================ LABEL Y CAMPO EDAD NUEVO ================#
            self.label_edad_nuevo = Label(self.ventana_editar, text="Edad del Alumno Nuevo:")
            self.label_edad_nuevo.grid(row=4, column=0, pady=10, padx=10)
            self.entry_edad_nuevo = Entry(self.ventana_editar)
            self.entry_edad_nuevo.grid(row=4, column=1, pady=10, padx=10)

            #================ LABEL Y CAMPO TELEFONO ANTIGUO ================#
            self.label_telefono_antiguo = Label(self.ventana_editar, text="Telefono del Alumno Antiguo:")
            self.label_telefono_antiguo.grid(row=5, column=0, pady=10, padx=10)
            self.entry_carrera_a_antiguo = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=telefono_antiguo), state='readonly')
            self.entry_telefono_antiguo.grid(row=5, column=1, pady=10, padx=10)

            #================ LABEL Y CAMPO TELEFONO NUEVO ================#
            self.label_telefono_nuevo = Label(self.ventana_editar, text="Telefono del Alumno Nuevo:")
            self.label_telefono_nuevo.grid(row=6, column=0, pady=10, padx=10)
            self.entry_telefono_nuevo = Entry(self.ventana_editar)
            self.entry_telefono_nuevo.grid(row=6, column=1, pady=10, padx=10)

            #================ LABEL Y CAMPO CARRERA ALUMNO ANTIGUO ================#
            self.label_carrera_a_antiguo = Label(self.ventana_editar, text="Carrera del Alumno Antiguo:")
            self.label_carrera_a_antiguo.grid(row=5, column=0, pady=10, padx=10)
            self.entry_carrera_a_antiguo = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=""), state='readonly')
            self.entry_carrera_a_antiguo.grid(row=5, column=1, pady=10, padx=10)

            #================ LABEL Y CAMPO CARRERA ALUMNO NUEVO ================#
            self.label_telefono_nuevo = Label(self.ventana_editar, text="Carrera del Alumno Nuevo:")
            self.label_telefono_nuevo.grid(row=6, column=0, pady=10, padx=10)
            self.entry_telefono_nuevo = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=carrera_a_antiguo))
            self.entry_telefono_nuevo.grid(row=6, column=1, pady=10, padx=10)

            #================ BOTON ACTUALIZAR ================#
            self.boton_actualizar = Button(self.ventana_editar, text="ACTUALIZAR ALUMNO", command = lambda: editar_datos(codigo, codigo, self.entry_nombre_nuevo.get(), nombre_antiguo, self.entry_edad.get(), edad_antiguo, self.entry_telefono.get(), telefono_antiguo, self.entry_carrera_a_nuevo, carrera_a_antiguo))
            self.boton_actualizar.grid(row=7, column=0, columnspan=2, pady=10, padx=10)

        #================ BOTONES EDITAR Y ELIMINAR ================#
        self.boton_editar = Button(self, text="EDITAR ALUMNO", command=editar_datos_ventana)
        self.boton_editar.grid(row=7, column=0, pady=10, padx=10)

        self.boton_eliminar = Button(self, text="ELIMINAR ALUMNO", command=eliminar_datos)
        self.boton_eliminar.grid(row=7, column=1, pady=10, padx=10)

        #Funcion Listar datos
        def listar_datos():
            #Eliminar datos de la tabla
            recorrer_tabla = self.tabla.get_children()
            for element in recorrer_tabla:
                self.tabla.delete(element)
            
            #Ejecutar la consulta y cargar los datos
            query = '''SELECT codigo_a, nombre_a, edad_a, telefono_a, nombre_c FROM alumno
                    INNER JOIN carrera ON alumno.codigo_c1 = carrera.codigo_c'''

            conexion = Conectar_db()
            datos = conexion.run_db(query)

            for alumno in datos:
                self.tabla.insert('', 0, text=alumno[0], value=(alumno[1], alumno[2], alumno[3], alumno[4]))
        
        listar_datos()