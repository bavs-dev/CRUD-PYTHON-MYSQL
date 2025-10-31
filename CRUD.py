#clase que me permite realizar la creacion de mi  consultas la relizacion de mi conexion
#como utulizamos mysql se utiliza pymysql
import logging

import pymysql
import tkinter.messagebox

#generamos la clese crud que es CREAD READ UPDATE DELETE CRUD
class CRUD:

    #mconstructor que indica que al inciar el programa se genere la conexion a la bd
    def __init__(self):
        # metodo para consultar un dato por id
        # conexion
        self.Conexion()
        pass

    # metodo para la Conexion de Base de Datos
    def Conexion(self):
        try:
            # conexion
            self.connection = pymysql.connect(
                host='localhost',  # colocamos ip si trabamos con servidores de lo contrario localhost
                user='root', # usuario con la que accedera a la base  de datos
                password='admin', # contraseña par acceder ala base  de datos
                db='CRUDPY' # nombre de la base  de datos
            )
            #el cursos nor permite tener nuestro enlace en la conexion asi mismo le indico que la genere
            self.cursor = self.connection.cursor()
            print("Se Conecto con MYSQL")

        except Exception as e:
            logging.error("Error en la conexion ",e)
            raise

    def Selection(self, ID):
        sql = 'SELECT ID,NOMBRE,APELLIDO,EDAD,CARRERA FROM usuarios WHERE ID ={}'.format(ID)
        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()

            # visualizar
            print("Id: ", user[0])
            print("Nombre: ", user[1])
            print("Apellido: ", user[2])
            print("Edad: ", user[3])
            print("Carrera: ", user[4])

        except Exception as e:
            raise

    # ejemplo
    def consulta_user(self, ID):
        sql = 'SELECT * FROM usuarios WHERE ID={}'.format(ID)
        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()
            return user
        except Exception as e:
            tkinter.messagebox.showinfo("crud", "no se encontro")
            return e

    def consulta_usarios(self):
        sql = 'SELECT * FROM usuarios'
        self.cursor.execute(sql)
        datos = self.cursor.fetchall()
        return datos

        # visualizar todo

    def selectionshow(self):
        sql = 'SELECT ID, NOMBRE,APELLIDO,EDAD,CARRERA FROM usuarios'
        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchall()
            for user in user:
                print("Id: ", user[0], "->  Nombre: ", user[1], " -> Apellido: ", user[2], " -> Edad: ", user[3],
                      " -> Carrera: ", user[4])
                print("____________________________________________\n")
        except Exception as e:
            raise

    # insert
    def insertar(self, NOMBRE, APELLIDO, EDAD, CARRERA):
        sql = f"INSERT INTO usuarios(NOMBRE,APELLIDO,EDAD,CARRERA) VALUES ('{NOMBRE}','{APELLIDO}',{EDAD},'{CARRERA}')"
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise

    def insertars(self, nombre, apellido, edad, carrera):
        sql = "INSERT INTO usuarios (NOMBRE, APELLIDO, EDAD, CARRERA) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(sql, (nombre, apellido, edad, carrera))
        self.connection.commit()

    # update
    def updatesql(self, NOMBRE, APELLIDO, EDAD, CARRERA, ID):
        sql = f"UPDATE usuarios SET NOMBRE='{NOMBRE}', APELLIDO='{APELLIDO}', EDAD = '{EDAD}', CARRERA = '{CARRERA}' WHERE ID={ID}"
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise

    def updatesqls(self, nombre, apellido, edad, carrera, id_usuario):
        sql = "UPDATE usuarios SET NOMBRE=%s, APELLIDO=%s, EDAD=%s, CARRERA=%s WHERE ID=%s"
        self.cursor.execute(sql, (nombre, apellido, edad, carrera, id_usuario))
        self.connection.commit()

    def deletesql(self, ID):
        sql = f"DELETE FROM usuarios WHERE ID={ID}"
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise

    def CerrarConexion(self):
        self.cursor.close()
        tkinter.messagebox.showinfo("CRUD", "Se Cerro la Conexion Con mysql")
        pass

