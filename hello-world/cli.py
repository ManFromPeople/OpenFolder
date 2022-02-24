import sys
print(sys.argv)
print(sys.argv[0]) #program name
print(sys.argv[1]) #first arg

print("Welcome to the greeter program")
name = input("Enter your name")
print("Greetings: " + name)

print("calculator program")
first_number = input("first number: ")
second_number = input("second number: ")
print(first_number + second_number)
print(int(first_number) + int(second_number))

parsecs_set = input("Enter parsecs set")
parsecs = int(parsecs_set)
lightyears = 3.26*parsecs
print(str(parsecs) + "parsecs is " + str(lightyears) + " lightyears")