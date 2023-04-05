def greet():
    print("Hello world")


def calc(length, width, height):

    area = length * width

    vol = area * height

    print(f"The area is {area} and the volume is {vol}")


l = int(input("Enter length (cm): "))
w = int(input("Enter width (cm): "))
h = int(input("Enter height (cm): "))

calc(l, w, h)
