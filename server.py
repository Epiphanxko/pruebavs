from flask import Flask, render_template, url_for, request,flash, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, PasswordField, SubmitField,BooleanField
from wtforms.validators import Email, Length, EqualTo, DataRequired,InputRequired

from werkzeug.security import generate_password_hash, check_password_hash

from config_server import Config
from flask_mysqldb import MySQL


app= Flask(__name__) 

app.config.from_object(Config)

app.secret_key = "floreria123"


database = MySQL(app)





#rutas
@app.route("/") 
def index(): 
    flash ("Bienvenido","alerta")
    return(render_template("index.html")) 

class Registro(FlaskForm):
    rNombre = StringField("Nombre", validators=[Length(min=3, max=50, message="Ingresa un nombre valido")])
    rApellido = StringField("Apellidos",validators=[InputRequired(), Length(min=1,max=150)])
    rCorreo =StringField("Correo",validators = [InputRequired(),Email()])
    rPass = PasswordField("Contraseña", validators=(DataRequired(),Length(min=8,message="DEBE TENER AL MENOS 8 CARACTERES")))
    rsubmit = SubmitField("Registrarme")
    rConfirm = PasswordField("Confirmar contraseña", validators=[])
    rTYC= BooleanField ("Aceptar Terminas y COndiciones", validators=[DataRequired()])


@app.route('/formulario', methods = ['GET', 'POST'])
def registro():
    
    form = Registro ()

    if form.validate_on_submit():
       inNombre = form.rNombre.data
       inApellidos =form.rApellido.data
       inCorreo =form.rCorreo.data
       inPass=form.rPass.data
       inConfirm =form.rConfirm.data
       inTYC =form.rTYC.data
       
       values = f"Nombre: {inNombre} Apellidos: {inApellidos} Correo: {inCorreo} Contraseña:{inPass} Confirmar: {inConfirm} TyC: {inTYC}" 
       print(values)
       
       if inPass == inConfirm and inTYC != False:
            password_hasheada= generate_password_hash(inPass)

            sqlCrearUsuario = "INSERT INTO usuarios(id_usuario,name_user,email_user) VALUES (%s,%s,%s)"

            crearUsuario = database.connection.cursor()
            crearUsuario.execute(sqlCrearUsuario,(inNombre,inCorreo,password_hasheada))
            database.connection.commit() 
            crearUsuario.close()

            flash("Cuenta creada", "succes")

            return redirect("login")

    return render_template('formulario.html', form=form)

@app.route('/login', methods =['GET', 'POST'])
def login(): 
    msj= None

    if request.method == 'POST':
        lUser =request.form.get("lUser")
        lPass =request.form.get("lPass")

        msj = f"NOMBRE: {lUser},CONTRASEÑA: {"lPass"}"

        return render_template('login.html',msj =msj)

    return render_template('login.html',msj =msj)

@app.route('/perfil')
def perfil():
    consulta_perfil = database.connection.cursor()

    sqlConsulta = "SELECT * FROM usuarios"

    consulta_perfil.execute(sqlConsulta)
    
    datos = consulta_perfil.fetchall()

    usuarios =[]

    if datos:
        for campo in datos:
            usuarios.append({
                    "uid": campo[0],
                    "uname": campo[1],
                    "uemail": campo[2],
                    "upass": "CONTRASEÑA"
                })
            
    else:
        usuarios = None


    return render_template('perfil.html', usuarios=usuarios)

#CATALOGO

@app.route('/catalogo', methods=['POST'])
def catalogo():
    consulta_producto = database.connection.cursor()
    sqlCOnsulta = "SELECT pnombre, ppreciov,pcantidad,pcveFROM productos"
    consulta.producto.execute(sqlCOnsulta)
    res_consulta=consulta_producto.fetchall

    producto[]



    return render_template('catalogo.html')
    


if "__main__"== __name__: 
    app.run(host="0.0.0.0", port=8088, debug=True) 