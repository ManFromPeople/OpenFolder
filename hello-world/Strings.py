fact = "The Moon has no atmosphere."
two_facts = fact + "No sound can be heard on the Moon."
print(two_facts)

multiline = "Facts about the Moon: \nThere is no atmosphere. \nThere is no sound."
print(multiline)

multiline = """Facts about the Moon:
There is no atmosphere.
There is no sound."""
print(multiline)

"temperatures and facts about the moon".title()

heading = "temperatures and facts about the moon"
heading.title()

temperatures = """Daylight: 260 F
Nighttime: -280 F"""
temperatures.split()

temperatures.split('\n')

"Moon" in "This text will describe facts and challenges with space travel"
"Moon" in "This text will describe facts about the Moon"

temperatures = """Saturn has a daytime of -170 degrees Celsius,
while Mars has -28 Celsius."""
#temperatures.find("Mars")
#temperatures.count("Mars")
temperatures.count("Moon")

"The Moon And The Earth".lower()
"The Moon And The Earth".upper()


temperatures = "Mars Average Temperature: -60 C"
parts = temperatures.split(':')
parts
parts[-1]

mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)
    elif "30 C".endswith("C"):
        print("This temperature is in Celsius")

"Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C")

text = "Temperatures on the Moon can vary wildly."
"temperatures" in text
"temperatures" in text.lower()

moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year"]
'\n'.join(moon_facts)
'+'.join(moon_facts)

text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several 
interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not 
significant enough to cause immediate effects on Earth. The highest daylight temperature of 
the Moon is 127 C."""

text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""
sentences = text.split('. ')
print(sentences)


mass_percentage = "1/6"
print ("On the Moon, you would weight about %s of your weight on Earth" % mass_percentage)

print ("""Both sides of the %s get the same amount sunlight,
but only one side is seen from %s because
the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))

mass_percentage = "1/6"
print("On the Moon, you would weigh about {} of your weight on Earth".format(mass_percentage))
print("""You are lighter on the {0}, because on the {0} 
you would weigh about {1} of your weigh on Earth.""".format("Moon", mass_percentage))
print("""You are lighter on the {moon}, because on the {moon}
you would weigh about {mass} of your weight on Earth""".format(moon="Moon", mass=mass_percentage))
print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth ")

round(100/6, 1)

print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth")

subject = "interesting facts about the moon"
f"{subject.title()}"

name = "Ganymede"
planet = "Mars"
gravity = "1.43"

template = """Gravity Facts about {name}
-----------------------------------
Planet Name: {planet}
Gravity on {name}: {gravity} m/s2"""

print(template.format(name=name, planet=planet, gravity=gravity))