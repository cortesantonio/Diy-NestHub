from os import system
import sys
from webbrowser import Elinks
from flask import *
from magichome import *
from datetime import datetime



app = Flask(__name__)
app.secret_key = "s5HKwm5AtlmzLiU0FIrrMsWXsrTdoxco"


@app.route('/', methods=['GET','POST'])
def home():
    if request.method=='GET':
        date = datetime.now()
        x = int(date.time().strftime("%H"))
        if x >= 19 :
            estadodia = 'Buenas Noches'
        elif x <19 and x>=12:
            estadodia ='Buenas Tardes'
        elif x >=6 and x<12:
            estadodia ='Buenos Dias'
        elif x >=0 and x<=5:
            estadodia = 'Buenas Noches'

        

        data = {
            'saludo' : estadodia,
            'dia':datetime.today().strftime('%A, %B %d')
        }
        return render_template('index.html' ,data=data)

@app.route('/offall')
def ofall():
    system('wizcon 192.168.1.97 OFF')
    espejo = MagicHomeApi('192.168.1.81', 3)
    espejo.turn_off()
    offEscritorio()
    offLED()
    return redirect('/#space')

@app.route('/onall')
def onall():
    system('wizcon 192.168.1.97 ON')
    espejo = MagicHomeApi('192.168.1.81', 3)
    espejo.turn_on()
    onEscritorio()
    onLED()
    return redirect('/#space')

@app.route('/switchWiz')
def switchWiz():
    system('wizcon 192.168.1.97 SWITCH')
    return redirect('/#space2')
@app.route('/wizon')
def wizon():
    system('wizcon 192.168.1.97 ON')
    return redirect('/#space2')
@app.route('/wizoff')
def wizoff():
    system('wizcon 192.168.1.97 OFF')
    return redirect('/#space2')

@app.route('/switchSonoff')
def switchSonoff():
    system('wizcon 192.168.1.97 SWITCH')
    return redirect('/#space2')

@app.route('/switchEspejo')
def switchEspejo():
    espejo = MagicHomeApi('192.168.1.81', 3)
    estado = len(espejo.get_status())
    if estado>7:
        espejo.turn_on()
        espejo.turn_off()
        estado = len(espejo.get_status())
   
    return redirect('/#space2')


@app.route('/onespejo')
def onespejo():
    espejo = MagicHomeApi('192.168.1.81', 3)
    espejo.turn_on()
    return redirect('/#space2')

@app.route('/offespejo')
def offespejo():
    espejo = MagicHomeApi('192.168.1.81', 3)
    espejo.turn_off()
    return redirect('/#space2')
@app.route('/offEscritorio')
def offEscritorio():
    esc = MagicHomeApi('192.168.1.94', 3)
    esc.turn_off()
    return redirect('/#space2')

@app.route('/onEscritorio')
def onEscritorio():
    esc = MagicHomeApi('192.168.1.94', 3)
    esc.turn_on()

    return redirect('/#space2')

@app.route('/offLED')
def offLED():
    esc = MagicHomeApi('192.168.1.88', 3)
    esc.turn_off()
    return redirect('/#space2')

@app.route('/onLED')
def onLED():
    esc = MagicHomeApi('192.168.1.88', 3)
    esc.turn_on()

    return redirect('/#space2')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3000,debug=True)