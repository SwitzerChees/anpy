class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f'Point({self.x}, {self.y})'
        
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    pass

p1 = Point(1,1)
p2 = Point(2,2)

p3 = p1 + p2

print(p3)

assert p3.x != 3