from flask import Flask, render_template, request
import requests
import config

app = Flask(__name__)

def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={config.API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data.get('cod') != 200:
        return None  # If there's an error (e.g., city not found)

    weather = {
        'location': data['name'],
        'description': data['weather'][0]['main'],
        'temp': round(data['main']['temp'] - 273.15, 2),  # Convert from Kelvin to Celsius
        'feels_like': round(data['main']['feels_like'] - 273.15, 2),
        'max_temp': round(data['main']['temp_max'] - 273.15, 2),
        'min_temp': round(data['main']['temp_min'] - 273.15, 2),
    }

    return weather

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            weather = get_weather_data(city)
            if weather:
                return render_template('index.html', **weather)
            else:
                return render_template('index.html', location=None)  # No weather data found
    else:
        city = "Delhi"  # Default city
        weather = get_weather_data(city)
        return render_template('index.html', **weather)

if __name__ == "__main__":
    app.run(debug=True)
