## Write a program to convert 32 degrees Celsius to degrees Fahrenheit.
#
## Data Requirements:
#   Problem Input: "celsius_Temp" (temperature in Celsius degrees)
#   Problem Output: "fahrenheit_Temp" (temperature in degrees Fahrenheit)
#   Formula: Fahrenheit = Celsius * 9/5 + 32
#
## Algorithm:
#   1. Assign the degrees in Celsius
#   2. Apply the variable "celsius_Temp" in the conversion formula
#   3. Display the degrees in Fahrenheit

# variable temperature Celsius
celsius_Temp = 32

# Formula to convert temperatures
fahrenheit_Temp = (celsius_Temp * (9/5)) + 32
fahrenheit_Temp = round(fahrenheit_Temp,2)

# Output with temperature in Fahrenheit
print(celsius_Temp,"degrees Celsius is", fahrenheit_Temp,"degrees in Fahrenheit")