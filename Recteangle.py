class Rectangle:
    def __init__(self):
        print("Inside init of Rectangle")
        
    def area(self,x,y):
        return x*y

class Square(Rectangle):
    def __init__(self):
        print("Inside init of Square")

    #method overriding
    def area(self,x):
        return Rectangle.area(self,x,x)
r = Rectangle()
sq = Square()
area = sq.area(5)
print(area)
