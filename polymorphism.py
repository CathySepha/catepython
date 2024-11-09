class Rectangle:
    def shape(self): #behaviour
        print("Drawing a Rectangle")

class Rhombus:
    def shape(self):
        print("Drawing a Rhombus")

class Parallelogram:
    def shape(self):
        print("Drawing a Parallelogram")

#same classes having the same method but different implementation

#creating objects

r = Rectangle()
r.shape()

rhom = Rhombus()
rhom.shape()

p = Parallelogram()
p.shape()
