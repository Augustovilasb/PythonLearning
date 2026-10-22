# Calculate the Age in different planets

# The days per year in each planet
earthDays = 365
mercuryDays = 88
venusDays = 225
jupiterDays = 4380
saturnDays = 10767

ageOnEarth = int(input("What is your age: "))

ageOnMercury = int((ageOnEarth * earthDays) / mercuryDays)
print("Your age on Mercury is approximately: ",ageOnMercury)

ageOnVenus = int((ageOnEarth * earthDays) / venusDays)
print("Your age on Venus is approximately: ",ageOnVenus)

ageOnJupiter = int((ageOnEarth * earthDays) / jupiterDays)
print("Your age on Jupiter is approximately: ",ageOnJupiter)

ageOnSaturn = int((ageOnEarth * earthDays) / saturnDays)
print("Your age on Saturn is approximately: ",ageOnSaturn)