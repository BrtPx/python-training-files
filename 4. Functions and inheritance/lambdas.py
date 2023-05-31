# anonymous inline functions called once using both maps and filter functions


nums = [1, 2, 3, 4, 5, 6]


def square(n):
    return n * n


print(list(map(square, nums)))


# using lambda
print(list(map(lambda n: n * n, nums)))
