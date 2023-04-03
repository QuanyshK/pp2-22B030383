class string:
    def getstring(self):
        self.a = input()
    def printstring(self):
        print(self.a.upper())
str = string()
str.getstring()
str.printstring()
#
class shape():
    def __init__(self) -> None:
        pass
    def area(self):
        return 0
class square():
    def __init__(self, length = 0):
        shape.__init__(self)
        self.length = length
    def area(self):
        return self.length * self.length
x = int(input())
s = square(x)
print(s.area())
print(s.area())
#
class shape():
    def __init__(self):
        pass
    def area(self):
        return 0
class rectangle():
    def __init__(self, length, width):
        shape.__init__(self)
        self.length = length
        self.width = width 
    def area(self):
        return self.length * self.width
x = int(input())
c = int(input())
s = rectangle(x, c)
print(s.area()) 
#
class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return self.x, self.y

    def move(self):
        a = input()
        b = input()
        self.x += int(a)
        self.y += int(b)
        return self.x, self.y

    def dist(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx ** 2 + dy ** 2) ** 0.5


x1 = input()
y1 = input()
x2 = input()
y2 = input()
point1 = point(int(x1), int(y1))
point2 = point(int(x2), int(y2))
print(point1.dist(point2))
print(point1.move())
print(point1.show())
#
class bank:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self):
        a = input()
        self.deposit = int(a)
        self.balance += self.deposit

    def withdraw(self, withdraw):
        self.withdraw = withdraw
        if self.balance >= self.withdraw:
            self.balance = self.balance - self.withdraw
        else:
            print("Sorry, u dont have any money")
    def account(self):
        return self.owner, self.balance


name = input()
money = input()
human = bank(str(name), int(money))
print(human.account())
human.deposit()
human.withdraw(200)
print(human.account())



