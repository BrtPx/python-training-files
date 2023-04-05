"""30if statements """
age = int(input("Tell me your age: "))

if age < 10:
    print("that wasn't so hard!")
elif age < 40:
    print("maybe you should keep that to yourself")
else:
    print("how are you even alive?!")

menu = input("Do you eat meat? (Y/N): ")
if menu == "y" or "Y":
    print("This is meat lovers menu")
else:
    print("This is the veggie menu")
