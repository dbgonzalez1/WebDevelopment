#Importar las liberias 
from markupsafe import escape
from flask import Flask, render_template
import pandas as pd
#Instanciar
app = Flask(__name__)
#Crear la base de datos
df = pd.DataFrame()
#Primer Controlador -> Mostrará la lista actual de tareas pendientes
@app.route('/')
def principal():
    return render_template('index.html')

#Segundo Controlador -> Aceptar datos del formulario
@app.route('/enviar')
def enviar():
     return render_template('enviar.html')

#Tercer Controlador -> Borrar la lista de tareas pendientes
@app.route('/borrar')
def borrar():
     return render_template('borrar.html')

#Main
if __name__ == '__main__':
    #debug = true para reinicializar automticamente
    app.run(debug=True)