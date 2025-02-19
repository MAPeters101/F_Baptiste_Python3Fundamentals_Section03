a = 10
b = 3
print(a/b)
print(a//b)
print()
print(-12/5)
print(-12//5)
print()
print(10%3)
print(4%2)
print(5%2)
print(13567%2)
print()
print(165/60)
print(165 - (2*60))
print(165//60)
print(165- (165//60 * 60))
print(165%60)
print()
elapsed_minutes = 165
hours = elapsed_minutes // 60
remaining_minutes = elapsed_minutes % 60
print(f"{elapsed_minutes} minutes = {hours} hours and {remaining_minutes} minutes.")

elapsed_minutes = 485
hours = elapsed_minutes // 60
remaining_minutes = elapsed_minutes % 60
print(f"{elapsed_minutes} minutes = {hours} hours and {remaining_minutes} minutes.")

elapsed_minutes = 10485
hours = elapsed_minutes // 60
remaining_minutes = elapsed_minutes % 60
print(f"{elapsed_minutes} minutes = {hours} hours and {remaining_minutes} minutes.")

print('-'*80)

total = 0
for i in range(1, 1_001):
    total += i
    print(f'total = {total}...')
print(f'Final total = {total}...')
print()

total = 0
for i in range(1, 1_001):
    total += i
    if i%100 == 0:
        print(f'total = {total}...')
print(f'Final total = {total}...')

