def rocket_parts():
    print("payload, propellant, structure")

rocket_parts()

output = rocket_parts()
output is None

def rocket_parts():
    return "payload, propellant, structure"
output = rocket_parts()
output

any([True, False, False])
any([False,False,False])

any()

str()

str(15)

def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"
distance_from_earth("Moon")

distance_from_earth("Saturn")

def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24

days_to_complete(238855, 75)

total_days = days_to_complete(238855, 75)
round(total_days)


def generate_report2(main_tank, external_tank, hydrogen_tank):
    output = f"""Fuel Report:
    Main tank: {main_tank}
    External tank:{external_tank}
    Hydrogen tank:{hydrogen_tank}
    """
    return print(output)
    main_tank = 80
    external_tank = 70
    hydrogen_tank = 75
output = generate_report(80,70,75)
generate_report2(80,70,75)

from datetime import timedelta, datetime

def arrival_time(hours = 51):
    now = datetime.now()
    arrival= now + timedelta(hours = hours)
    return arrival.strftime("Arrival: %A %H:%M")
arrival_time()

arrival_time(hours=0)

from datetime import  timedelta, datetime
def arrival_time(destination, hours = 51):
    now = datetime.now()
    arrival = now + timedelta(hours = hours)
    return arrival.strftime(f"{destination} Arrival: %A %H:%M")

arrival_time("Moon")

arrival_time("Orbit", hours=0.13)

def variable_length(*args):
    print(args)

variable_length()

variable_length("one","two")

def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to lauch is {total_minutes} minutes"
    else:
        return f"Total time to lauch is {total_minutes/60} hours"

sequence_time(4, 15, 78)

def variable_length(**kwargs):
    print(kwargs)

variable_length(tanks =1, day = "Wednesday", pilots =3)

def crew_members(**kwargs):
    print(f"{len(kwargs)} astronauts assigned for this mission:")
    for title, name in kwargs.items():
        print(f"{title}: {name}")

crew_members(captain = "Neil Armstrong", pilot = "Buzz Aldrin", command_pilot="Michael Collins")


