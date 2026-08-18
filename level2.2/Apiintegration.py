import requests

def get_weather(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    
    try:
        response = requests.get(url)
        data = response.json()
        temp = data["current_weather"]["temperature"]
        windspeed = data["current_weather"]["windspeed"]
        print(f"Temperature: {temp}°C")
        print(f"Wind speed: {windspeed} km/h")
    except Exception as e:
        print("Failed to fetch weather data:", e)

latitude = input("Enter latitude: ").strip()
longitude = input("Enter longitude: ").strip()
get_weather(latitude, longitude)