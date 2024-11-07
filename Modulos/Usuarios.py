from Modulos.ConnectionString import Coneccion
import pyodbc
from werkzeug.security import check_password_hash, generate_password_hash
Con = Coneccion()

def insertarUsuario(Usuario,Contraseña):
    cursor = Con.cursor()
    ContraEncrypt = generate_password_hash(Contraseña)
    cursor.execute("INSERT INTO Usuarios(Username,Contraseña) VALUES(?,?)",Usuario,ContraEncrypt)
    cursor.commit()
    cursor.close()

def buscarUsuario(Usuario,contraseña):
    cursor = Con.cursor()
    cursor.execute("SELECT Contraseña FROM Usuarios WHERE Username = ?",Usuario)
    HashPass = cursor.fetchone()
    cursor.close()
    if check_password_hash(HashPass[0],contraseña):
        return True
    else:
        return False
