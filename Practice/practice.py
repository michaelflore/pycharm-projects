# Global Variables
position = "Student"


# Method to tell what position he really is, indent is important with methods
# Make sure there are 2 blank lines after
def myfunc():
    position = "Web Developer"
    print("Michael is a " + position)

# Print out Global Variable
print("Michael is a " + position)

# Text and Numeric Types
number = 5
string = "Mike"
myFloat = 20.5

# Print out the type, similar to what we do in JavaScript
print(type(number))
print(type(string))
print(type(myFloat))

# Sequence, Notice the brackets
aList = ["milk", "eggs", "butter"]
aTuple = ("this", "is", "awesome")
aRange = range(9)

# Print out their type
print(type(aList))
print(type(aTuple))
print(type(aRange))

for i in aList:
    print(i)
    if i == "eggs":
        break
adj = ["1", "2", "3"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

# Mapping
aDictionary = {"name": "mike", "age": 35}

# Print out type
print(type(aDictionary))

# Multi Line String
multiLineString = '''this is a
multi
line
string '''

print(multiLineString)

# STRINGS are arrays
name = "Mike"
last = "Flores"
print(name[0])

# Slicing the 4 is not included but lets say we wanted 'ike'
print(name[1:4])

# Length counts from 1
print(len(name), name.lower(), name.upper(), name.replace("M", "S"))
print(name + ' ' + last)

# Format method
quant = 3
number = 567
name = "bubbles"

myItem = "I want {} {} for the {} dogs that I have"
print(myItem.format(quant, name, number))

# For Loop
for i in range(5):
    print("hello")

# Measuring Strings
for i in aList:
    print(i, len(i))

# Read/Write Files
with open('pong.py') as file:
    read_data = file.read()
# file.closed Check that its closed

# keyboard input with if and else
kbdInput = int(input("Please Enter an Integer: "))

if kbdInput < 32:
    kbdInput = 32
    print("Integer is now: ", kbdInput)
elif kbdInput > 42:
    kbdInput = 42
    print("Integer is now: ", kbdInput)
else:
    print(kbdInput, "Hello.")
    myfunc()


