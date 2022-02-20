from flask import Flask, request, render_template
import requests
from FlaskWebProject1 import app

@app.route('/')
def index():
   return render_template('getname.html')

@app.route('/place', methods = ['POST','GET'])
def fetch_details():
    if request.method == 'POST':
        option = request.form['loc']
        api_key= 'efef2377e7fd98dda1b25ef1208128e5'
        url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(option,api_key)
        req = requests.get(url).json()    

        if req['cod']=='404':
            return render_template('PlaceNotFound.html')
        else:
            r={
                'location' : option.upper(),
                'cod' : req['cod'],
                'temperature' : req['main']['temp'],
                'humidity' : req['main']['humidity'],
                'icon' : req['weather'][0]['icon'],
                'windspeed' : req['wind']['speed']
            }        
        return render_template('putTemperature.html',temp_details=r)        

    

