from weatherApi import WeatherApi

api_key = "77fd7a6fac4c4836bf6130530240505"
client = WeatherApi(api_key)

city = input("Enter the city name: ")

print(client.get_current_temperature(city))
print(client.get_temperature_after(city, 2, 10))
print(client.get_lat_and_long(city))