#clase que me permite realizar la encriptacion de datos con AES
"""
AES (Advanced Encryption Standard) es un algoritmo de cifrado simétrico utilizado para
proteger la confidencialidad de los datos. En un cifrado simétrico, tanto la clave de
encriptación como la clave de desencriptación son la misma, lo que significa que la
seguridad depende de la protección de esa clave.
"""
#librerias a utilizar
from cryptography.fernet import Fernet
import os

#clase
class Seguridad:

    #constructos metodo que se declara una  vez
    def __init__(self):
        # Ruta donde guardar la clave de cifrado
        self.ruta_clave = 'clave_cifrado.key'

        # Si la clave ya existe, la cargamos
        if os.path.exists(self.ruta_clave):
            with open(self.ruta_clave, 'rb') as archivo:
                self.clave = archivo.read()
        else:
            # Si no existe la clave, la generamos
            self.clave = Fernet.generate_key()
            # Guardamos la clave en un archivo
            with open(self.ruta_clave, 'wb') as archivo:
                archivo.write(self.clave)

        # Creamos el objeto Fernet con la clave
        self.cipher = Fernet(self.clave)

    #metodo que me permite cifrar datos
    def cifrar_datos(self, datos):
        """
        Cifra los datos.
        """
        # Convertir los datos a bytes y cifrarlos
        datos_bytes = datos.encode('utf-8')
        datos_cifrados = self.cipher.encrypt(datos_bytes)
        return datos_cifrados

    #metodo que me permite desifras datos
    def descifrar_datos(self, datos_cifrados):
        """
        Descifra los datos cifrados.
        """
        try:
            # Descifrar los datos
            datos_descifrados = self.cipher.decrypt(datos_cifrados)
            return datos_descifrados.decode('utf-8')
        except Exception as e:
            print(f"Error al descifrar los datos: {e}")
            return None
