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

#for statement
a = ["List", "of", "some", "sort"]
for x in a:
  # Do something for every x

  names = ["Adam", "Alex", "Mariah", "Martine", "Columbus"]

  for item in names:
      print item


# A simple dictionary
d = {"foo" : "bar"}

for key in d:
  print d[key]  # prints "bar"






webster = {
  "Aardvark" : "A star of a popular children's cartoon show.",
  "Baa" : "The sound a goat makes.",
  "Carpet": "Goes on the floor.",
  "Dab": "A small amount."
}

# Add your code below!
for key in webster:
  print webster[key]

#prints even numbers
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for number in a:
  if number % 2 == 0:
    print number


#list and functions
#define a function count_small that has one parameter, numbers
def count_small(numbers):
    #We initialize a variable total that we can use in the for loop.
  total = 0
  for n in numbers:
      #For each item n in numbers, if n is less than 10, we increment total.
      #After the for loop, we return total.
    if n < 10:
      total = total + 1
  return total
#After the function definition, we create an array of numbers called lotto
lotto = [4, 8, 15, 16, 23, 42]
#We call the count_small function, pass in lotto, and store the returned result in small.
small = count_small(lotto)
#Finally, we print out the returned result, which is 2 since only 4 and 8 are less than 10.
print small


#Write a function called fizz_count that takes a list x as input.
def fizz_count(x):
#Create a variable count to hold the ongoing count. Initialize it to zero.
  count = 0
#for each item in x:, if that item is equal to the string "fizz" then increment the count variable.
  for item in x:
    if item == "fizz":
      count = count + 1
        #After the loop, please return the count variable.
  return count


#string looping
for letter in "Codecademy":
    print
    letter

# Empty lines to make the output pretty
print
print

word = "Programming is fun!"

for letter in word:
    # Only print out the letter i
    if letter == "i":
        print
        letter

#animal count dictionary with 3 entries
animal_counts = {
  "ant": 3,
  "bear": 6,
  "crow": 2
}

#looping through dictinaries
#we create two dictionaries, once and twice, that have the same keys.

once  = {'a': 1, 'b': 2}
twice = {'a': 2, 'b': 4}
for key in once:
  print "Once: %s" % once[key]
  print "Twice: %s" % twice[key]



prices = {"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}

stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}

for food in prices:
  print food
  print "price: %s" % prices[food]
  print "stock: %s" % stock[food]


prices = {"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}

stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}

#Create a variable called total and set it to zero.
total = 0
#Loop through the prices dictionary
for food in prices:
    # For each key in prices, multiply the number in prices by the number in stock. Print that value into the console and then add it to total.
  print prices[food] * stock[food]
  total = total + prices[food] * stock[food]
    #, outside your loop, print total.
print total


#more functions
#, we first define a function called sum with a parameter numbers.
def sum(numbers):
    #We initialize the variable total which we will use as our running sum.
  total = 0
    #For each number in the list, we add that number to the running sum total.
  for number in numbers:
    total += number
        #At the end of the function, we return the running sum.
  return total
#After the function, we create, n, a list of numbers.
# we call the sum(numbers) function with the variable n and print the result.

n = [1, 2, 5, 10, 13]
print sum(n)

shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


# Define a function compute_bill that takes one argument food as input.

def compute_bill(food):
    #In the function, create a variable total with an initial value of zero.
    total = 0
    #For each item in the food list, add the price of that item to total.
    for item in food:
        total = total + prices[item]
        #return the total
    return total


shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


# While you loop through each item of food, only add the price of the item to total if the item's stock count is greater than zero.
#if the item is in stock and after you add the price to the total, subtract one from the item's stock count.

def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:
            total = total + prices[item]
            stock[item] = stock[item] - 1
    return total


shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


# Write your code below!
def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:
            total = total + prices[item]
            stock[item] = stock[item] - 1
    return total




#print each student details
lloyd = {
  "name": "Lloyd",
  "homework": [],
  "quizzes": [],
  "tests": []
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

students = [lloyd, alice, tyler]
for student in students:
  print student["name"]
  print student["homework"]
  print student["quizzes"]
  print student["tests"]



#python division
#a reminder of how division works in Python.

5 / 2
# 2

5.0 / 2
# 2.5

#To divide two integers and end up with a float, you must first use float() to convert one of the integers to a float.
float(5) / 2
# 2.5


lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

# Define a function called average that has one argument, numbers

def average(numbers):
    #Inside that function, call the built-in sum() function with the numbers list as a parameter. Store the result in a variable called total.
  total = sum(numbers)
    #use float() to convert total and store the result in total
  total = float(total)
    #Divide total by the length of the numbers list. Use the built-in len() function to calculate that.
    #Return that result.
  return total / len(numbers)


# we create a dictionary called cost that contains the costs of some fruit
cost = {
    "apples": [3.5, 2.4, 2.3],
    "bananas": [1.2, 1.8],
}
#we calculate the average cost of apples and the average cost of bananas.
# Since we like apples much more than we like bananas,
# we weight the average cost of apples by 90% and the average cost of bananas by 10%.
return 0.9 * average(cost["apples"]) + \
0.1 * average(cost["bananas"])

lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}



#weighted averages

def average(numbers):
    total = sum(numbers)
    total = float(total)
    return total / len(numbers)

#Define a function called get_average that takes one argument called student.
def get_average(student):

    #Make a variable homework that stores the average() of student["homework"]. for quizzes and tests too
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])

   #Multiply the 3 averages by their weights and return the sum of those three. Homework is 10%, quizzes are 30% and tests are 60%.
    return 0.1 * average(student["homework"]) + 0.3 * average(student["quizzes"]) + 0.6 * average(student["tests"])



#Define a function called get_class_average that has one argument class_list.
def get_class_average(class_list):
    #make an empty list called results.
  results = []
    #For each student item in the class_list, calculate get_average(student) and then call results.append() with that result.
  for student in class_list:
    student_avg = get_average(student)
    results.append(student_avg)
        #return the result of calling average() with results.
  return average(results)



#print out the result of calling get_class_average with your students list
#Your students should be [lloyd, alice, tyler].
#print the result of get_letter_grade for the class's average.

def get_class_average(class_list):
  results = []
  for student in class_list:
    student_avg = get_average(student)
    results.append(student_avg)
  return average(results)

students = [lloyd, alice, tyler]
class_avg = get_class_average(students)
print class_avg
print get_letter_grade(class_avg)


#, multiply the second element of the n list by 5
n = [1, 3, 5]
# Overwrite the second element with that result.
n[1] = n[1] * 5
print n

#pop
n = [1, 3, 5]
n.pop(1)
# Returns 3 (the item at index 1)
print n
# prints [1, 5]

#remove
n.remove(1)
# Removes 1 from the list,
# NOT the item at index 1
print n
# prints [3, 5]

#delete
del(n[1])
# Doesn't return anything
print n
# prints [1, 5]


#function

number = 5

def my_function(x):
    return x * 3

print my_function(number)

m = 5
n = 13


# Add add_function
def add_function(x, y):
    #return after adding
    return x + y


#print
print
add_function(m, n)

#spring concatenation
n = "Hello"
# Your function here!
def string_function(s):
	return s + 'world'

print string_function(n)


def list_function(x):
    return x

n = [3, 5, 7]
print list_function(n)


#using an element from a list in a function
#define a function called first_item. It has one argument called items.
def first_item(items):
    #Inside the function, print out the item stored at index zero of items.
  print items[0]
#After the function, create a new list called numbers.
numbers = [2, 7, 9]
#call the first_item function with numbers as its argument, which prints out 2
first_item(numbers)

#define a function called list_function
#Inside the function,  print out the item stored at index one of x
def list_function(x):
    return x[1]

n = [3, 5, 7]
print list_function(n)


def double_first(n):
  n[0] = n[0] * 2
#create a list called numbers.
numbers = [1, 2, 3, 4]
#use the double_first function to modify that list.
double_first(numbers)
#print out [2, 2, 3, 4]
print numbers

#Add 3 to the item at index 1 of the list.
#Store the result back into index 1.
#Return the list.

def list_function(x):
  x[1] = x[1] + 3
  return x

n = [3, 5, 7]
print list_function(n)




my_list = [1, 2, 3]
my_list.append(4)
print my_list
# prints [1, 2, 3, 4]



#Define a function called list_extender that has one parameter lst.
#Inside the function, append the number 9 to lst
#Then return the modified list.
n = [3, 5, 7]

def list_extender(lst):
  lst.append(9)
  return lst


print list_extender(n)

n = [3, 5, 7]

#Define a function called print_list that has one argument called x.
def print_list(x):
    #Inside that function, print out each element one by one. Use the existing code as a scaffold.

#Then call your function with the argument n.

    for i in range(0, len(x)):
        print
        x[i]


print_list(n)



#Create a function called double_list that takes a single argument x (which will be a list)
#and multiplies each element by 2 and return that list.
#6, 10, 14
n = [3, 5, 7]

def double_list(x):
  for i in range(0, len(x)):
    x[i] = x[i] * 2
  return x
# Don't forget to return your new list!

print double_list(n)



#[0, 1, 2].
def my_function(x):
  for i in range(0, len(x)):
    x[i] = x[i] * 2
  return x


#through items
for item in list:
  print item

#through indexes, ranges
for i in range(len(list)):
  print list[i]



print my_function(range(3)) # Add your range between the parentheses!





n = [3, 5, 7]
#define a function called total that accepts one argument called numbers. It will be a list.
def total(numbers):
    #Inside the function, create a variable called result and set it to zero.
    #Using one of the two methods above, iterate through the numbers list. For each number, add it to result.
    result = 0
    for n in range(len(numbers)):
        result += numbers[n]
        #return result.
    return result



n = ["Michael", "Lieberman"]
# Define a function called join_strings accepts an argument called words. It will be a list.

def join_strings(words):
    #Inside the function, create a variable called result and set it to "", an empty string.
    #Iterate through the words list and append each word to result.
    #return the result

  result = ""
  for word in words:
    result += word
  return result

print join_strings(n)


#two lists as two arguments in a function
a = [1, 2, 3]
b = [4, 5, 6]
print a + b
# prints [1, 2, 3, 4, 5, 6]


#define a function called join_lists that has two arguments, x and y. They will both be lists.
#Inside that function, return the result of concatenating x and y together.
m = [1, 2, 3]
n = [4, 5, 6]

# Add your code here!

def join_lists(x, y):
	return x + y


print join_lists(m, n)
# You want this to print [1, 2, 3, 4, 5, 6]



# define a function called join_lists that has two arguments, x and y. They will both be lists.
#Inside that function, return the result of concatenating x and y together.
m = [1, 2, 3]
n = [4, 5, 6]

def join_lists(x, y):
	return x + y


print join_lists(m, n)
# You want this to print [1, 2, 3, 4, 5, 6]



n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

#define a function called flatten with one argument called lists.
def flatten(lists):
    #Make a new, empty list called results.
  results = []
    #Iterate through lists. Call the looping variable numbers.
    #Iterate through numbers.
  for numbers in lists:
    for number in numbers:
        #For each number, .append() it to results.
      results.append(number)
            #return results from your function.
  return results

print flatten(n)


board = []
#Use range() to loop 5 times.
for num in range(0,5):
    #Inside the loop, .append() a list containing 5 "O"s to board, just like in the example above.
    board.append(["O"] * 5)
print board


#random integers
from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
# Add your code below!
print ship_row
print ship_col

guess_row = int(raw_input("Guess Row: "))
guess_col = int(raw_input("Guess Col: "))

#gaming 1
from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col
guess_row = int(raw_input("Guess Row: "))
guess_col = int(raw_input("Guess Col: "))

# Write your code below!
if guess_row == ship_row and guess_col == ship_col:
  print "Congratulations! You sank my battleship!"
else:
  print "You missed my battleship!"
  board[guess_row][guess_col] = "X"
  print_board(board)

#nested if statement
#check if guess_row is not in range(5) or guess_col is not in range(5).
#If that is the case, print out "Oops, that's not even in the ocean."
#After your new if statement, add an else that contains your existing handler for an incorrect guess. Don't forget to indent the code!
if guess_row == ship_row and guess_col == ship_col:
  print "Congratulations! You sank my battleship!"
else:
  if guess_row not in range(5) or \
    guess_col not in range(5):
    print "Oops, that's not even in the ocean."
  else:
    print "You missed my battleship!"
    board[guess_row][guess_col] = "X"
  print_board(board)


  #gaming 3
  from random import randint

  board = []

  for x in range(0, 5):
      board.append(["O"] * 5)


  def print_board(board):
      for row in board:
          print
          " ".join(row)


  print_board(board)


  def random_row(board):
      return randint(0, len(board) - 1)


  def random_col(board):
      return randint(0, len(board[0]) - 1)


  ship_row = random_row(board)
  ship_col = random_col(board)
  print
  ship_row
  print
  ship_col
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))

  # Write your code below!
  if guess_row == ship_row and guess_col == ship_col:
      print
      "Congratulations! You sank my battleship!"
  else:
      if guess_row not in range(5) or \
                      guess_col not in range(5):
          print
          "Oops, that's not even in the ocean."
      elif (board[guess_row][guess_col] == 'X'):
          print
          "You guessed that one already."
      else:
          print
          "You missed my battleship!"
          board[guess_row][guess_col] = "X"
      print_board(board)

#gaming
from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col
guess_row = int(raw_input("Guess Row: "))
guess_col = int(raw_input("Guess Col: "))

if guess_row == ship_row and guess_col == ship_col:
  print "Congratulations! You sank my battleship!"
else:
  if guess_row not in range(5) or \
    guess_col not in range(5):
    print "Oops, that's not even in the ocean."
  elif (board[guess_row][guess_col] == 'X'):
    print "You guessed that one already."
  else:
    print "You missed my battleship!"
    board[guess_row][guess_col] = "X"
  print_board(board)


#gaming

from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

# Everything from here on should be in your for loop
# don't forget to properly indent!
for turn in range(4):
  print "Turn", turn + 1
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print "Oops, that's not even in the ocean."
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
    else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"
    print_board(board)


#adding the break statement under the condition to end the loop after win
from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

# Everything from here on should be in your for loop
# don't forget to properly indent!
for turn in range(4):
  print "Turn", turn + 1
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"
    break
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print "Oops, that's not even in the ocean."
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
    else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"
    if (turn == 3):
      print "Game Over"
    print_board(board)


#game making with python
#Make multiple battleships: you'll need to be careful because you need to make sure that you don’t place battleships on top of each other on the game board. You'll also want to make sure that you balance the size of the board with the number of ships so the game is still challenging and fun to play.

#Make battleships of different sizes: this is trickier than it sounds. All the parts of the battleship need to be vertically or horizontally touching and you’ll need to make sure you don’t accidentally place part of a ship off the side of the board.

#Make your game a two-player game.

#Use functions to allow your game to have more features like rematches, statistics and more!


#Create a while loop that prints out all the numbers from 1 to 10 squared (1, 4, 9, 16, ... , 100), each on their own line.

#Fill in the blank space so that our while loop goes from 1 to 10 inclusive.
#Inside the loop, print the value of num squared. The syntax for squaring a number is num ** 2.
#Increment num.

num = 1

while num <= 10:  # Fill in the condition
  # Print num squared
  print num ** 2
  # Increment num (make sure to do this!)
  num += 1


  #loops
  choice = raw_input('Enjoying the course? (y/n)')

  while choice != 'y' and choice != 'n':  # Fill in the condition (before the colon)
      choice = raw_input("Sorry, I didn't catch that. Enter again: ")


#break
ount = 0

while True:
  print count
  count += 1
  if count >= 10:
    break

#while #else
import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
  num = random.randint(1, 6)
  print num
  if num == 5:
    print "Sorry, you lose!"
    break
  count += 1
else:
  print "You win!"





  #a game
  from random import randint

  # Generates a number from 1 through 10 inclusive
  random_number = randint(1, 10)

  guesses_left = 3
  # Start your game!
  while guesses_left > 0:
      guess = int(raw_input("Your guess: "))
      if guess == random_number:
          print
          "You win!"
          break
      guesses_left -= 1
  else:
      print
      "You lose."



#Create a for loop that prompts the user for a hobby 3 times.

#Save the result of each prompt in a hobby variable

#append each one to hobbies.

#print hobbies after your for loop

hobbies = []

# Add your code below!

for num in range(3):
  hobby =  raw_input("Tell me one of your favorite hobbies: ")
  hobbies.append(hobby)

print hobbies


#for loops
numbers  = [7, 9, 12, 54, 99]

print "This list contains: "

for num in numbers:
  print num

# Add your loop below!
for num in numbers:
    print num**2




#key and values
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
  # Your code here!
  print key, d[key]

  #multiple lists
  list_a = [3, 9, 17, 15, 19]
  list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

  for a, b in zip(list_a, list_b):
      # Add your code here!
      print
      max(a, b)




fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
  if f == 'tomato':
    print 'A tomato is not a fruit!' # (It actually is.)
    break
  print 'A', f
else:
  print 'A fine selection of fruits!'

  #this code executes the else statement
  fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

  print
  'You have...'
  for f in fruits:
      if f == 'tomato':
          print
          'A tomato is not a fruit!'  # (It actually is.)
      print
      'A', f
  else:
      print
      'A fine selection of fruits!'



      #is even
      def is_even(x):
          if x % 2 == 0:
              return True
          else:
              return False
    #is int

          def is_int(x):
              absolute = abs(x)
              rounded = round(absolute)
              return absolute - rounded == 0


    #digit_sum

          def digit_sum(n):
              a = 0
              for each in str(n):
                  a = a + int(each)
              return a

    #factorial that takes integer x as input

          def factorial(x):
              ans = 1
              while (x != 0):
                  ans *= x
                  x -= 1
              return ans



#Define a function called is_prime that takes a number x as input.

#For each number n from 2 to x - 1, test if x is evenly divisible by n.

#If it is, return False.

#If none of them are, then return True.
    #def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
                break
        else:
            return True




        #reverse function
        #Define a function called reverse that takes a string textand returns that string in reverse. For example: reverse("abcd") should return "dcba".

#You may not use reversed or [::-1] to help you with this.

#You may get a string containing special characters (for example, !, @, or #).

def reverse(text):
    string = ""
    l = len(text)
    while l > 0:
        string += text[l-1]
        l -= 1
    return string

print (reverse("car"))


#Define a function called anti_vowel that takes one string, text, as input and returns the text with all of the vowels removed.

#For example: anti_vowel("Hey You!") should return "Hy Y!". Don't count Y as a vowel. Make sure to remove lowercase and uppercase vowels

def anti_vowel(text):
    s = ""
    for c in text:
        if type(c) is str:
            d = c.lower()
            if d != 'a' and d != 'e' and d != 'i' and d != 'o' and d != 'u':
                s = s + c
        else:
            s = s + c
    return s

#Define a function scrabble_score that takes a string word as input and returns the equivalent scrabble score for that word.

#Assume your input is only one word containing no spaces or punctuation.
#As mentioned, no need to worry about score multipliers!
#Your function should work even if the letters you get are uppercase, lowercase, or a mix.
#Assume that you're only given non-empty strings.


score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}


def scrabble_score(word):
    total = 0
    for c in word:
        d = c.lower()
        total += score[d]
    return total

#
#Write a function called censor that takes two strings, text and word, as input.
    # It should return the text with the word you chose replaced with asterisks.

    def censor(text, word):
        index = text.index(word)
        l = len(word)
        text = str.replace(text, word, '*' * l)
        return text



#Define a function called count that has two arguments called sequence and item.

#Return the number of times the item occurs in the list.

#For example: count([1, 2, 1, 1], 1) should return 3 (because 1 appears 3 times in the list).

#There is a list method in Python that you can use for this, but you should do it the long way for practice.
#Your function should return an integer.
#The item you input may be an integer, string, float, or even another list!
#Be careful not to use list as a variable name in your code—it's a reserved word in Python!


def count(sequence, item):
    i = 0
    for x in sequence:
        if x == item:
            i = i + 1
    else:
        return i


#Define a function called purify that takes in a list of numbers,
# removes all odd numbers in the list, and returns the result.
# For example, purify([1,2,3]) should return [2].

#Do not directly modify the list you are given as input; instead, return a new list with only the even numbers.

def purify(l):
    return filter(lambda x: x % 2 == 0, l)





#Define a function called product that takes a list of integers as input
# and returns the product of all of the elements in the list.
# For example: product([4, 5, 5]) should return 100 (because 4 * 5 * 5 is 100).

#Don't worry about the list being empty.
#Your function should return an integer.


def product(l):
    total = 1
    for d in l:
        total *= d
    return total

#Write a function remove_duplicates that takes in a list and removes elements of the list that are the same.

#For example: remove_duplicates([1, 1, 2, 2]) should return [1, 2].

#Don't remove every occurrence, since you need to keep a single occurrence of a number.
#The order in which you present your output does not matter. So returning [1, 2, 3] is the same as returning [3, 1, 2].
#Do not modify the list you take as input! Instead, return a new list.

def remove_duplicates(l):
    nl = []
    for i in l:
        if i not in nl:
            nl.append(i)
    return nl



#Write a function called median that takes a list as an input
# and returns the median value of the list. For example: median([1, 1, 2]) should return 1.

#The list can be of any size and the numbers are not guaranteed to be in any particular order. Make sure to sort it!
#If the list contains an even number of elements, your function should return the average of the middle two.





#Define a function on line 3 called print_grades with one argument, a list called grades_input.

#Inside the function, iterate through grades_input and print each item on its own line.

#After your function, call print_grades with the grades list as the parameter.

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade
print_grades(grades)

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]



#On line 3, define a function, grades_sum, that does the following:

#Takes in a list of scores, scores
#Computes the sum of the scores
#Returns the computed sum.
#Call the newly created grades_sum function with the list of grades and print the result.
def grades_sum(scores):
    total = 0
    for grade in scores:
        total += grade
    return total


print
grades_sum(grades)




#computing the average
#Define a function, grades_average, below the grades_sum function that does the following:

#Has one argument, grades_input, a list
#Calls grades_sum with grades_input
#Computes the average of the grades by dividing that sum by float(len(grades_input)).
#Returns the average.
#Call the newly created grades_average function with the list of grades and print the result.


rades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


def grades_sum(scores):
    total = 0
    for grade in scores:
        total += grade
    return total


print
grades_sum(grades)


def grades_average(grades):
    sums = grades_sum(grades)
    return sums / float(len(grades))


print
grades_average(grades)


#the variance
#define a new function called grades_variance that accepts one argument, scores, a list.

#First, create a variable average and store the result of calling grades_average(scores).

#Next, create another variable variance and set it to zero. We will use this as a rolling sum.

#for each score in scores: Compute its squared difference: (average - score) ** 2 and add that to variance.

#Divide the total variance by the number of scores.

#Then, return that result.

#Finally, after your function code, print grades_variance(grades).

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


def print_grades(grades_input):
    for grade in grades_input:
        print
        grade


def grades_sum(scores):
    total = 0
    for score in scores:
        total += score
    return total


def grades_average(grades_input):
    sum_of_grades = grades_sum(grades_input)
    average = sum_of_grades / float(len(grades_input))
    return average


def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        var = (average - score) ** 2
        variance += var
    return variance / len(scores)


print
grades_variance(grades)





#standard deviation
#Define a function, grades_std_deviation, that takes one argument called variance.

#return the result of variance ** 0.5

#After the function, create a new variable called variance and store the result of calling grades_variance(grades).

#Finally print the result of calling grades_std_deviation(variance).




grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


def print_grades(grades_input):
    for grade in grades_input:
        print
        grade


def grades_sum(scores):
    total = 0
    for score in scores:
        total += score
    return total


def grades_average(grades_input):
    sum_of_grades = grades_sum(grades_input)
    average = sum_of_grades / float(len(grades_input))
    return average


def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        var = (average - score) ** 2
        variance += var
    return variance / len(scores)


print
grades_variance(grades)


def grades_std_deviation(variance):
    return variance ** 0.5


variance = grades_variance(grades)

print
grades_std_deviation(variance)


#print the results out
print print_grades(grades)
print grades_sum(grades)
print grades_average(grades)
print grades_variance(grades)
print grades_std_deviation(variance)




#dictionaries
#Create your own Python dictionary, my_dict, in the editor to the right with two or three key/value pairs.

#Then, print the result of calling the my_dict.items().

my_dict = {
    "Name": "yemi",
    "Age": 10,

}

print
my_dict.items()




#keys and values
#Remove your call to .items() and replace it with a call to .keys() and a call to .values(), each on its own line. Make sure to print both!
my_dict = {
    "Name": "yemi",
    "Age": 10,

}

print
my_dict.keys()
print
my_dict.values()



#the in operator
#For each key in my_dict: print out the key , then a space, then the value stored by that key. (You should use print a, b rather than print a + " " + b.)
my_dict = {
    "Name": "yemi",
    "Age": 10,

}

for key in my_dict:
    print
    key, my_dict[key]

print
my_dict.keys()
print
my_dict.values()


#an example
for number in range(5):
  print number,

d = {
  "name": "Eric",
  "age": 26
}

for key in d:
  print key, d[key],

for letter in "Eric":
  print letter,  # note the comma!



  #list comprehesive syntax
  #Use a list comprehension to build a list called even_squares in the editor.

#Your even_squares list should include the squares of the even numbers between 1 to 11. Your list should start [4, 16, 36...] and go from there.

doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]

# Complete the following line. Use the line above for help.
even_squares = [x **2 for x in range(1,12) if x % 2 ==0]

print even_squares





#Use a list comprehension to create a list, cubes_by_four.

#The comprehension should consist of the cubes of the numbers 1 through 10 only if the cube is evenly divisible by four.

#Finally, print that list to the console.

#Note that in this case, the cubed number should be evenly divisible by 4, not the original number.

cubes_by_four = [x ** 3 for x in range(1,11) if (x ** 3) % 4 == 0]


print cubes_by_four





#list sliding
l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print l[2:9:2]


#Omitting Indices
#If you don't pass a particular index to the list slice, Python will pick a default.
#Use list slicing to print out every odd element of my_list from start to finish.

#Omit the start and end index. You only need to specify a stride.

my_list = range(1, 11) # List of numbers 1 - 10

# Add your code below!
my_list = range(1, 11) # List of numbers 1 - 10

print my_list[::2] # returns [1, 3, 5, 7, 9]




#Reversing a List
my_list = range(1, 11)

# Add your code below!
backwards = my_list[::-1]
print backwards # prints [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]



#stride length
#Create a variable, backwards_by_tens,
# and set it equal to the result of going backwards through to_one_hundred by tens.
# Go ahead and print backwards_by_tens to the console.


to_one_hundred = range(101)
# Add your code below!

backwards_by_tens = to_one_hundred[::-10]
print backwards_by_tens # prints [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]



#Create a list, to_21, that's just the numbers from 1 to 21, inclusive.

#Create a second list, odds, that contains only the odd numbers in the to_21 list (1, 3, 5, and so on). Use list slicing for this one instead of a list comprehension.

#Finally, create a third list, middle_third, that's equal to the middle third of to_21, from 8 to 14, inclusive.

to_21 = range(1,22)
odds = to_21[::2]
middle_third = to_21[7:14]

print to_21
print odds
print middle_third




#anonymous functions
my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

#One of the more powerful aspects of Python is that it allows for a style of programming called functional programming, which means that you're allowed to pass functions around just as if they were variables or values. Sometimes we take this for granted, but not all languages allow this!

#Check out the code at the right. See the lambda bit? Typing

lambda x: x % 3 == 0
Is the same as

def by_three(x):
  return x % 3 == 0
#Only we don't need to actually give the function a name; it does its work and returns a value without one. That's why the function the lambda creates is an anonymous function.

#When we pass the lambda to filter, filter uses the lambda to determine what to filter, and the second argument (my_list, which is just the numbers 0 – 15) is the list it does the filtering on.


#lambda syntax
# The lambda should ensure that only "Python" is returned by the filter.

#Fill in the second part of the filter function with languages, the list to filter.
cubes = [x ** 3 for x in range(1, 11)]
filter(lambda x: x % 3 == 0, cubes)







#Create a list, squares, that consists of the squares of the numbers 1 to 10. A list comprehension could be useful here!

#Use filter() and a lambda expression to print out only the squares that are between 30 and 70 (inclusive).
squares = [x ** 2 for x in range(1, 11)]

print filter(lambda x: x >= 30 and x <= 70, squares)





#iterating over dictionaries
movies = {
  "Monty Python and the Holy Grail": "Great",
  "Monty Python's Life of Brian": "Good",
  "Monty Python's Meaning of Life": "Okay"
}

print movies.items()




#comprehending comprehensions
#Use a list comprehension to create a list,
#  threes_and_fives, that consists only of the numbers between 1 and 15 (inclusive) that are evenly divisible by 3 or 5.
threes_and_fives = [x for x in range(1,16) if x % 3 == 0 or x % 5 == 0]
print threes_and_fives


#list slicing
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"

forwards = garbled[::-1]
print forwards


message = forwards[::2]
print message


#lambda expressions
my_list = range(16)
filter(lambda x: x % 3 == 0, my_list)


#Create a new variable called message.

#Set it to the result of calling filter() with the appropriate lambda that will filter out the "X"s. The second argument will be garbled.

#Finally, print your message to the console.


message = filter(lambda a: a != "X", garbled)
print message



#python classes
class Fruit(object):
  """A class that makes various tasty fruits."""
  def __init__(self, name, color, flavor, poisonous):
    self.name = name
    self.color = color
    self.flavor = flavor
    self.poisonous = poisonous

  def description(self):
    print "I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor)

  def is_edible(self):
    if not self.poisonous:
      print "Yep! I'm edible."
    else:
      print "Don't eat me! I am super poisonous."

lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()


#go ahead and define an __init__() function for your Animal class. Pass it the argument self for now;

class Animal(object):
    def __init__(self):
        pass


#Pass __init__() a second parameter, name.
#In the body of __init__(), let the function know that name refers to the created object's name by typing self.name = name.

class Animal(object):
    def __init__(self,name):
        self.name = name


#Outside the Animal class definition, create a variable named zebra and set it equal to Animal("Jeffrey").

#Then print out zebra's name.

class Animal(object):
    def __init__(self, name):
        self.name = name


zebra = Animal("Jeffrey")
print
zebra.name


#we can add is_hungry attribute
# Class definition
class Animal(object):
  """Makes cute animals."""
  # For initializing our instance objects
  def __init__(self, name, age, is_hungry):
    self.name = name
    self.age = age
    self.is_hungry = is_hungry

# Note that self is only used in the __init__()
# function definition; we don't need to pass it
# to our instance objects.

zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)

print zebra.name, zebra.age, zebra.is_hungry
print giraffe.name, giraffe.age, giraffe.is_hungry
print panda.name, panda.age, panda.is_hungry

#class scope


#When dealing with classes, you can have variables that are available everywhere (global variables),
# variables that are only available to members of a certain class (member variables),
# and variables that are only available to particular instances of a class (instance variables).

#The same goes for functions: some are available everywhere,
#  some are only available to members of a certain class,
# and still others are only available to particular instance objects.



class Animal(object):
  """Makes cute animals."""
  is_alive = True
  def __init__(self, name, age):
    self.name = name
    self.age = age

zebra = Animal("Jeffrey", 2)
giraffe = Animal("Bruce", 1)
panda = Animal("Chad", 7)

print zebra.name, zebra.age, zebra.is_alive
print giraffe.name, giraffe.age, giraffe.is_alive
print panda.name, panda.age, panda.is_alive




#methodolical Approach
#Add a method, description, to your Animal class.
# Using two separate print statements,
# it should print out the name and age of the animal it's called on.
# Then, create an instance of Animal, hippo (with whatever name and age you like), and call its description method.

class Animal(object):
    """Makes cute animals."""
    is_alive = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Add your method here!
    def description(self):
        print
        self.name
        print
        self.age


hippo = Animal("Anderson", 36)
hippo.description()


#member variables
#A class can have any number of member variables. These are variables that are available to all members of a class.




class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = "good"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Add your method here!
    def description(self):
        print
        self.name
        print
        self.age


hippo = Animal("Anderson", 36)
hippo.description()

sloth = Animal("Kemi", 12)
ocelot = Animal("Kemi", 7)

hippo.description()

print
hippo.health
print
sloth.health
print
ocelot.health




#another example
#he example above, we create two instances of an Animal.
#Then we print out True, the default value stored in hippo's is_alive member variable.
#Next, we set that to False and print it out to make sure.
#Finally, we print out True, the value stored in cat's is_alive member variable. We only changed the variable in hippo, not in cat.
hippo = Animal("Jake", 12)
cat = Animal("Boots", 3)
print hippo.is_alive
hippo.is_alive = False
print hippo.is_alive
print cat.is_alive





#Create an instance of ShoppingCart called my_cart.
# Initialize it with any values you like, then use the add_item method to add an item to your cart.
class ShoppingCart(object):
  """Creates shopping cart objects
  for users of our fine website."""
  items_in_cart = {}
  def __init__(self, customer_name):
    self.customer_name = customer_name

  def add_item(self, product, price):
    """Add product to the cart."""
    if not product in self.items_in_cart:
      self.items_in_cart[product] = price
      print product + " added."
    else:
      print product + " is already in the cart."

  def remove_item(self, product):
    """Remove product from the cart."""
    if product in self.items_in_cart:
      del self.items_in_cart[product]
      print product + " removed."
    else:
      print product + " is not in the cart."

my_cart = ShoppingCart("Eric")
my_cart.add_item("Ukelele", 10)



#more classes
class Customer(object):
    """Produces objects that represent customers."""
    def __init__(self, customer_id):
        self.customer_id = customer_id

    def display_cart(self):
        print "I'm a string that stands in for the contents of your shopping cart!"

class ReturningCustomer(Customer):
    """For customers of the repeat variety."""
    def display_order_history(self):
        print "I'm a string that stands in for your order history!"

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()



#inheritance syntax


class DerivedClass(BaseClass):
  # code goes here

#example
class Shape(object):
    """Makes shapes!"""
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides

# Add your Triangle class below!
class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3



#overidding
#Sometimes you'll want one class that inherits from another to not only take on the methods and attributes of its parent,
        #  but to override one or more of them.


class Employee(object):
  def __init__(self, name):
    self.name = name
  def greet(self, other):
    print "Hello, %s" % other.name

class CEO(Employee):
  def greet(self, other):
    print "Get back to work, %s!" % other.name

ceo = CEO("Emily")
emp = Employee("Steve")
emp.greet(ceo)
# Hello, Emily
ceo.greet(emp)




#Create a new class, PartTimeEmployee, that inherits from Employee.

#Give your derived class a calculate_wage method that overrides Employee's. It should take self and hours as arguments.

#Because PartTimeEmployee.calculate_wage overrides Employee.calculate_wage, it still needs to set self.hours = hours.

#It should return the part-time employee's number of hours worked multiplied by 12.00 (that is, they get $12.00 per hour instead of $20.00)



class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00


class Employee(object):
    """Models real-life employees!"""

    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00


# Add your code below!
#first, inside your PartTimeEmployee class:

#Add a new method called full_time_wage with the arguments self and hours.
#That method should return the result of a super call to the calculate_wage method of PartTimeEmployee's parent class. Use the example above for help.
#Then, after your class:

#Create an instance of the PartTimeEmployee class called milton. Don't forget to give it a name.
#Finally, print out the result of calling his full_time_wage method. You should see his wage printed out at $20.00 per hour! (That is, for 10 hours, the result should be 200.00.)
class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00

    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(hours)


milton = PartTimeEmployee('Milton')
print
milton.full_time_wage(10)



#class basics
#Create a class, Triangle.
# Its __init__() method should take self, angle1, angle2, and angle3 as arguments.
#  Make sure to set these appropriately in the body of the __init__() method (see the Hint for more).


class Triangle(object):
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3


#Inside the Triangle class:

#Create a variable named number_of_sides
#and set it equal to 3.
#Create a method named check_angles.
# The sum of a triangle's three angles should return True if the sum of self.angle1, self.angle2, and self.angle3 is equal 180, and False otherwise.



class Triangle(object):
    number_of_sides = 3

    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check_angles(self):
        if (self.angle1 + self.angle2 + self.angle3) == 180:
            return True
        else:
            return False


    #Create a variable named my_triangle and set it equal to a new instance of your Triangle class. Pass it three angles that sum to 180 (e.g. 90, 30, 60).

#Print out my_triangle.number_of_sides

#Print out my_triangle.check_angles

class Triangle(object):
    number_of_sides = 3

    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check_angles(self):
        if (self.angle1 + self.angle2 + self.angle3) == 180:
            return True
        else:
            return False


my_triangle = Triangle(90, 30, 60)

print
my_triangle.number_of_sides
print
my_triangle.check_angles()


#Create a class named Equilateral that inherits from Triangle.

#Inside Equilateral, create a member variable named angle and set it equal to 60.

#Create an __init__() function with only the parameter self, and set self.angle1, self.angle2, and self.angle3 equal to self.angle (since an equilateral triangle's angles will always be 60˚).


class Triangle(object):
    number_of_sides = 3

    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check_angles(self):
        if (self.angle1 + self.angle2 + self.angle3) == 180:
            return True
        else:
            return False


my_triangle = Triangle(90, 30, 60)

print
my_triangle.number_of_sides
print
my_triangle.check_angles()


class Equilateral(Triangle):
    angle = 60

    def __init__(self):
        self.angle1 = self.angle
        self.angle2 = self.angle
        self.angle3 = self.angle


#instance of the class belwo the class
class Car(object):
   pass
my_car = Car()


#class memeber variables
class Car(object):
  condition = "new"

my_car = Car()


#structure
class ClassName(object):
  memberVariable = "initialValue"


#calling the class member variables using the print statement
class Car(object):
  condition = "new"

my_car = Car()

print my_car.condition


#initializing a class
class Car(object):
   condition = "new"
   def __init__(self, model, color, mpg):
       self.model = model
       self.color = color
       self.mpg = mpg

my_car = Car("Delorean", "silver", 88)

print my_car.condition



#refering to member variables
#Referring to member variables
#Calling class member variables works the same whether those values are created within the class
# (like our car's condition) or values are passed into the new object at initialization. We use dot notation to access the member variables of classes since those variables belong to the object.

#For instance, if we had created a member variable named new_variable,
# a new instance of the class named new_object could access this variable by saying:

new_object.new_variable


#Now that you've created my_car print its member variables:

#First print the model of my_car. Click "Stuck? Get a hint!" for an example.
#Then print out the color of my_car.
#Then print out the mpg of my_car.


class Car(object):
   condition = "new"
   def __init__(self, model, color, mpg):
       self.model = model
       self.color = color
       self.mpg = mpg

my_car = Car("DeLorean", "silver", 88)

print my_car.condition

print my_car.model
print my_car.color
print my_car.mpg



#creating class members
#Besides member variables, classes can also have their own methods. For example:

class Square(object):
  def __init__(self, side):
    self.side = side

  def perimeter(self):
    return self.side * 4

#The perimeter() class method is identical to defining any other function, except that it is written inside of the Square class definition.

#Just like when we defined __init__(), you need to provide self as the first argument of any class method.



#creating class methods
#The perimeter() class method is identical to defining any other function,
# except that it is written inside of the Square class definition.

#Just like when we defined __init__(), you need to provide self as the first argument of any class method.
class Car(object):
    condition = "new"

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

    def display_car(self):
        print
        "This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg))


my_car = Car("DeLorean", "silver", 88)

my_car.display_car()


#another example
class Square(object):
  def __init__(self, side):
    self.side = side

  def perimeter(self):
    return self.side * 4








#Inside the Car class, add a method drive_car that sets self.condition to the string "used".

#Remove the call to my_car.display_car() and instead print only the condition of your car.

#Then drive your car by calling the drive_car method.

#Finally, print the condition of your car again to see how its value changes.
  class Car(object):
      condition = "new"

      def __init__(self, model, color, mpg):
          self.model = model
          self.color = color
          self.mpg = mpg

      def display_car(self):
          print
          "This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg))

      def drive_car(self):
          self.condition = "used"

  my_car = Car("DeLorean", "silver", 88)

  print
  my_car.condition
  print
  my_car.drive_car()
  print
  my_car.condition









#inheritance
#Create a class ElectricCar that inherits from Car.
# Give your new class an __init__() method of that includes a battery_type member variable in addition to the model, color and mpg.

#Then, create an electric car named my_car with a "molten salt" battery_type.
  # Supply values of your choice for the other three inputs (model, color and mpg).

  class Car(object):
      condition = "new"

      def __init__(self, model, color, mpg):
          self.model = model
          self.color = color
          self.mpg = mpg

      def display_car(self):
          print
          "This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg))

      def drive_car(self):
          self.condition = "used"

  class ElectricCar(Car):
      def __init__(self, model, color, mpg, battery_type):
          self.model = model
          self.color = color
          self.mpg = mpg
          self.battery_type = battery_type

  my_car = ElectricCar("DeLorean", "silver", 88, "molten salt")



  #Inside ElectricCar add a new method drive_car that changes the car's condition to the string "like new".

#Then, outside of ElectricCar, print the condition of my_car

#Next, drive my_car by calling the drive_car function

#Finally, print the condition of my_car again


class Car(object):
    condition = "new"

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

    def display_car(self):
        print
        "This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg))

    def drive_car(self):
        self.condition = "used"


class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        self.model = model
        self.color = color
        self.mpg = mpg
        self.battery_type = battery_type

    def drive_car(self):
        self.condition = "like new"


my_car = ElectricCar("DeLorean", "silver", 88, "molten salt")

print
my_car.condition
print
my_car.drive_car()
print
my_car.condition


#classes
#Define a Point3D class that inherits from object

#Inside the Point3D class, define an __init__() function that accepts self, x, y, and z, and assigns these numbers to the member variables self.x, self.y, self.z

#Define a __repr__() method that returns "(%d, %d, %d)" % (self.x, self.y, self.z). This tells Python to represent this object in the following format: (x, y, z).

#Outside the class definition, create a variable named my_point containing a new instance of Point3D with x=1, y=2, and z=3.

#Finally, print my_point.

class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return "(%d, %d, %d)" %(self.x, self.y, self.z)

my_point = Point3D(1, 2, 3)
print my_point


#file input output
my_list = [i ** 2 for i in range(1, 11)]
# Generates a list of squares of the numbers 1 - 10

f = open("output.txt", "w")

for item in my_list:
  f.write(str(item) + "\n")

f.close()


#open
#f = open("output.txt", "w")
#Create a variable, my_file,
# and set it equal to calling the open() function on output.txt.
# In this case, pass "r+" as a second argument to the function so the file will allow you to read and write to it! (See the Hint for details.)

my_file = open("output.txt", "r+")

#writing
my_file.write("Data to be written")

#Iterate over my_list to get each value.

#Use my_file.write() to write each value to a text file called, output.txt.

#Make sure to call str() on the iterating data so .write() will accept it.

#Make sure to add a newline (+ "\n") after each element to ensure each will appear on its own line.

#Use my_file.close() to close the file when you're done.

#Passing the exercise means that you successfully wrote my_list to output.txt!

my_list = [i ** 2 for i in range(1, 11)]

my_file = open("output.txt", "w")

# Add your code below!
for item in my_list:
    my_file.write(str(item) + "\n")

my_file.close()

#reading
#Declare a variable, my_file, and set it equal to the file object returned by calling open() with both "output.txt" and "r".

#Next, print the result of using .read() on my_file, like the example above.

#Make sure to .close() your file when you're done with it! All kinds of doom will happen if you don't.
#Declare a new variable my_file and store the result of calling open() on the "text.txt" file in "r"ead-only mode.

#On three separate lines, print out the result of calling my_file.readline()

my_file = open("output.txt", "r")

print my_file.read()

my_file.close()


my_file = open("text.txt", "r")

print my_file.readline()
print my_file.readline()
print my_file.readline()

my_file.close()





















# Use a file handler to open a file for writing
write_file = open("text.txt", "w")

# Open the file for reading
read_file = open("text.txt", "r")

# Write to the file
write_file.write("Not closing files is VERY BAD.")

#During the I/O process, data is buffered: this means that it is held in a temporary location before being written to the file.

#Python doesn't flush the buffer—that is,
# write data to the file—until it's sure you're done writing.
# One way to do this is to close the file.
# If you write to a file without closing, the data won't make it to the target file.
#Check out our extremely bad code in the editor. Click Run—you'll note that our read_file.read() didn't read any data back!

#Add a write_file.close() call after writing to the file but before reading it.
#Add a read_file.close() call after the print read_file.read() line


# Try to read from the file
print read_file.read()

read_file = open("text.txt", "r")
write_file.write("Not closing files is VERY BAD.")
write_file.close()
print read_file.read()
read_file.close()
#Note that we don't explicitly close() our file, and remember that if we don't close a file, our data will get stuck in the buffer.



#with and as keywords
with open("file", "mode") as variable:
  # Read or write to the file




  with open("text.txt", "w") as my_file:
      my_file.write("My Data!")


      #Below your with...as code, do two things:

#Check if the file is not closed.
#If that's the case, call .close() on it.
#(You don't need an else here, since your if statement should do nothing if closed is True.)
#After your if statement, print out the value of my_file.closed to make sure your file is really closed.

with open("text.txt", "w") as my_file:
    my_file.write("Hello Python!")
    if not my_file.closed:
        my_file.close()
    print my_file.closed