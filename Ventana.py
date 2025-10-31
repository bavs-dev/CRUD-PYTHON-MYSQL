from tkinter import *
from tkinter import ttk
from Seguridad import  *
from CRUD import *
import tkinter.messagebox

#libreria o clase que mandamos a llamar para utilizar el logger
from logger_config import get_logger

# Obtener el logger para la aplicación
logger = get_logger("Ventana")

#clase que genera el diseño
class Ventana(Frame):
    #instancia que permite mandar a llamar la conecion y los metodos que necesitamos
    OBCRUD=CRUD()

    #constructor crea el frame asi mismo carga los datos requeridos
    def __init__(self,master=None):
        super().__init__(master,width=680,height=300)
        self.master=master
        self.pack()
        self.create_widgets()
        self.llenaDatoss()

    #limpiar
    def Limpiar(self):
        self.txtNombre.delete(0,END)
        self.txtApellido.delete(0,END)
        self.txtEdad.delete(0,END)
        self.txtCarrera.delete(0,END)
        pass
    


    def fNuevod(self):
        seguridad = Seguridad()

        # Cifrar los datos y convertir a base64
        nombre_cifrado = seguridad.cifrar_datos(self.txtNombre.get())
        apellido_cifrado = seguridad.cifrar_datos(self.txtApellido.get())
        edad_cifrada = seguridad.cifrar_datos(self.txtEdad.get())
        carrera_cifrada = seguridad.cifrar_datos(self.txtCarrera.get())

        # Insertar los datos cifrados (en formato base64) en la base de datos
        self.OBCRUD.insertars(nombre_cifrado, apellido_cifrado, edad_cifrada, carrera_cifrada)

        tkinter.messagebox.showinfo("CRUD", "Se Añadió a la BD (Cifrado con AES y Base64)")
        logger.info("Inicio de la aplicación.")
        self.Limpiar()

    #metodo que solo sirve para mandar mensaje
    def fGuardar(self):
        tkinter.messagebox.showinfo("CRUD","Guardar")
        pass

#modifica la el valor en la bd
    def fModificars(self):
        seguridad = Seguridad()

        # Cifrar los datos antes de pasarlos a la consulta SQL
        nombre_cifrado = seguridad.cifrar_datos(self.txtNombre.get())
        apellido_cifrado = seguridad.cifrar_datos(self.txtApellido.get())
        edad_cifrada = seguridad.cifrar_datos(self.txtEdad.get())
        carrera_cifrada = seguridad.cifrar_datos(self.txtCarrera.get())
        id_usuario = self.txtID.get()

        # Llamar al método de actualización (UPDATE) de la base de datos
        self.OBCRUD.updatesqls(nombre_cifrado, apellido_cifrado, edad_cifrada, carrera_cifrada, id_usuario)

        # Mostrar un mensaje de éxito
        tkinter.messagebox.showinfo("CRUD", "Se modificó el dato")

        # Limpiar los campos de texto
        self.Limpiar()

#elimina el valor de la bd
    def fEliminar(self):
        self.OBCRUD.deletesql(self.txtID.get())
        self.Limpiar()
        tkinter.messagebox.showinfo("CRUD","eliminado")
        pass

    #metodo que solo amnda un mensaje de cancelar
    def fCalcelar(self):
        tkinter.messagebox.showinfo("CRUD","Cancelar")
        pass


#metodo que consulta  los valores de la tabla conforme al id
    def fConsultars(self):
        seguridad = Seguridad()

        # Consultar los datos cifrados de la base de datos
        datos_cifrados = self.OBCRUD.consulta_user(self.txtID.get())

        if datos_cifrados != 0:
            # Descifrar los datos
            nombre_descifrado = seguridad.descifrar_datos(datos_cifrados[1])
            apellido_descifrado = seguridad.descifrar_datos(datos_cifrados[2])
            edad_descifrada = seguridad.descifrar_datos(datos_cifrados[3])
            carrera_descifrada = seguridad.descifrar_datos(datos_cifrados[4])

            # Mostrar los datos descifrados en los campos de texto
            self.txtNombre.insert(0, nombre_descifrado)
            self.txtApellido.insert(0, apellido_descifrado)
            self.txtEdad.insert(0, edad_descifrada)
            self.txtCarrera.insert(0, carrera_descifrada)

            tkinter.messagebox.showinfo("CRUD", "Se encontró el dato")
        else:
            tkinter.messagebox.showinfo("CRUD", "No se encontró el dato")


#metodo que llena la tabla y cosulta valores
    def llenaDatoss(self):
        seguridad = Seguridad()

        # Consultar todos los datos cifrados de la base de datos
        datos_cifrados = self.OBCRUD.consulta_usarios()  # Asume consulta de todos los usuarios

        for row in datos_cifrados:
            # Descifrar los datos
            nombre_descifrado = seguridad.descifrar_datos(row[1])
            apellido_descifrado = seguridad.descifrar_datos(row[2])
            edad_descifrada = seguridad.descifrar_datos(row[3])
            carrera_descifrada = seguridad.descifrar_datos(row[4])

            # Insertar los datos descifrados en la interfaz gráfica (ej. Treeview)
            self.grid.insert("", END, text=row[0],
                             values=(nombre_descifrado, apellido_descifrado, edad_descifrada, carrera_descifrada))

        if len(self.grid.get_children()) > 0:
            self.grid.selection_set(self.grid.get_children()[0])

    #este permite  destuye
    def Cerrar(self):
        self.destroy() 
  
#cierra la conexion
    def CerrarConexionMYSQL(self):
        self.OBCRUD.CerrarConexion()
        self.Cerrar()
        exit()
        pass
#llena los datos de la tabla
    def tabla(self):
        self.grid.destroy()
        self.create_widgets()
        #self.llenaDatos()
        self.llenaDatoss()
        pass


    def create_widgets(self):
        #frame 1 botones
        frame1 = Frame(self, bg="#0E80C6")
        frame1.place(x=0,y=0, width=94,height=300)
        
        #botones del fram1
        self.btnNew = Button(frame1, text="Añadir", command=self.fNuevod, bg="#FEF5E7", fg="#000000")
        self.btnNew.place(x=5,y=50, width=80, height=30)

        self.btnModificar=Button(frame1, text="Modificar", command=self.fModificars, bg="#FEF5E7", fg="#000000")
        self.btnModificar.place(x=5, y=90,width=80,height=40)

        self.btnEliminar = Button(frame1, text="Eliminar", command=self.fEliminar, bg="#FEF5E7", fg="#000000")
        self.btnEliminar.place(x=5,y=135, width=80, height=30)

        self.btnConsultar = Button(frame1, text="Consultar", command=self.fConsultars, bg="#FEF5E7", fg="#000000")
        self.btnConsultar.place(x=5,y=170, width=80, height=30)

        self.btnclear = Button(frame1,text="LIMPIAR", command=self.Limpiar, bg="#FEF5E7", fg="#000000")
        self.btnclear.place(x=5,y=205, width=80, height=30)

        self.btntabla = Button(frame1,text="Actualizar", command=self.tabla, bg="#FEF5E7", fg="#000000")
        self.btntabla.place(x=5,y=240, width=80, height=30)

        self.btnsalir= Button(frame1,text="SALIR", command=self.CerrarConexionMYSQL, bg="#FEF5E7", fg="#000000")
        self.btnsalir.place(x=5,y=275, width=80, height=30)

        # frame2 de txt
        frame2 = Frame(self,bg="#CAF3FC")
        frame2.place(x=95,y=0,width=150,height=300)

        #atributos
        #Id
        lblID = Label(frame2,text="ID: ",bg="#CAF3FC")
        lblID.place(x=3,y=5)
        self.txtID=Entry(frame2)
        self.txtID.place(x=3,y=25, width=60, height=20)

        #Nombre
        lblNombre = Label(frame2, text="Nombre", bg="#CAF3FC")
        lblNombre.place(x=3, y=55)
        self.txtNombre=Entry(frame2)
        self.txtNombre.place(x=3,y=75, width=120, height=20)

        #apellido
        lblApellido = Label(frame2,text="Apellido",  bg="#CAF3FC")
        lblApellido.place(x=3, y=105)
        self.txtApellido = Entry(frame2)
        self.txtApellido.place(x=3, y=125, width=120, height=20)

        #edad
        lblEdad = Label(frame2, text="Edad: ",  bg="#CAF3FC")
        lblEdad.place(x=3,y=155)
        self.txtEdad= Entry(frame2)
        self.txtEdad.place(x=3,y=175,width=120, height=20)

        #carrera
        lblCarrera = Label(frame2,text="Carrera: ", bg="#CAF3FC")
        lblCarrera.place(x=2,y=205)
        self.txtCarrera = Entry(frame2)
        self.txtCarrera.place(x=3,y=225, width=120,height=20)
         
        
        self.grid= ttk.Treeview(self,column=("col1","col2","col3","col4"))
        self.grid.column("#0",width=50)
        self.grid.column("col1",width=60,anchor=CENTER)
        self.grid.column("col2",width=90,anchor=CENTER)
        self.grid.column("col3",width=90,anchor=CENTER)
        self.grid.column("col4",width=90,anchor=CENTER)

        self.grid.heading("#0",text="ID", anchor=CENTER)
        self.grid.heading("col1",text="NOMBRE", anchor=CENTER)
        self.grid.heading("col2",text="APELLIDO", anchor=CENTER)
        self.grid.heading("col3",text="EDAD", anchor=CENTER)
        self.grid.heading("col4",text="CARRERA", anchor=CENTER)
        self.grid.place(x=247,y=0,width=420,height=290)
        


        












