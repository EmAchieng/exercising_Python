#String Formatting with %

#used the % operator to replace the %s

#Hello Mike
name = "Mike"
print ("Hello %s" % (name))

print "The %s who %s %s!" % ("Knights", "say", "Ni")
# This will print "The Knights who say Ni!"


name = raw_input("What is your name? ")
quest = raw_input("What is your quest? ")
color = raw_input("What is your favorite color? ")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)


#creating strings
'Alpha'
"Bravo"
str(3)

#string methods
len("Charlie")
"Delta".upper()
"Echo".lower()

#printing a string
print ("Foxtrot")

#string techniques
g = "Golf"
h = "Hotel"
print ("%s, %s" % (g, h))

#variable my_string
#find the length of the string
#change it to uppercase

my_string = "hey"
print len(my_string)
print my_string.upper()


#variable called now
#store the result of datetime.now()
#print now

from datetime import datetime

now = datetime.now()
print now

#if you want to get the current time details
from datetime import datetime
now = datetime.now()

current_year = now.year
current_month = now.month
current_day = now.day

from datetime import datetime

now = datetime.now()
print now

current_year = now.year
print current_year

current_month = now.month
print current_month

current_day = now.day
print current_day


#month, day year

from datetime import datetime
now = datetime.now()

print '%s/%s/%s' % (now.month, now.day, now.year)


#import datetime
from datetime import datetime
now = datetime.now()

print '%s:%s:%s' % (now.hour, now.minute, now.second)

#date and time combined
from datetime import datetime
now = datetime.now()

print '%s/%s/%s' % (now.month, now.day, now.year)
print '%s:%s:%s' % (now.hour, now.minute, now.second


#date and time combined
from datetime import datetime
now = datetime.now()

print '%s/%s/%s %s:%s:%s' % (now.year, now.month, now.day, now.hour, now.minute, now.second)


#conditionals


def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:
        return -1
    else:
        return 0


print
greater_less_equal_5(4)
print
greater_less_equal_5(5)
print
greater_less_equal_5(6)


#slicing strings
my_string = "Python"
my_string[1:] # "ython"

#Set new_word equal to the slice from the 1st index all the way to the end of new_word. Use [1:len(new_word)] to do this.

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
else:
    print 'empty'



def power(base, exponent):  # Add your parameters here!
  result = base ** exponent
  print "%d to the power of %d is %d." % (base, exponent, result)

power(37, 4)  # Add your arguments here!


#function calling a function
def fun_one(n):
  return n * 5

def fun_two(m):
  return fun_one(m) +  7



#function calling a function
def one_good_turn(n):
    return n + 1


def deserves_another(n):
    return one_good_turn(n) + 2

#more functions
def shout(phrase):
  if phrase == phrase.upper():
    return "YOU'RE SHOUTING!"
  else:
    return "Can you speak up?"

shout("I'M INTERESTED IN SHOUTING")

#import math
#Insert math. before sqrt() so that it has the form math.sqrt().
# This tells Python not only to import math, but to get the sqrt() function from within math.
import math
print math.sqrt(25)

#However, we only really needed the sqrt function, and it can be frustrating to have to keep typing math.sqrt(

from module import function

#Now you can just type sqrt() to get the square root of a number—no more math.sqrt()!
from math import sqrt


#universal import
from math import *

import math # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print everything # Prints 'em all!

#strings
def biggest_number(*args):
    print
    max(args)
    return max(args)


def smallest_number(*args):
    print
    min(args)
    return min(args)


def distance_from_zero(arg):
    print
    abs(arg)
    return abs(arg)


biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)

#finding the maximum value
max (10, 5, 4)

print (max)

#finding the minimum value

min (2, 4, 5)
print(min)

#abs()
#3 and -3 both have the same absolute value: 3.
#The abs() function always returns a positive value,
absolute = abs(-42)
print absolute

#type()
# returns the type of the data it receives as an argument.
print type(42) #int
print type(4.2) #float
print type('spam') #string

#functions
def speak(message):
  return message

if happy():
  speak("I'm happy!")
elif sad():
  speak("I'm sad.")
else:
  speak("I don't know what I'm feeling.")

#more functions
def shut_down(s):
    if s == "yes":
        return "Shutting down"


    elif s == "no":
        return "Shutdown aborted"

    else:
        return "Sorry"

#more functions
def is_numeric(num):
  return type(num) == int or type(num) == float:

max(2, 3, 4) # 4
min(2, 3, 4) # 2

abs(2) # 2
abs(-2) # 2

#def a function called distance_from_zero, with one argument (choose any argument name you like).

#If the type of the argument is either int or float, the function should return the absolute value of the function input.

#Otherwise, the function should return "Nope"

def distance_from_zero(num):
  if type(num) == int or type(num) == float:
    return abs(num)
  else:
    return "Nope"

#We define a function called bigger that has two arguments called first and second.
#Then, we print out the larger of the two arguments using the built-in function max.
#Finally, the bigger function returns Tru
  def bigger(first, second):
      print
      max(first, second)
      return True

#Write a function called answer that takes no arguments and returns the value 42.

#Even without arguments, you will still need parentheses.
  # Don't forget the colon at the end of the function definition!
  def answer():
      print()

      return 42

#the hotel costs 140 per night
  def hotel_cost(nights):
      return 140 * nights

def fruit_color(fruit):
  if fruit == "apple":
    return "red"
  elif fruit == "banana":
    return "yellow"
  elif fruit == "pear":
    return "green"

#more functions

  def plane_ride_cost(city):
      if city == "Charlotte":
          return 183
      elif city == "Tampa":
          return 220
      elif city == "Pittsburgh":
          return 222
      elif city == "Los Angeles":
          return 475

def finish_game(score):
  tickets = 10 * score
  if score >= 10:
    tickets += 50
  elif score >= 7:
    tickets += 20
  return tickets


def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475

def rental_car_cost(days):
    #Every day you rent the car costs $40.
  cost = days * 40
  if days >= 7:
      #if you rent the car for 7 or more days, you get $50 off your total.
    cost -= 50
  elif days >= 3:
      #if you rent the car for 3 or more days, you get $20 off your total.
    cost -= 20
  return cost


#We define two simple functions, double(n) and triple(p) that return 2 times or 3 times their input. Notice that they have n and p as their arguments
#We define a third function, add(a, b) that returns the sum of the previous two functions when called with a and b, respectively.




def double(n):
  return 2 * n

def triple(p):
  return 3 * p
#function calls the above functions. double and triple
def add(a, b):
  return double(a) + triple(b)




def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475

def rental_car_cost(days):
  cost = days * 40
  if days >= 7:
    cost -= 50
  elif days >= 3:
    cost -= 20
  return cost
#define a function called trip_cost that takes two arguments, city and days.
  #have your function return the sum of calling the rental_car_cost(days), hotel_cost(days), and plane_ride_cost(city) functions.
def trip_cost(city, days):
  return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city)




def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475

def rental_car_cost(days):
  cost = days * 40
  if days >= 7:
    cost -= 50
  elif days >= 3:
    cost -= 20
  return cost
#Modify your trip_cost function definition. Add a third argument, spending_money.

#Modify what the trip_cost function does. Add the variable spending_money to the sum that it returns.

def trip_cost(city, days, spending_money):
  return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

#print out the trip_cost( to "Los Angeles" for 5 days with an extra 600 dollars of spending money.

print trip_cost("Los Angeles", 5, 600)


  #ists
  zoo_animals = ["pangolin", "cassowary", "sloth", ];
  # One animal is missing!

  if len(zoo_animals) > 3:
      print
      "The first animal at the zoo is the " + zoo_animals[0]
      print
      "The second animal at the zoo is the " + zoo_animals[1]
      print
      "The third animal at the zoo is the " + zoo_animals[2]
      print
      "The fourth animal at the zoo is the " + zoo_animals[3]

#replacing item in a list using index
zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
# Last night our zoo's sloth brutally attacked
# the poor tiger and ate it whole.

# The ferocious sloth has been replaced by a friendly hyena.
zoo_animals[2] = "hyena"

# What shall fill the void left by our dear departed tiger?
# Your code here!
zoo_animals[3] = "giraffe"


letters = ['a', 'b', 'c']
letters.append('d')
print len(letters)
print letters


suitcase = []
suitcase.append("sunglasses")

# Your code here!
suitcase.append("toothbrush")
suitcase.append("mirror")
suitcase.append("comb")



list_length = 3 # Set this to the length of suitcase
print len(suitcase)
print "There are %d items in the suitcase." % (list_length)
print suitcase


suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

# The first and second items (index zero and one)
first = suitcase[0:2]

# Third and fourth items (index two and three)
middle = suitcase[2:4]

# The last two items (index four and five)
last =  suitcase[4:]


animals = "catdogfrog"

# The first three characters of animals
cat = animals[:3]

# The fourth through sixth characters
dog = animals[3:6]

# From the seventh character to the end
frog = animals[6:]


animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")# to find "duck"

# insert
animals.insert(duck_index,"cobra")

print animals # Observe what prints after the insert operation


#for statement
my_list = [1, 9, 3, 8, 5, 7]

for number in my_list:
    # Your code here
    print
    2 * number


#sort()
animals = ["cat", "ant", "bat"]
animals.sort()

for animal in animals:
  print animal

#Write a for-loop that iterates over start_list and .append()s each number squared (x ** 2) to square_list.

#Then sort square_list!

start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for number in start_list:
  square_list.append(number ** 2)
square_list.sort()

print square_list


#dictionaries
# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print residents['Puffin'] # Prints Puffin's room number

# keys will access the values

print residents['Sloth']
print residents['Burmese Python']


# key - animal_name : value - location
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

# Your code here!
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']

zoo_animals['Rockhopper Penguin'] = 'Pacific'



print zoo_animals





#Add a key to inventory called 'pocket'

#Set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'

#.sort() the items in the list stored under the 'backpack' key

#Then .remove('dagger') from the list of items stored under the 'backpack' key

#Add 50 to the number stored under the 'gold' key

inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort()


inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] = inventory['gold'] + 50



#removing items from a list
backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
backpack.remove('dagger')
print backpack

