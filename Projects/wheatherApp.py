import urllib.parse
import urllib.request
import json

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  
    }

    try:
        url = base_url + '?' + urllib.parse.urlencode(params)
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode('utf-8'))

            temperature_celsius = data["main"]["temp"]
            description = data["weather"][0]["description"]
            
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            country = data["sys"]["country"]

            print("----------------Weather Information---------------\n")
            print(f"City: {city}\n")
            print(f"Temperature: {temperature_celsius:.2f}°C\n")
            print(f"Weather: {description}\n")
            print(f"Humidity: {humidity}%\n")
            print(f"Wind Speed: {wind_speed} m/s\n")
            print(f"Country: {country}\n")


    except urllib.error.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except urllib.error.URLError as erru:
        print(f"URL Error: {erru}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    city_name = input("Enter city name : ")
    print("\nSearching",city_name,".........")
    api_key = "729eb44316c3d092097c247bc74c15f6" 
    get_weather(city_name, api_key)


