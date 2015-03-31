class Square:
        side = 3    
        def __init__(self,x):
                self.side = x
        def area(self):
                return self.side * self.side


sq = Square(5)

print(Square.side)

print(Square.area(sq))
print(sq.area())
