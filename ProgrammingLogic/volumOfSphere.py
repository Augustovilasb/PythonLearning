## Design and write a program that assigns a value to the
#   radius of a sphere to calculate the volume.
#
## Create a variable called, “total liquid” (try and make sure it's large,
#   that is much greater than the volume of the sphere).
#  Work out how many spheres of liquid would be needed to
#   hold all the water of “total liquid” (ignore remainders).
#
## Data requirements:
#   Problem Input: "radius", "total_liquid"
#   Problem Output: "volume_Sphere", "spheres_Necessary"
#   Formula: Volume = 4/3 * PI * (Radius ** 3)
#
## Algorithm:
#   1. Assign the radius, pi and the total liquid
#   2. Calculate the volume of the sphere
#   3. Calculate the number of spheres needed ignoring remainders
#   4. Display the volume and the number of spheres

# Assign the variables
total_liquid = 1000000
pi = 3.14
radius = 5
print("")

# Volume of the sphere
volume_Sphere = 4/3 * pi * (radius ** 3)
print("1) The volume of the sphere is:", round(volume_Sphere,2))

# Number of the sphere needed
# I am using the operator '//' to ignore the remainder
spheres_Necessary = int(total_liquid // volume_Sphere)
print("2) The total liquid is:", total_liquid)
print("3)", spheres_Necessary, "spheres are needed to hold all of the water")