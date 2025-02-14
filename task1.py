import datetime as dt
import requests

def kalvin_to_c_f(k):
    c = k - 273.15
    f = c * (9/5) + 32
    return c, f


base_url = "https://api.openweathermap.org/data/2.5/weather?"

api_key = open('apikey' , 'r').read()
city_name = input("Enter city name : ")

# https://api.openweathermap.org/data/2.5/weather?q=API
url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(url).json()

# print(response)

# Enter city name : surat
# {'coord': {'lon': 72.8333, 'lat': 21.1667}, 
# 'weather': [{'id': 711, 'main': 'Smoke', 'description': 'smoke', 'icon': '50n'}], 
# 'base': 'stations', 
# 'main': {'temp': 297.14, 'feels_like': 296.98, 'temp_min': 297.14, 'temp_max': 297.14, 
# 'pressure': 1012, 'humidity': 53, 'sea_level': 1012, 'grnd_level': 1011}, 'visibility': 5000,
# 'wind': {'speed': 2.57, 'deg': 360},
# 'clouds': {'all': 0}, 'dt': 1737558264, 'sys': {'type': 1, 'id': 9071, 'country': 'IN', 'sunrise': 1737510484, 'sunset': 1737550321}, 
# 'timezone': 19800, 'id': 1255364, 'name': 'Surat', 'cod': 200}

temp_kelvin = response['main']['temp']
temp_c , temp_f = kalvin_to_c_f(temp_kelvin)

feels_like_kalvin = response['main']['feels_like']
feels_like_c , feels_like_f = kalvin_to_c_f(feels_like_kalvin)

humidity = response['main']['humidity']
wind_speed = response['wind']['speed']
# sunrise_time = response['sys']['sunrise'] + response['timezone']
sunrise_time = dt.datetime.fromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.fromtimestamp(response['sys']['sunset'] + response['timezone'])


print(f"Temprature in {city_name} : {temp_c:.2f} 'C or {temp_f:.2f} F\n")
print(f"Temprature Feels like in {city_name} : {feels_like_c:.2f} 'C or {feels_like_f:.2f} F\n")
print(f"Humidity in {city_name} : {humidity} % \n")
print(f"wind_speed in {city_name} : {wind_speed} m/s\n")
print(f"sunrise_time in {city_name} at {sunrise_time} local time.\n")
print(f"sunset_time in {city_name} at {sunset_time} local time.\n")
