lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["kelvin","karren","jim","oscar","tobby"]
friends.append("[1],""dennis")
print(friends)

for i in range(99,0,-1):
    print(i)

class point:
    pass
p1 = point()
p2 = point()
p1.x = 5
p1.y = 4

p2.x = 3
p2.y = 6
print(p1.x, p1.y)
print(p2.x, p2.y)
class point:
    def reset(self):
        self.x = 0
        self.y = 0
p = point()
p.reset()
print(p.x, p.y)
class point:
    def _init_(self, x, y):
        self.move(x, y)
def move(self, x, y):
    self.x = x
    self.y = y
def reset(self):
    self.move(0, 0)
# Constructing a point
point = point(3, 5)
print(point.x, point.y)