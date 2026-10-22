from datetime import date

car_year = int(input("Enter the car year: "))
type_car = input("The car is Diesel or Petrol? (D/P)").lower()
limit_age = 10

year = date.today().year
car_age = year - car_year
print(f"The car age is: {car_age}")
print("")

if car_age >= limit_age or type_car == "p":
    print("High Pollution!!!")
else:
    print("Low Pollution!!!")
