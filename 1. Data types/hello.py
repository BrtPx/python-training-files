"""Simple Hello world and area of circle calculator"""

name = input("First Name: ")
sign = input("...and your call-sign ")
print(name)
print(name, "call-sign", sign)


r = input("Provide radius: ")
area = 3.142 * int(r) ** 2
print(area)
