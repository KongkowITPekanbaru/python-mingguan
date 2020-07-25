# hello world

print("hello world")

# variable assignment

a = 1
b = 2
c = a + b

print(c)

# control flow

# if-else clause
if b > a:
    print(c)
else:
    print(a)

# if-elif-else clause

if b > a:
    print(c)
elif a > b:
    print(a)
else:
    print("none")

# loop

# for loop

for i in range(10):
    print(i)

# while loop

i = 0
while i < 10:
    print(i)
    i += 1

# function

def hello():
    print("world")

hello()

def add(a, b):
    return a + b

print(add(a, b))

# class
class Hello:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return self.name

a = Hello("world")
print(a.greet())
