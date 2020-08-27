from flask import Flask, render_template, request
import requests
import datetime

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    r=""
    if request.method == "POST":
        city = request.form['city']
        countrycode = request.form['countrycode']
        unit = request.form['unit']
        url = requests.get(
            'https://api.openweathermap.org/data/2.5/weather?q={},{}&appid=1963eb78cc0e9f89a4d066862d8ec90b&units=metric'.format(city,countrycode))

        weather_data = url.json()
        day=datetime.datetime.now()
        if (unit == 'celcius'):
            temp = round(weather_data['main']['temp'])
            r = str(temp)+" "+"C"
        elif(unit == 'ferhenheit'):
            temp = round((round(weather_data['main']['temp']))*(9/5))+32
            r= str(temp)+" "+"F"
        
        humidity = weather_data['main']['humidity']
        pressure = weather_data['main']['pressure']
        cloudiness = weather_data['clouds']['all']
        wind_speed = round((weather_data['wind']['speed'])*3.6)
        icon = weather_data['weather'][0]['icon']
        description = weather_data['weather'][0]['description']

        return render_template("result.html",temp=r,day=day.strftime("%A"),humidity=humidity,cloudiness=cloudiness,pressure=pressure,wind_speed=wind_speed, city=city, icon=icon, description=description,countrycode=countrycode)

    return render_template("home.html")


    

app.run(debug=True,port=5054)