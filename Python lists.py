thisList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thisList)
print(len(thisList))

# Print the second item of the list:
print(thisList[1])

# Print the last item of the list:
print(thisList[-1])

# Return the third, fourth, and fifth item:
print(thisList[2:5])

#  returns the items from the beginning to, but NOT including, "kiwi":
print(thisList[:4])

# returns the items from "cherry" to the end:
print(thisList[2:])

# returns the items from "orange" (-4) to, but NOT including "mango" (-1):
print(thisList[-4:-1])

# To determine if a specified item is present in a list use the in keyword:
if "apple" in thisList:
    print("yes,here have an apple")

changeItem = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# Change Item Value
"""
changeItem[1] = "watermelon"
print(changeItem)
"""

changeItem[2:5] = ["strawberry", "blueberry"]
print(changeItem)

# The insert() method inserts an item at the specified index:
changeItem.insert(1, "haha")
print(changeItem)

# Change the second and third value by replacing it with one value:
changeItem[1:3] = ["watermelon"]
print(changeItem)

# Using the append() method to append an item:
thisList.append("orange")
print(thisList)

# o append elements from another list to the current list, use the extend() method：
thisList.extend(changeItem)
print(thisList)

thistuple = ("kiwi", "orange")
thisList.extend(thistuple)
print(thisList)

thisList.remove("kiwi")
print(thisList)

# The pop() method removes the specified index.
thisList.pop(0)
print(thisList)

# Remove the last item:
thisList.pop()
print(thisList)

# The del keyword also removes the specified index:
del thisList[0]
print(thisList)

# The del keyword can also delete the list completely.
# del thisList

# The clear() method empties the list. The list still remains, but it has no content.
# thisList.clear()
# print(thisList)

# Print all items by referring to their index number:
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

# With list comprehension you can do all that with only one line of code:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)



