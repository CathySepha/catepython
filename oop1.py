from datatypes import student


class Student:
    #properties/variables/attributes/characteristics
    name = "Ryan"
    gender = "Male"
    age = 32

    #Behaviors/Method/Function
    def study(self):
        print("Student is studying")

#object 1
student1 = Student()  #Creating an object
student1.study()
print(student1.name)

#object2
student2 = Student()
student2.study()
