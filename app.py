from flask import Flask, render_template, request, session, redirect
from flask_session import Session
from Modulos.helpers import login_required
from Modulos.Usuarios import *
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
@login_required
def index():
    return render_template('Principal.html')

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        email = request.form.get("inputEmail")
        password = request.form.get("inputPassword")
        if buscarUsuario(email,password):
            session["user_id"] = email
        return redirect('/')
    
@app.route('/logout')
@login_required
def logout():
    session.clear()
    return redirect('/login') 

@app.route('/register',methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template('register.html')
    elif request.method == "POST":
        Usuario = request.form.get("User")
        Contraseña = request.form.get("Pass")
        Contra2 = request.form.get("Pass1")
        if Contraseña != Contra2:
            return redirect('/register')
        insertarUsuario(Usuario,Contraseña)
        return redirect('/')