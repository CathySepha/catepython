number = 76 #intefer
second = 45.90 #float
greeting = "Hello there" #string
ispythoninteresting = True #boolean

print(number)
print(second)
print(greeting)
print(ispythoninteresting)

#Data Structures- Multiple values stored in a single variable

cars = ["toyota","audi","mazda"] #List, elements come out in an ordered manner when printed out , and are also changeable
print(cars)

fruits = ("banana","apple","mango") #Tuple- it is ordered but unchangeable
print(fruits)

countries = {"kenya","rwanda","SA"} #Set  elements are unordered
print(countries)


student = {
    "firstname" : "John",
    "age" : 23 ,
    "course" : "Python",
    "gender" : "M"
} # Dictionary Key value pair
print(student)
print(student["firstname"])


#Determining Data Types
print( type(countries))
print( type(student))
print(type(cars))

#Typecasting process of converting one datatype to another

print(float(number))
print(int(second))