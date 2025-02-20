a = 10
b = 10

print(a == b)

c = 10.0
print(a == c)
print(a is c)
print()

a = 10
b = 10.0
print(a == b)
print(a is b)
print(id(a), id(b))
print()

a = 10
b = 10
print(a == b)
print(a is b)
print(id(a), id(b))
print()

a = 10_000
b = 10_000
print(a == b)
print(a is b)
print(id(a), id(b))
print()

print(10 != 12)
print(10.5 != 12.5)
print(10 >= 5)
print(10.5 < 100)
