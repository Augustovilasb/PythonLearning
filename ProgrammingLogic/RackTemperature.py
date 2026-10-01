
temps = [45, 52, 78, 60, 81, 49]
limit = 75

# 1
count = 0
for temp in temps:
    count += 1
    if  temp > 75:
        print("Server",count,"-","Temp:",temp," <- HOT")
    else:
        print("Server",count,"-","Temp:",temp,)
print(" ")

rack_ok = True
qnt_overheated = 0
for temp in temps:
    if temp > limit:
        rack_ok = False
        qnt_overheated += 1
if  rack_ok:
    print("Everything is ok!")
else:
    print("Rack status: OVERHEATED!")
    print(qnt_overheated,"servers are overheated!")
print("")

servers_overheated = 0
for temp in temps:
    servers_overheated += 1
    if temp > limit:
        print("Server:",servers_overheated,"- Temp:",temp)
print("")

high_temp = 0
each_server = 0
server_higher = 0
for temp in temps:
    each_server += 1
    if temp > high_temp:
        server_higher = each_server
        high_temp = temp
print("The highest temp is:", high_temp,"from server:", server_higher)