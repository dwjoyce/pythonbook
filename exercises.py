##############################
# Chapter 1.
#

# A1.
3 + 5 / 2

# A2.
4 * 2 - 7

# A3.
7 ** 6

# A4.
11 // 4
11 % 4

# A5.
40 * 9 / 5 + 32


##############################
# Chapter 2.
#

# A1.
age = 21

# A2.
age * 365

# A3.
2017 - age + 100


##############################
# Chapter 3.
#

# A1.
abs(-35.5)

# A2.
round(-22.8364926, 4)

# A3.
abs(round(-7495.184758, 2))

# A4.
min(7, -8, 4, -12, 1)
max(7, -8, 4, -12, 1)


##############################
# Chapter 4.
#

# A1.
import turtle
turtle.speed(0)
turtle.forward(100)
turtle.left(60)
turtle.forward(100)
turtle.left(60)
turtle.forward(100)
turtle.left(60)
turtle.forward(100)
turtle.left(60)
turtle.forward(100)
turtle.left(60)
turtle.forward(100)
turtle.left(60)

# A2.
import turtle
turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.left(72)

# A3.
# Down to the pupil.


##############################
# Chapter 5.
#

# No exercises.


##############################
# Chapter 6.
#

# No exercises.


##############################
# Chapter 7.
#

# A1.
num1 = 10
num2 = 30
num3 = 50
num4 = 70
num5 = 90
total = num1 + num2 + num3 + num4 + num5
print(num1, num2, num3, num4, num5, total)

# A2.
year = 1996
age = 21
print(year, age, age + 10)

# A3.
print("Year of birth", year, "age is", age, "age in 10 years", age + 10)

# A4.
name = "Fred Bloggs"
print((name + "\t") * 100)

# A5.
import turtle

turtle.pencolor("red")
turtle.fillcolor("blue")
turtle.begin_fill()
turtle.circle(250)
turtle.end_fill()

turtle.pencolor("green")
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(150)
turtle.end_fill()

turtle.pencolor("black")
turtle.fillcolor("magenta")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()


##############################
# Chapter 8.
#

# A1.
name = input("What's your name? ")
print(name * 100)

# A2.
name = input("What's your name? ")
num = input("Give me a number: ")
print(name * int(num))

# A3.
day = input("Give me a day between 10 and 20: ")
print("That date will be the", day + "th")

# A4.
first_num_str = input('First number: ')
second_num_str = input('Second number: ')

first_num = float(first_num_str)
second_num = float(second_num_str)

total = first_num + second_num

print('The sum of those two numbers is', total)
print('The first number subtracted by the second is', first_num - second_num)
print('The first number divided by the second is', first_num / second_num)
print('The first number multiplied by the second is', first_num * second_num)


##############################
# Chapter 9.
#

# A1 - vip.py
print('Welcome to our VIP program for calculating cinema ticket prices')
print('Ticket prices are £5.00 for ordinary tickets, £6.00 for VIPs')

vip = input('Do you require a VIP ticket, yes or no? ')
price = 5.0

if vip == 'yes':
    price = price * 1.2
    print('You have chosen a VIP seat - enjoy your film!')

weekend = input('Is your viewing at the weekend, yes or no? ')
if weekend == 'yes':
    price = price * 1.5
    print('Weekend viewing adds on another 50%, sorry!')

popcorn = input('Would you like popcorn, yes or no? ')
if popcorn == 'yes':
    price = price + 1.25
print('Your total price is:', price)

# A2 - kiosk.y
choice = input("What you you like, 1. Mars (50p), 2. Kitkat (40p), 3. Galaxy (55p) or 4. Haribo (30p)? ")
if choice == "1":
    print("Please insert 50p")
if choice == "2":
    print("Please insert 40p")
if choice == "3":
    print("Please insert 55p")
if choice == "4":
    print("Please insert 30p")

# A3 - weather.py
weather = input("What's the weather today, sunny, rainy or cloudy? ")
if weather == "sunny":
    print("Bring some sun cream!")
if weather == "rainy":
    print("Bring your umbrella")
if weather == "cloudy":
    print("Bring a jumper")


##############################
# Chapter 10.
#

# A1 - kiosk.py
choice = input("What you you like, 1. Mars (50p), 2. Kitkat (40p), 3. Galaxy (55p) or 4. Haribo (30p)? ")
if choice == "1":
    print("Please insert 50p")
elif choice == "2":
    print("Please insert 40p")
elif choice == "3":
    print("Please insert 55p")
elif choice == "4":
    print("Please insert 30p")
else:
    print("Not a valid choice!")
    
# A2 - move.py
transport = input("What form of transport are you using, plane, car, bicycle or walking? ")
if transport == "plane":
    print("Fast")
elif transport == "car":
    print("Quick")
elif transport == "bicycle":
    print("Steady")
elif transport == "walking":
    print("Slow")
    
# A3 - shapes.py
import turtle
shape = input("What shape to draw, circle, square or star? ")
if shape == "circle":
    turtle.circle(100)
elif shape == "square":
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
elif shape == "star":
    turtle.forward(100)
    turtle.right(144)
    turtle.forward(100)
    turtle.left(72)
    turtle.forward(100)
    turtle.right(144)
    turtle.forward(100)
    turtle.left(72)
    turtle.forward(100)
    turtle.right(144)
    turtle.forward(100)
    turtle.left(72)
    turtle.forward(100)
    turtle.right(144)
    turtle.forward(100)
    turtle.left(72)
    turtle.forward(100)
    turtle.right(144)
    turtle.forward(100)
    turtle.left(72)
else:
    print("Sorry, can't do that one.")


##############################
# Chapter 11.
#

# A1 - largest.py
num1 = input("First number: ")
num2 = input("Second number: ")
num3 = input("Third number: ")

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
else:
    print(num3)
    
# A2 - car.py
color = input("What color is the car? ")
car_type = input("What type is the car? ")
price = input("What price is the car? ")

price = int(price)

if color == "red" and car_type == "sports" and price < 10000:
    print("I want that car!")


##############################
# Chapter 12.
#

# A1 - hundred.py
num = 0
while num <= 100:
    print(num)
    num = num + 1

# A2 - hundred.py
num = 0
while num <= 100:
    print(num)
    num = num + 1

num = 100
while num >= 0:
    print(num)
    num = num - 1

# A3 - hundred.py
num = 0
while num <= 100:
    print(num)
    num = num + 5

num = 100
while num >= 0:
    print(num)
    num = num - 5

# A4
import turtle
sides = input("How many sides to draw? ")
sides = int(sides)
num = 0
while num < sides:
    turtle.forward(100)
    turtle.left(360 / sides)
    num = num + 1


##############################
# Chapter 13.
#

# A1 - adder.py
total = 0
while True:
    num = input("Enter a number, or type 'quit' to stop: ")
    if num == "quit":
        break
    total = total + int(num)
print('The grand total is:', total)

# A2 - words.py
sentence = ""
while True:
    word = input("Enter a word, or 'stop': ")
    if word == "stop":
        break
    sentence = sentence + word
print(sentence)

# A3
import turtle
while True:
    sides = input("How many sides to draw, or 'stop': ")
    if sides == "stop":
        break
    sides = int(sides)
    num = 0
    while num < sides:
        turtle.forward(100)
        turtle.left(360 / sides)
        num = num + 1


##############################
# Chapter 14.
#

# A1 - guess.py
import random

number_to_guess = random.randrange(1, 101)
num_tries = 0

while num_tries < 6:
    user_guess = int(input('Guess the number: '))
    if user_guess == number_to_guess:
        print('Well done - you guessed right!')
        break
    elif user_guess < number_to_guess:
        print('Too low!')
    else:
        print('Too high!')
    num_tries = num_tries + 1

print('The answer was:', number_to_guess)

# A2 - poly.py
import turtle
import random

sides = random.randrange(3, 12)
num = 0
while num < sides:
    turtle.forward(100)
    turtle.left(360 / sides)
    num = num + 1


##############################
# Chapter 15.
#

# A1 - guess.py
import random
choices = ['rock', 'paper', 'scissors']

while True:
    user_choice = input("Enter your choice, rock, paper or scissors (or stop to quit): ")
    if user_choice == "stop":
        break

    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        print('Draw!')
    elif ((user_choice == 'rock' and computer_choice == 'scissors') or
          (user_choice == 'scissors' and computer_choice == 'paper') or
          (user_choice == 'paper' and computer_choice == 'rock')):
        print('You won! Computer choice', computer_choice)
    else:
        print('Computer won! Computer choice', computer_choice)

# A2 - sizes.py
import turtle
import random

colors = ['red', 'green', 'blue', 'magenta', 'cyan', 'yellow']
color = random.choice(colors)
turtle.fillcolor(color)

turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()


##############################
# Chapter 16.
#

# A1 - sentence.py
sentence = input("Type a sentence: ")
index = 0
while index < len(sentence):
    print(sentence[index])
    index = index + 2
    
index = len(sentence) - 1
while index >= 0:
    print(sentence[index])
    index = index - 2

print(sentence[::2])
print(sentence[-1::-2])

# A2 - daysofweek.py
day_names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
day_num = int(input("Please enter day of week, 1 - 7: "))
print(day_names[day_num - 1])

# A3 - planets.py
planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planet_type = input("Which type of planet, rocky or gaseous? ")
if planet_type == "rocky":
    print(planet_names[:4])
else:
    print(planet_names[4:])

# A4 - colors.py
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
print("Primary colors are:", colors[0], colors[3], colors[4])

# A5 - seasons.py
seasons = [['December', 'January', 'February'],
           ['March', 'April', 'May'],
           ['June', 'July', 'August'],
           ['September', 'October', 'November']]
choice = input("Which season, winter, spring, summer or autumn? ")
if choice == "winter":
    print(', '.join(seasons[0]))
elif choice == "spring":
    print(', '.join(seasons[1]))
elif choice == "summer":
    print(', '.join(seasons[2]))
elif choice == "autumn":
    print(', '.join(seasons[3]))


##############################
# Chapter 17.
#

# A1.
for num in range(1000, 2000, 50):
    print(num)
    
# A2.
for num in range(100, 0, -5):
    print(num)
    
# A3 - sides.py
import turtle
sides = input("How many sides to draw? ")
sides = int(sides)
for num in range(sides):
    turtle.forward(100)
    turtle.left(360 / sides)

# A4 - brekkie.py
breakfast = []
while True:
    item = input("What are we having for breakfast, or type 'stop': ")
    if item == "stop":
        break
    breakfast.append(item)
    
for item in breakfast:
    print("Yummy, I just love", item)

# A5 - bullseye.py
import turtle
turtle.up()

width = 20  # thickness of each circle

for num in range(11, 0, -1):
    turtle.goto(0, -num * width)
    if (num % 2) == 0:  # even
        turtle.fillcolor("white")
    else:
        turtle.fillcolor("red")

    turtle.begin_fill()
    turtle.circle(num * width)
    turtle.end_fill()

turtle.down()

##############################
# Chapter 18.
#

# A1. functions.py (new calc function)
def calc(num1, num2, operator):
    if operator == "add":
        print(num1 + num2)
    elif operator == "subtract":
        print(num1 - num2)
    elif operator == "multiply":
        print(num1 * num2)
    elif operator == "divide":
        print(num1 / num2)
        
calc(50, 40, "add")
calc(50, 40, "subtract")
calc(50, 40, "multiply")
calc(50, 40, "divide")

# A2. functions.py (new timestable function)
def timestable(rows):
    for row in range(1, rows + 1):
        for col in range(1, rows + 1):  # use same number
            print(row * col, end=" ")
        print()  # blank line

timestable(12)
timestable(3)
        
# A3. shapes.py
import turtle

def box():
    width = int(input("Box width: "))
    length = int(input("Box length: "))
    for side in range(4):
        if (side % 2) == 0:
            size = length
        else:
            size = width
        turtle.forward(size)
        turtle.left(90)

def circle():
    radius = int(input("Circle radius: "))
    turtle.circle(radius)
    
def polygon():
    num_sides = int(input("Polygon number sides: "))
    length = int(input("Polygon side length: "))
    for side in range(num_sides):
        turtle.forward(length)
        turtle.left(360 / num_sides)

def star():
    length = int(input("Star side length: "))
    for point in range(5):
        turtle.forward(length)
        turtle.right(144)
        turtle.forward(length)
        turtle.left(72)

while True:
    shape = input("Which shape to draw, box, circle, polygon, star, or 'stop': ")
    if shape == "stop":
        break
    elif shape == "box":
        box()
    elif shape == "circle":
        circle()
    elif shape == "polygon":
        polygon()
    elif shape == "star":
        star()


##############################
# Chapter 19.
#

def sum_up(num1, num2):
    return num1 + num2

# A1. functions.py (new add_list function)
def add_list(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total

print(add_list([1, 2, 3, 4, 5]))

# A2 - functions.py (new product function)
def product(num1, num2):
    return num1 * num2

print(sum_up(product(4, 5), product(6, 7)))

# A3 - functions.py (new prime function)
def prime(number):
    # return whether the number is prime (True) or not (False)
    if number < 2:
        return False
    for num in range(2, number):
        if number % num == 0:
            return False
    return True

print(prime(0))  # should print out False
print(prime(1))  # should print out False
print(prime(2))  # should print out True
print(prime(25))  # should print out False
print(prime(29))  # should print out True


##############################
# Chapter 20.
#

# A1.
mission_file = open("mission.txt")
for line in mission_file:
    print(line.upper())
mission_file.close()

# A2.
mission_file = open("mission.txt")
for line in mission_file:
    print(len(line))
mission_file.close()

# A3.
mission_file = open("mission.txt")
length_total = 0
num_words = 0
for line in mission_file:
    for word in line.split():
        length_total = length_total + len(word)    
        num_words = num_words + 1
mission_file.close()

print("Average number words per line is", length_total / num_words)


##############################
# Chapter 21.
#

# A1 - notes.py
notes_file = open("notes.txt", "w")
while True:
    sentence = input("Please type in a sentence, or 'stop': ")
    if sentence == "stop":
        break
    notes_file.write(sentence + "\n")
notes_file.close()

# A2 - notes.py (again)
notes_file = open("notes.txt", "w")
line_number = 1
while True:
    sentence = input("Please type in a sentence, or 'stop': ")
    if sentence == "stop":
        break
    notes_file.write(str(line_number) + ".  " + sentence + "\n")
    line_number = line_number + 1
notes_file.close()

# A3 - cipher.py
sentence = input("Please type in a sentence: ")
output_file = open("encoded.txt", "w")
for letter in sentence:
    output_file.write(str(ord(letter)) + " ")
output_file.close()


##############################
# Chapter 22.
#

# A1 - chapter 8 programs with try/except blocks.
try:
    name = input("What's your name? ")
    num = input("Give me a number: ")
    print(name * int(num))
except:
    print("That was not a number!")

###

try:
    first_num_str = input('First number: ')
    second_num_str = input('Second number: ')

    first_num = float(first_num_str)
    second_num = float(second_num_str)

    total = first_num + second_num

    print('The sum of those two numbers is', total)
    print('The first number subtracted by the second is', first_num - second_num)
    print('The first number divided by the second is', first_num / second_num)
    print('The first number multiplied by the second is', first_num * second_num)
except:
    print("One of those was not a number!")

# A2.
num1 = int(input("Type in first number: "))
num2 = int(input("Type in second number: "))
try:
    print("Result is", num1 / num2)
except ZeroDivisionError:
    print("That second number was zero!")
    
# A3 - openfile.py
try:
    filename = input("Type in name of file: ")
    in_file = open(filename)
    for line in in_file:
        print(line)
    in_file.close()
except FileNotFoundError:
    print("Sorry, that file does not exist")
