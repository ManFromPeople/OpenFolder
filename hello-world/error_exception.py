open("/path/to/mars.jpg")

def main():
    open("/path/to/mars.jpg")
if __name__== '__main__':
    main()

try:
    open('config.txt')
except FileNotFoundError:
    print("Couldn't find the config.txt file!")

def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
if __name__ == '__main__':
    main()

main()

def main():
    try: configuration = open('D:\config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
    except(BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")


main()

try:
    open('D:\config.txt')
except FileNotFoundError as err:
    print("got a problem trying to read the file:", err)

try:
    open('C:\\config.txt')
except OSError as err:
    if err.errno == 2:
        print("Couldn't find the config.txt file!")
    elif err.errno == 13:
        print("Found config.txt but couldn't read it")


def water_left (astronauts, water_left, days_left):
    daily_usage = astronauts*11
    total_usage = daily_usage*days_left
    total_water_left = water_left - total_usage
    if total_water_left<0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} litres"

water_left(5,100,2)

try:
    water_left(5,100,2)
except RuntimeError as err:
    alert_navigation_system(err)

water_left("3", "200", None)

def water_left(astronauts, water_left, days_left):
    for argument in [astronauts, water_left,days_left]:
        try:
            #If argument is an int, the following operation will work
            argument/10
        except TypeError:
            # TypError will be raised only if it isn't the right type
            # Raise the same exception but with a better error message
            raise TypeError(f"All arguments must be of type int, but received:" f'{argument}'")
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} litres"



def water_left(astronauts, water_left, days_left):
    for argument in [astronauts, water_left, days_left]:
        try:
            # If argument is an int, the following operation will work
            argument / 10
        except TypeError:
            # TypError will be raised only if it isn't the right type
            # Raise the same exception but with a better error message
            raise TypeError(f"All arguments must be of type int, but received: '{argument}'")
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters

 water_left("3", "200", None)