import requests, json
try:
    joke = requests.get("https://api.chucknorris.io/jokes/random")
    if joke.status_code == 200:
        joke = joke.json()
        print(joke["value"])
except requests.exceptions.RequestException as e:
    print("That didn't work.")