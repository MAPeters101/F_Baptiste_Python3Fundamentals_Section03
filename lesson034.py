
print(not True)
print(not False)
print()

print(True and True)
print(True and False)
print(False and True)
print(False and False)
print()

print(True or True)
print(True or False)
print(False or True)
print(False or False)
print()
print('-'*80)


balance = 1000.00
withdrawal = 50.00
withdrawal_limit = 500.00
print((withdrawal < withdrawal_limit) and (withdrawal <= balance))
print()

balance = 1000.00
withdrawal = 600.00
withdrawal_limit = 500.00
print((withdrawal < withdrawal_limit) and (withdrawal <= balance))
print()

balance = 1000.00
withdrawal = 1200.00
withdrawal_limit = 1500.00
print((withdrawal < withdrawal_limit) and (withdrawal <= balance))
print()
print('-'*80)



a = 20
b = 10
print(a / b > 1)
print()

a = 20
b = 0
#print(a / b > 1)
print(b != 0 and a / b > 1)
print()

a = 20
b = 30
#print(a / b > 1)
print(b != 0 and a / b > 1)
print()

a = 20
b = 10
#print(a / b > 1)
print(b != 0 and a / b > 1)
print()

