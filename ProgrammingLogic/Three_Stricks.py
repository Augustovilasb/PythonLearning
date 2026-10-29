first_sticker = int(input("Input the first number: "))
second_sticker = int(input("Input the second number: "))
third_sticker = int(input("Input the third number: "))

if first_sticker > second_sticker and first_sticker > third_sticker:
    if (second_sticker ** 2) + (third_sticker ** 2) == (first_sticker ** 2):
        print("U can do it with those stickers.")
    else:
        print("U cant do it with those stickers.")
elif second_sticker > first_sticker and second_sticker > third_sticker:
    if (first_sticker ** 2) + (third_sticker ** 2) == (second_sticker ** 2):
        print("U can do it with those stickers.")
    else:
        print("U cant do it with those stickers.")
else:
    if (first_sticker ** 2) + (second_sticker ** 2) == (third_sticker ** 2):
        print("U can do it with those stickers.")
    else:
        print("U cant do it with those stickers.")

