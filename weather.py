import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=9.03&longitude=38.74&current_weather=true"
response = requests.get(url)
data = response.json()

temperature = data["current_weather"]["tempertaure"]# your turn
windspeed = data["currrent_weather"]["windspeed"]

print(f"Temperature: {temperature}°C")
print(f"Windspeed: {windspeed} km/h")