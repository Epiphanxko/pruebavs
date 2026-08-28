from flask import Flask, render_template, url_for

#variables globales
app= Flask(__name__) #Creación del entorno Flask

#rutas
@app.route("/") #La ruta raíz del servidor
def index(): #inicia la función
    return(render_template('index.html')) #y toma una plantilla de la carpeta templates para renderizarla

#Esto se ecribe con el snippet froute
@app.route('/formulario', methods = ['GET', 'POST']) #este es un cambio en la URL y methods es una foma en que transmite los datos de form
def registro():
    return render_template('formulario.html')

@app.route('/login', methods =['GET', 'POST'])
def login(): #hay que quitar el foo de aqui pq si no no jala :)
    return render_template('login.html')


if "_main" == __name__: #Cuando se ejecute el servidor,
    app.run(host="0.0.0.0", port=8088, debug=True) #que lo haga por el puerto 8088, con la ip que se tenga en ese momento en modo depuración

#En consola se debe usar el comando flask --app server run --debug (dbug crea el modo depurador para guardar los cambios en tiempo real)