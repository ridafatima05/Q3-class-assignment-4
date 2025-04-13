#DICTIONARY METHOD PRACTICE

"""
1. Create and Access Dictionaries
o Create a dictionary called student with these key-value pairs:
 "name": "John"
 "age": 20
 "grade": "A"
 "courses": ["Math", "Science", "History"]
o Print the student's name
o Print the list of courses
o Add a new key-value pair: "email": "john@example.com"
o Print the entire dictionary
"""

student = {
    "name": "Rida Fatima",
    "age" : 18,
    "grade": "A",
    "courses" : ["Math", "Chemistry", "Physics"]

}
print("Name:", student["name"])

# Print the list of courses
print("Courses:", student["courses"])

# Add a new key-value pair
student["email"] = "rida@example.com"

# Print the entire dictionary
print("Full Student Dictionary:", student)
 
"""
2. Modify Dictionary Values
o Change the student's age to 21
o Add a new course "Computer Science" to the courses list
o Update the grade to "A+"
o Print the modified dictionary"""

student["age"] = 21
student["courses"] = "Computer Science"
student["grade"] = "A+"
print(f"Modified List: {student}")


"""
. Dictionary Operations
o Create a second dictionary student_address with these key-value pairs:
 "street": "123 College Ave"
 "city": "New York"
 "zip": "10001"
o Combine both dictionaries into a new dictionary called student_info
o Remove the "zip" key from student_info
o Check if "phone" exists in the dictionary
o Print the final dictionary"""

student_address = {

  "street": "123 College Ave",
  "city": "New York",
  "zip": "10001"
}

# Combine dictionaries 
student_info = student.copy()
student_info.update(student_address)

# Remove the "zip" key
student_info.pop("zip", None)

# Check if "phone" exists
has_phone = "phone" in student_info
print("Phone exists?", has_phone)

# Print final dictionary
print("Final Student Info Dictionary:", student_info)

"""
4. Dictionary Methods
o Create a dictionary word_count with these key-value pairs:
 "hello": 5
 "world": 10
 "python": 15
o Get all keys and print them as a list
o Get all values and print them as a list
o Get all key-value pairs and print them
o Make a copy of the dictionary
o Clear the original dictionary
o Print both dictionaries to verify one is empty and one is a copy
"""

# Create the dictionary
word_count = {
    "hello": 5,
    "world": 10,
    "python": 15
}

# Get all keys and print them as a list
keys = list(word_count.keys()) #key()
print("Keys:", keys)

# Get all values and print them as a list
values = list(word_count.values()) #value()
print("Values:", values)

# Get all key-value pairs and print them  #.item()
items = list(word_count.items())
print("Key-Value Pairs:", items)

# Make a copy of the dictionary
word_count_copy = word_count.copy()

# Clear the original dictionary
word_count.clear()

# Print both dictionaries to verify one is empty and one is a copy
print("Original Dictionary (after clearing):", word_count)
print("Copied Dictionary:", word_count_copy)
