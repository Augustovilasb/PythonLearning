value = float(input("Please, enter the value of the purchase: "))

TENDER_MINIMUM = 15000
QUOTES_MINIMUM = 500

if value < QUOTES_MINIMUM:
    print("You can order right now!")
elif value > TENDER_MINIMUM:
    print("The purchase must go to tender.")
else:
    print("We need to get a quote from three different suppliers first.")
