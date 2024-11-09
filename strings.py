from datatypes import greeting
from variables import lastname

text = "Hello World"
course = "WEB DEVELOPMENT"
print(text)


#accessing an element in a string
print(text[0])
print(text[1])

# determining the size/length of a string
print(len(text))

#modyfing a string
print(course.lower())
print(text.upper())

#string concatenation - joining strings
greeting = "Hello there"
firstname = "Cathy "
lastname = " Sephadine "

print(greeting + " " + firstname)
print(greeting + " " + firstname +" " + lastname)

