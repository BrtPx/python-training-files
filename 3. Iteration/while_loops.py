age = 37
num = 0

while num < age:
    if num == 0:
        num += 1
        continue
    if num == 16:
        num += 1
        continue
    if num % 2 == 0:
        print(num)
    num += 1
