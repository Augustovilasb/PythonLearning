email = input("Please, input email: ")

email_at = email.count("@") == 1
email_dot =  "." in email
email_len = len(email)

if email_at and email_dot and email_len >= 6:
    email_index_at = email.index("@")
    email_index_dot = email.index(".")

    if email_index_at < email_index_dot:
        print("Valid email!")
    else:
        print("Invalid email!")

else:
    print("Invalid email!")
