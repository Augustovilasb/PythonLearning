# hostname = DUB-RACK12-SRV07

print("1. Lowercase")
#hostname = input("Enter the hostname: ").lower()
hostname = "DUB-RACK12-SRV07".lower()
print("The hostname on lower case:",hostname)
print("")

print("2. Hostname length")
print("The hostname has", len(hostname),"caracteres.")
print("The first one is:", hostname[0])
print("The last one is:", hostname[-1])
print("")

print("3. Broking the hostname in parts")
print("The host name in parts:")
parts = hostname.split("-")
print("Those are the hostname parts:",parts)
print("And we have",len(parts),"parts")
print("")

print("4. Checking if the hostname has 3 parts")
if len(parts) != 3:
    print("Hostname invalid!")
    print("It must have 3 parts!")
else:
    print("The hostname has the 3 parts needed!")
    print("Valid hostname!")
print("")

print("5. Checking if all the parts on  the hostname are valid")
valid = True
for part in parts:
      if part == "":
          valid = False
          break
if valid:
    print("All the parts are filled!")
    print("Valid hostname!")
else:
    print("Invalid hostname!")
    print("The hostname can't have any empty part!")
print("")

print("6. Find the rack number, server number and the site:")
if len(parts) != 3:
    print("Invalid hostname!")
else:
    part0 = parts[0]
    part1 = parts[1]
    part2 = parts[2]
    print("Site:", part0.upper())
    print("Rack number:", int(part1[-2:]))
    print("Server number:", int(part2[-2:]))
print("")

print("7. Invert the hostname")
print("Standard hostname:", hostname)
inverted_hostname = ""
for letters in hostname:
    inverted_hostname = letters + inverted_hostname
print("Inverted hostname:",inverted_hostname)
print("")

print("8. Inverted hostname with out the '-'")
print(inverted_hostname)
print(inverted_hostname.replace("-",""))
print("")

print("9. How many vowels hostname has:")
count = 0
vowels = ""
for letters in hostname:
    if letters in {"a","e","i","o","u"}:
            count += 1
            vowels = vowels + letters
print("We have:",count,"in the hostname.")
print("Those are:",vowels)
print("")

print("10. Hostname statement:")
if len(parts) != 3:
    print("Invalid hostname!")
else:
    part0 = parts[0]
    part1 = parts[1]
    part2 = parts[2]
    print(f"Hostname: {hostname}\nLength: {len(hostname)}\nFirst: {hostname[0]} | Last: {hostname[-1]}\nSite: {part0.upper()}\nRack: {int(part1[-2:])}\nServer: {int(part2[-2:])}\nReversed: {inverted_hostname}\nCode: {inverted_hostname.replace("-","")}\nVowels: {count}")