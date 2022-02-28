name = 'Earth'
moons = 1

jupiter_name = 'Jupiter'
jupiter_moons = 79

planet = {
    'name': 'Earth',
    'moons': 1
}

print(planet.get('name'))
# Display Earth

# planet['name'] is identical to using planet.get('name')
print(planet['name'])

wibble = planet.get('wibble') # Return None
wibble = planet ['wibble'] # Throws KeyError

planet.update({'name': 'Makemake'})
# name is now set to Makemake

planet ['name'] = 'Makemake1'

# Using update
planet.update({
    'name': 'Jupiter',
    'moons': 79
})

planet['name'] = 'Jupiter'
planet['moons'] = 79


planet['orbital period'] = 4333

# planet dictionary now contains {
# name : 'jupiter'
# moons : 79
# orbital period : 4333
# }
planet.pop('orbital period')

# Add addres
planet['diameter (km)'] = {
    'polar' : 133709,
    'equatorial': 142984
}

print(f'{planet["name"]} polar diameter : {planet ["diameter (km)"] ["polar"]}')

rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')


if 'december' in rainfall:
    rainfall['december']= rainfall['december']+1
else:
    rainfall['december'] = 1
# Because december exist, the value will be 3.1

total_rainfall = 0
for value in rainfall.values():
    total_rainfall=total_rainfall + value
print(f'There was {total_rainfall}cm in the last quarter')

