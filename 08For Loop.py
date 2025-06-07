# for loop: used to interate over a sequence (String, list, tuple, set) repeat a block of code on exact amount of time. 
#           for i in range(start, end, skip)
# 
'''
for i in range(10):
    print(i)

for  i in range(1, 11):
        print(i)

for i in range(1, 11, 2):
    print(i)

for i in range(10, 0, -1):
    print(i)
'''

#--------------------------------------------------------------------#
# List: An ordered collection of items that can be modified, most flexible
fruits = ["apple", "banana", "orange"]  # Creating a list
print(fruits)  # Print whole list
print(fruits[0])  # Access first item
print(len(fruits))  # Get list length

# Basic operations
fruits.append("mango")  # Add item at end
fruits.remove("banana")  # Remove specific item

# Loop through list
for fruit in fruits:
    print(fruit)




#----------------------------------------------------------------------#
# Tuple: An ordered collection of items that cannot be modified (immutable), Faster
colors = ("red", "green", "blue")  # Creating a tuple
print(colors)  # Print whole tuple
print(colors[0])  # Access first item
print(len(colors))  # Get tuple length

# Loop through tuple
for color in colors:
    print(color)

# Note: Cannot modify tuple after creation
# colors[0] = "yellow"  # This will raise an error



#----------------------------------------------------------------------#
# Set: An unordered collection of unique items
numbers = {1, 2, 3, 4, 5}  # Creating a set
print(numbers)  # Print set
numbers.add(6)  # Add item
numbers.remove(2)  # Remove item

# Note: Sets don't maintain order and don't allow duplicates
duplicate_set = {1, 2, 2, 3, 3, 4}  # Duplicates are automatically removed
print(duplicate_set)  # Will print {1, 2, 3, 4}

# Loop through set
for number in numbers:
    print(number)


number = {1,2,3,4,5,6,7}
fruits = {'apple', 'mango', 'banana', 'orange'}

print(number)  # This will also be in random order because it's a set
print(fruits)  # Similarly random order because it's a set