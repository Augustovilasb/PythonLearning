import math
from enum import Enum

class Option(Enum):
    AREA_OF_A_CIRCLE = 1
    VOLUME_OF_SPHERE = 2
    EXIT = 0

choose = None

while choose != Option.EXIT:

    print("------ MENU ======")
    print("1. Calculate the area of a circle.")
    print("2. Calculate the volume of a sphere.")
    print("0. Exit.")

    try:
        choose = Option(int(input("Please, enter a option (0,1 or 2): ")))
    except ValueError:
        print("Check the options again.")
        continue

    if choose == Option.AREA_OF_A_CIRCLE:
        radius_area = float(input("Please, enter a circle radius: "))
        area = round(math.pi * (radius_area ** 2), 4)
        print("The area of circle with radius", radius_area, "is: ", area)

    elif choose == Option.VOLUME_OF_SPHERE:
        radius_sphere = float(input("Please, enter the sphere radius: "))
        volume_sphere = round((4/3) * (math.pi * (radius_sphere ** 3)), 4)
        print("The volume of the sphere with radius", radius_sphere, "is: ", volume_sphere)

    elif choose == Option.EXIT:
        print("You are welcome!")