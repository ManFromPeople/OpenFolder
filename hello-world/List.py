planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print("The first planet is", planets[0])
print("The second planet is", planets[1])
print("The third planet is", planets[2])

planets[3] = "Red Planet"
print("Mars is also known as", planets[3])

number_of_planets = len(planets)
print("There are", number_of_planets, "planets in the solar system.")

planets.append("Pluto")
number_of_planets = len(planets)
print("There are actually", number_of_planets, "planets in the solar system.")

planets.pop() # Goodbye, Pluto
number_of_planets = len(planets)
print("No, there are definetely", number_of_planets, "planets in the solar system.")

print("The first planet is", planets[0])

print("The last planet is", planets[-1])
print("The penultimate planet is", planets[-2])

jupiter_index = planets.index("Jupiter")
print("Jupiter is the", jupiter_index + 1, "planet from the sun")

gravity_on_earth = 1.0
gravity_on_the_moon = 0.166

gravity_on_planets = [0.378, 0.907, 1, 0.379, 2.36, 0.916, 0.889, 1.12]

bus_weight = 12650 # in kilograms, on Earth
print("On Earth, a double-decker bus weighs", bus_weight, "kg")
print("On Mercury, a double-decker bus weighs", bus_weight*gravity_on_planets[0], "kg")

bus_weight = 12650 # in kilograms, on Earth
print("On Earth, a double-decker bus weighs", bus_weight, "kg")
print("The lightest a bus would be in the solar system is", bus_weight*min(gravity_on_planets), "kg")
print ("The heaviest a bus would be in the solar system is", bus_weight*max(gravity_on_planets), "kg")

planets_before_earth = planets[0:2]
print(planets_before_earth)

planets_after_earth = planets[3:8]
print(planets_after_earth)

amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moon = ["Io", "Europa", "Ganymede", "Calisto"]
regular_satellite_moons = amalthea_group + galilean_moon
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

regular_satellite_moons.sort()
print("The regular satelline moons of Jupiter are", regular_satellite_moons)

regular_satellite_moons.sort(reverse=True)
print("The regualar satellite moons of Jupiter are", regular_satellite_moons)

