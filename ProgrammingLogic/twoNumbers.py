## Design and write a program that assigns two decimal numbers and then separately:
#
#   - sum
#   - difference
#   - product
#   - average
#   - the remainder after division and
#   - the first to the power of the second
#
## Data requirements:
#   Problem Input: "first_Number", "second_Number" (must be two decimal numbers)
#   Problem Output: "sum_Result", "difference_Result1", "difference_Result2", "product_Result",
#                   "avg_Result", "remainder_Result", "power_Result"
#
## Algorithm
#   1. Assign the two decimal numbers
#   2. Calculate the sum, difference, product, average, remainder and power
#   3. Display each result separately

# Assign two decimal numbers
first_Number = 7.5
second_Number = 2.0
print("")

# Sum of the 2 numbers
sum_Result = first_Number + second_Number
print("1) The sum of the 2 numbers is:", sum_Result)

# Difference of the 2 numbers
difference_Result1 = first_Number - second_Number
difference_Result2 = second_Number - first_Number
if first_Number > second_Number:
    print("2) The difference between first number on the second is:", difference_Result1)
else:
    print("2) The difference between second number on the first is:", difference_Result2)

# Product of the numbers
product_Result = first_Number * second_Number
print("3) The product of the 2 numbers is:", product_Result)

# Average of 2 numbers
avg_Result = sum_Result / 2
print("4) The average of the 2 numbers is:", avg_Result)

# Remainders after division
remainder_Result = first_Number % second_Number
print("5) The remainder after division between the 2 numbers is:", remainder_Result)

# First number to the power of the second number
power_Result = first_Number ** second_Number
print("6) The first number to the power of the second number is:", power_Result)