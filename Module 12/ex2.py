import requests
try:
    place = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={input("Enter municipality name: ")},FI&appid=3e6db4be391a310c688d92eea4eb8b3f')
    if place.status_code == 200:
        place = place.json()
        place = place[0]
        weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={place["lat"]}&lon={place["lon"]}&exclude=current,minutely,hourly&appid=3e6db4be391a310c688d92eea4eb8b3f').json()
        print(f'Weather: {weather["weather"][0]["description"]}')
        print(f'Temperature: {weather["main"]["temp"]-272.15:.1f} Celsius')
except requests.exceptions.RequestsException as e:
    print("Oops")