num = [25, 2, 6, 4, 9, 7, 3, 44, 9, 8, 6, 4, 1, 2, 26, 7, 8]  # define list

# set remove duplicates but do not order list on strings
names = [
    "adam",
    "jason",
    "david",
    "jack",
    "zeek",
    "brian",
    "liam",
    "zeek",
    "jason",
    "brian",
    "liam",
]


print(set(num))
print(set(names))


def life(dicts):
    life_colors = list(dicts.values())
    print(dicts)
    print(life_colors)
    for colour in set(life_colors):
        nums = life_colors.count(colour)
        print(f"There are {nums} {colour} around you")


natural = {}

while True:
    nature = input("name any object in nature: ")
    color = input("give the object's color: ")
    natural[nature] = color  # assign key:values to dictionary

    another = input("add another object: ")
    if another == "y":
        continue
    break

life(natural)
