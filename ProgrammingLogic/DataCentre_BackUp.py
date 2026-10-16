one_tape = 800 # 1 GB
copy_speed = 3 # 3 GB/min
tape_price = 24.60 # Euros
VAT = 1.23 # 23%
time_changing = 10 # Minutos

gb = int(input("How many GB? "))
start_hr = int(input("Input the start time: "))
start_min = int(input("Input the start time: "))

# how many tapes necessary
tapes_necessary = ((gb + 799) // one_tape)
print("Quantity of tapes necessary is:", tapes_necessary)

# time necessary to change the tapes in minutes
time_changing_tapes = ((tapes_necessary - 1) * time_changing)
print("The time necessary to change all of them is:", time_changing_tapes, "minutes")

copy_time = ((gb + 2) // copy_speed)
print("The time necessary only to copy all the files is:", round(copy_time, 2))

total_duration = copy_time + time_changing_tapes
print("The time necessary to complete the whole process is:", round(total_duration, 2))
duration_hour = total_duration // 60
duration_min = total_duration % 60
print(f"We expect the process duration: {duration_hour:02}:{duration_min:02}")

time_starting = ((start_hr * 60) + start_min)
time_finishing = time_starting + total_duration
time_hr_finishing = (time_finishing // 60) % 24
time_min_finishing = time_finishing % 60
print(f"We expect finish at {time_hr_finishing:02}:{time_min_finishing:02}")

tape_without_vat = tape_price / VAT
print(f"Price of each tape without VAT: {tape_without_vat:.2f} Euros")

total_price = tape_price * tapes_necessary
print(f"This is the final price with 23% VAT: {total_price:.2f} Euros")
total_price_without_VAT = (tape_price * tapes_necessary) / VAT
print(f"This is the final price without 23% VAT: {total_price_without_VAT:.2f} Euros")
