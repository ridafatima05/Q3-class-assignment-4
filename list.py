#ASSIGNMENT #04

"""
 1. Create and Modify Lists
o Create a list called fruits with the items: "apple", "banana", "orange"
o Add "grape" to the end of the list using an appropriate method
o Insert "mango" at position 2 in the list
o Remove "banana" from the list
o Print the final list   """


fruits = ["apple", "banana","orange"]
print(f"Original List: {fruits}")
fruits.append("grape")
fruits.insert(2,"mango")
fruits.remove("banana")
print(f"Final List: {fruits}" )


"""
2. List Operations
o Create a list numbers with values: 10, 20, 30, 40, 50
o Create a second list more_numbers with values: 60, 70, 80
o Combine both lists into a new list called all_numbers
o Make a copy of all_numbers called numbers_copy
o Reverse the order of numbers_copy
o Print both all_numbers and numbers_copy
"""

# Original list
scores = [85, 92, 78, 65, 92, 85, 74]

# Sort in ascending order
ascending_order = sorted(scores)
print(f"Ascending Order: {ascending_order}")

# Sort in descending order
descending_order = sorted(scores, reverse=True)
print(f"Descending Order: {descending_order}")

# Count how many times 92 appears
count_92 = scores.count(92)
print(f"92 appears {count_92} times in the list.")

# Find and print highest and lowest scores
highest_score = max(scores)
lowest_score = min(scores)
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")

# Print the sorted list (ascending)
print(f"Sorted List (Ascending): {ascending_order}")


"""
4. List Manipulation
o Create a list letters with values: "a", "b", "c", "d", "e"
o Use slicing to create a new list with only the first three letters
o Use slicing to create another list with only the last two letters
o Find and print the index of "c" in the list
o Replace "d" with "z" in the original list
o Print the modified list

"""

# Original list
letters = ["a", "b", "c", "d", "e"]
print(f"Original List: {letters}")

# First three letters using slicing   
#.slice() method on list - Doesn't exist
#slice() built-in function - Used to create slice objects

first_three_letters = letters[0:3] #list slicing
print(f"First three letters: {first_three_letters}")

# Last two letters using slicing
last_two_letters = letters[-2:]
print(f"Last two letters: {last_two_letters}")

# Index of 'c'
index_c = letters.index("c")
print(f"Index of 'c': {index_c}")

# Replace 'd' with 'z'
letters[3] = "z"

print(f"Modified list: {letters}")
