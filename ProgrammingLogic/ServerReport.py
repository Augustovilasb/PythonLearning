hostname = input("Enter the hostname:")
ram_total = int(input("Enter the RAM total:"))
ram_used = int(input("Enter the RAM used:"))

print(f"The server has the hostname: {hostname} and has total of {ram_total} GB and is currently using: {ram_used} GB")
print(f"RAM free: {ram_total - ram_used}")