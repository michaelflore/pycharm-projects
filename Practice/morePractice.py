# Set - Sequence
# Tuple - Fixed Data, its faster
# Dictionaries - key value pairs

# Slicing for List and Tuple
word = "computer"

# counts from 0 and does not include the 4
print(word[1:4])

# 1-6 and the 2 stands for every other item
print(word[1:6:2])

# from 3 until the end
print(word[3:])

# 0-4
print(word[:5])

# last item
print(word[-1])

# last 3 items
print(word[-3:])

# Not the last 3 items
print(word[:-3])

# Working with Strings
anotherWord = "bug "

print(anotherWord * 3)
print("u" in anotherWord)

# min is the first in the alpha
bug = "bug"
print(min(bug), max(bug))
print(len(bug)) # from 1 because no such thing as 0 length

# List Sequence
myList = [8, 5] * 3
print(myList)

myListTwo = [7, 8, 3]
for item in myListTwo:
    print(item * 2)

anotherList = [2, 5, 8]
print(sum(anotherList))
print(sum(anotherList[-2:]))

animals = ["pig", "cow"]
print(sorted(animals))

x = "hippo"
print(x.count("p"))

animalsTwo = ["pig", "cow", "horse"]
vanessa, kayla, megan = animalsTwo
print(animalsTwo)












