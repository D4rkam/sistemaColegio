from tkinter import *
from tkinter import ttk
from visual.frame_carrera import *
from visual.frame_materia import *
from visual.frame_profesores import *
from visual.frame_alumnos import *


class Aplicacion(ttk.Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

#================ VENTANA ================#  
        self.mi_ventana = ventana
        self.mi_ventana.title("Sistema Escolar")
        self.mi_ventana.iconbitmap("img/EmbeddedImage.ico")

#================ CONTENEDOR DE PANELES ================#
        self.navegador = ttk.Notebook(self)

#================ PANEL DE INICIO ================#   
        self.inicio = Label(self.navegador, text="Pagina de inicio")
        self.navegador.add(self.inicio, text="INICIO")

#================ PANEL DE CARRERA ================# 
        self.resg_carrera = VistaCarrera(self.navegador)
        self.navegador.add(self.resg_carrera, text="CARRERA")

#================ PANEL DE MATERIA================#
        self.resg_materia = VistaMateria(self.navegador)
        self.navegador.add(self.resg_materia, text="MATERIA")

#================ PANEL DE PROFESORES ================# 
        self.resg_profe = VistaProfe(self.navegador)
        self.navegador.add(self.resg_profe, text="PROFESOR")

#================ PANEL DE MATERIA================#
        self.resg_alumno = VistaAlumnos(self.navegador)
        self.navegador.add(self.resg_alumno, text="ALUMNO")

        self.navegador.pack()
        self.pack()