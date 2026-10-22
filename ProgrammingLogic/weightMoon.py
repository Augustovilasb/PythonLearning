## The weight of something on the moon is 16.5% of what it is on Earth, create a
#   variable of the weight of someone on Earth and display their weight on the Moon
#
## Data requirements:
#   Problem Input: "my_weight_on_earth" (weight on Earth in Kg)
#   Problem Output: "my_weight_on_moon" (weight on the Moon in Kg)
#   Formula: Weight on Moon = Weight on Earth * 0.165
#
## Algorithm:
#   1. Assign the weight on Earth
#   2. Calculate the weight on the Moon
#   3. Display the weight on the Moon

# Assign the weight on Earth
my_weight_on_earth = 80
print("")

# Weight on the Moon (16.5% of the weight on Earth)
my_weight_on_moon = my_weight_on_earth * 0.165

# Display the result
print("1) My weight on Earth is:", my_weight_on_earth, "Kg.")
print("2) My weight on the Moon would be:", round(my_weight_on_moon, 2), "Kg.")