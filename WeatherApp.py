import requests

API_KEY = "3211f674cc9805f7cef269544c5c31be"  # 🔑 Replace with your actual API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    # Create request URL
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            main = data["main"]
            weather = data["weather"][0]
            
            temperature = main["temp"]
            humidity = main["humidity"]
            description = weather["description"]

            print(f"\n Weather in {city.title()}:")
            print(f" Temperature: {temperature}°C")
            print(f" Humidity: {humidity}%")
            print(f" Description: {description.title()}\n")
        else:
            print("\n City not found. Please enter a valid city name.\n")
    except Exception as e:
        print(5*"*","Error:",5*"*", e)
if __name__ == "__main__":
    print("*" * 10, "Weather App", "*" * 10)
    city_name = input("Enter city name: ")
    get_weather(city_name)
