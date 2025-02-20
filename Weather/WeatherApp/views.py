from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    data = {}
    if request.method == 'POST':
        city = request.POST.get('city', '').strip()
        if city:
            api_key = 'cf9e408ae1ce2326a2ecb342f0a9bd6c'
            api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
            try:
                res = urllib.request.urlopen(api_url).read()
                json_data = json.loads(res)

                data = {
                    'city': f"{json_data['name']}, {json_data['sys']['country']}",  # City and Country Code
                    'temperature': json_data['main']['temp'],  # Temperature in Celsius
                    'humidity': json_data['main']['humidity'],  # Humidity Percentage
                    'pressure': json_data['main']['pressure'],  # Atmospheric Pressure
                    'latitude': json_data['coord']['lat'],  # Latitude
                    'longitude': json_data['coord']['lon'],  # Longitude
                    'description': json_data['weather'][0]['description'],  # Weather Description
                    'icon': f"http://openweathermap.org/img/w/{json_data['weather'][0]['icon']}.png"  # Weather Icon
                }
            except:
                data['error'] = "City not found. Please enter a valid city name."

    return render(request, "index.html", data)
