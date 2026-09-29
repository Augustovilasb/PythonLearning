import time

start = time.time()

secret = 98776
tries = 0

for guess in range(100000):
    tries += 1
    print(tries)
    if guess == secret:
        print("Found it:", guess)
        break

end = time.time()
print("Time:", end - start, "seconds")