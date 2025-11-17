"""Problem 4: Weather Advisory System
Create a weather advisor that gives clothing
recommendations:
Input: Temperature (Celsius) and weather condition
Weather Conditions: "sunny", "rainy", "cloudy"
Logic:
Sunny + temp > 25°C: "Wear light clothes and
sunscreen"
Sunny + temp ≤ 25°C: "Wear comfortable clothes"
Rainy: "Take an umbrella and wear a jacket"
Cloudy + temp < 15°C: "Wear warm clothes"
Cloudy + temp ≥ 15°C: "Light jacket recommended"""

input_temperature = input("Enter a temperature")
temperature = float(input_temperature)

weather_con = input("Input Weather Condition")


if weather_con == "sunny" and temperature > 25:
    print("Wear light clothes and sunscreen")

elif weather_con == "sunny" and temperature <= 25:
    print("Wear light clothes and sunscreen")

elif weather_con == "rainy" :
    print("Take an umbrella and wear a jacket")

elif weather_con == "cloudy" and temperature < 15:
    print("Wear warm clothes")

elif weather_con == "cloudy" and temperature >= 15:
    print("Light jacket recommended")

else:
    print("Invalid input")