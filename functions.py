# Built in functions
y = max(34, 56, 70, 18)
print(y)

y = min(34, 56, 70, 18)
print(y)

y = (34, 56, 70, 18)
print(y)

z = pow(2, 3)
print(z)


#User-defined functions
def greeting():
     print("Hello")
greeting() #calling a function

def multiply():
    a = 12
    b = 10
    print(a * b)
multiply()

#parameter/ viariable  and arguments/value
def add(x, y):
    print(x + y)
add(4, 5)
add(60, 50)



def employee(fullname,age,position, status):
    print(fullname,age,position,status)
employee( "Cathy Kathomi", 23, "Senior Dev","Married")

employee( "John Doe", 21, "CEO", "Single")

employee( "yao Zhiming", 32, "","Married")

employee( "Harley Kathomi", 23, "Senior Dev","Married")


