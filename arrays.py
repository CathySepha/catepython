#Arrays

courses = ["MIT","Datascience","Cybersecurity"]
print(courses[1])

#looping through an array
for y in courses:
    print( "Course is",y)


#Adding a new element
courses.append("Python")
print(courses)

#Deleting  element
courses.remove("Python")
print(courses)