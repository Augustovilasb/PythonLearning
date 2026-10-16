# spread the email by the @

email = input("Please enter the email: ")

split_point = email.index("@")
name = email[:split_point]
domain = email[split_point +1:]

uName = name
uDomain = domain
print(uName)
print(uDomain)