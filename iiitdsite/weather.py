import requests

api_key = "57e74c118984b8e89d7396384dcb4324"

base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = 'Dharwad'
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)

x = response.json()

if x["cod"] != "404":
    y = x["main"]
    temp_cel = int(y["temp"] - 273)
    temp_fah = int((temp_cel * 1.8) + 32)
