import requests
from geopy.geocoders import Nominatim

def location_from_coordinates(latitude, longitude):
    try:
        geolocator = Nominatim(user_agent="S*5")
        location = geolocator.reverse((latitude, longitude))
        return location.address
    except Exception as e:
        print(f"Error finding location: {e}")
        return None

def main():
    api_key = "f5eb6ceafc4d463eebb5bf57ed6af96a"
    input_type = input("Do you want to enter a city name or coordinates (type 'city' or 'coordinates')? ").strip().lower()

    if input_type == 'city':
        location = input("Enter the city name: ").strip().title()
        link = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    elif input_type == 'coordinates':
        latitude = input("Enter the latitude: ").strip()
        longitude = input("Enter the longitude: ").strip()
        location = location_from_coordinates(latitude, longitude)
        if not location:
            return
        print(f"The current location of this coordinate is: {location}")
        link = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"
    else:
        print("Invalid input. Please type 'city' or 'coordinates'.")
        return

    weather_response = requests.get(link)
    weather_data = weather_response.json()

    if weather_data['cod'] == "404":
        print(f"Invalid location: {location}")
    else:
        temp_city = weather_data['main']['temp'] - 273.15
        climate = weather_data['weather'][0]['main']
        print(f"Temperature in location: {temp_city:.2f}°C")
        print(f"Climate in location: {climate}")

        more_info = input("For more information please type 'more', otherwise press any other key: ").strip().lower()
        if more_info == 'more':
            wind_speed = weather_data['wind']['speed']
            humidity = weather_data['main']['humidity']
            max_temperature = weather_data['main']['temp_max'] - 273.15
            min_temperature = weather_data['main']['temp_min'] - 273.15
            print(f"Wind Speed in location: {wind_speed} m/s")
            print(f"Humidity in location: {humidity}%")
            print(f"Maximum temperature in location: {max_temperature:.2f}°C")
            print(f"Minimum temperature in location: {min_temperature:.2f}°C")

        print("Thank you for using our project!")


try:
  main()

except Exception as e:
  print(f"Something went wrong, please try again later.{e}")

input()
