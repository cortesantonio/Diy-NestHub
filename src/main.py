from os import system
import sys
from webbrowser import Elinks
from flask import *
from magichome import *
from datetime import datetime



app = Flask(__name__)
app.secret_key = "s5HKwm5AtlmzLiU0FIrrMsWXsrTdoxco"

@app.route('/')
def home():
    date = datetime.now()
    x = int(date.time().strftime("%H"))
    if x > 19:
        estadodia = 'Buenas Noches'
    elif x <=19 and x>=12:
        estadodia ='Buenas Tardes'
    elif x >=0 and x<12:
       estadodia ='Buenos Dias'

    data = {
        'saludo' : estadodia
    }
    return render_template('index.html' ,data=data)
@app.route('/devices')
def devices():
    return render_template('home.html')

@app.route('/tiempo')
def tiempo():
    return render_template('tiempo.html')
@app.route('/news')
def news():
    return render_template('news.html')
@app.route('/switchWiz')
def switchWiz():
    system('wizcon 192.168.1.97 SWITCH')
    return redirect('/devices')

@app.route('/switchSonoff')
def switchSonoff():
    system('wizcon 192.168.1.97 SWITCH')
    return redirect('/devices')

@app.route('/switchEspejo')
def switchEspejo():
    espejo = MagicHomeApi('192.168.1.81', 3)
    estado = len(espejo.get_status())
    if estado>7:
        espejo.turn_on()
        espejo.turn_off()
        estado = len(espejo.get_status())
   
    return redirect('/devices')

@app.route('/offEscritorio')
def offEscritorio():
    esc = MagicHomeApi('192.168.1.94', 3)
    esc.turn_off()
    return redirect('/devices')

@app.route('/onEscritorio')
def onEscritorio():
    esc = MagicHomeApi('192.168.1.94', 3)
    esc.turn_on()

    return redirect('/devices')

@app.route('/offLED')
def offLED():
    esc = MagicHomeApi('192.168.1.88', 3)
    esc.turn_off()
    return redirect('/devices')

@app.route('/onLED')
def onLED():
    esc = MagicHomeApi('192.168.1.88', 3)
    esc.turn_on()

    return redirect('/devices')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3000,debug=True)