from os import system
import sys
from flask import *
from magichome import *
from datetime import datetime



app = Flask(__name__)
app.secret_key = "s5HKwm5AtlmzLiU0FIrrMsWXsrTdoxco"


@app.route('/', methods=['GET','POST'])
def home():
    data = {
            
            'dia':datetime.today().strftime('%A, %B %d')
    }
    return render_template('index.html' ,data=data)


@app.route('/switchWiz')
def switchWiz():
    system('wizcon 192.168.1.82 SWITCH')
    return redirect('/')

@app.route('/onespejo')
def onespejo():
    espejo = MagicHomeApi('192.168.1.104', 3)
    espejo.turn_on()
    return redirect('/')

@app.route('/offespejo')
def offespejo():
    espejo = MagicHomeApi('192.168.1.104', 3)
    espejo.turn_off()
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3000,debug=True)