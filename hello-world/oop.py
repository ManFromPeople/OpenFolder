class Car:

car = Car()

class Elevator:
    def __init__(self, starting_floor):
        self.make = "The evelator company"
        self.floor = starting_floor

# To create the object

elevator = Elevator(1)
print(elevator.make) # "The Elevator company"
print(elevator.floor) # 1

class Car:
    def __init__(self):
        self.color = "Red" # ends up on the object
        self.make = "Mercedes" # becomes a local variable in the constructor

car = Car()
print(car.color) # "Red"
print(car.make) # would result in an error, 'make' does not exist on teh object

class Square:
    def __int__(self):
        self.height = 2
        self.width = 2
    def set_side(self,new_side):
        self.height = new_side
        self.width = new_side

square = Square()
square.height = 3 # not a square anymore

class Square:
    def __init__(self):
      self._height = 2
      self._width = 2
    def set_side(new_side):
      self._height = new_side
      self._width = new_side

  square = Square()
  square._height = 3 # not a square anymore

class Square:
    def __init__(self):
      self.__height = 2
      self.__width = 2
    def set_side(new_side):
      self.__height = new_side
      self.__width = new_side

  square = Square()
  square.__height = 3 # raises AttributeError

  square = Square()
  square._Square__height = 3

class Square:
    def __init__(self):
      self.__height = 2
      self.__width = 2
    def set_side(self, new_side):
      self.__height = new_side
      self.__width = new_side
    def get_height(self):
        return self.__height
    def set_height(self,h):
        if h>= 0:
            self.__height =h
        else:
            raise Exception("value needs to be 0 or large")

square = Square()
square.__height = 3 # raises AttributeError


class Square:
    def __init__(self, w, h):
        self.height = h
        self.__width = w

    def set_side(self, new_side):
        self.__height = new_side
        self.__width = new_side
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, new_value):
        if new_value >=0:
            self.__height = new_value
        else:
            raise Exception("Value must be larger than 0")


class Participant:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choise = ""
    def choose(self):
        self.choise = input("{name}, select rock, paper or scissor:".format(name = self.name))
        print("{name} select {choise}".format(name=self.name, choise = self.choise))

class GameRound:
    def __init__(self, p1, p2):
        p1.choise()
        p2.choise()
    def compareChoise(self):
        print("implement")
    def awardPoints(self):
        print("implement")

class Game:
    def __init__(self):
        self.endGame = False
        self.paricipant = Participant("Spock")
        self.secondParticipant = Participant("Kirk")
    def start(self):
        game_round = GameRound(self.paricipant, self.secondParticipant)
    def checkEndCondition(self):
        print("implement")
    def determineWinner(self):
        print("implement")

game = Game()
game.start()

