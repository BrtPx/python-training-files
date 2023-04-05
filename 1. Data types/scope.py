""" variable scope """
_name = "Mike"  # global scope variable


def print_name():
    global _name
    _name = "Kel"  # local scope variable
    print("Name inside function is", _name)
    return _name  # return local variable and redefine with assignment


_name = print_name()
print("Name outside function is", _name)
