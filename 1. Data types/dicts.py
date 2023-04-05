house = {
    "stark": "wolf",
    "lannister": "lion",
    "targaryen": "dragon",
}  # define dictionary
print(house)
print(house["stark"])

print("targaryen" in house)  # check value in list
print(house.keys())

print(list(house.keys()))  # typecast dict_keys into a list

vals = list(house.values())  # typecast dict_values into a list
print(vals)

print(vals.count("dragon"))  # count occurrence

house["baratheon"] = "stag"  # add entry to dictionary
print(house)

tyler = dict(
    name="rose", hair="blonde", personality="flirty"
)  # alternate of defining dictionary
print(tyler)


def artworks(dicts):
    for key, val in dicts.items():  # cycle dicts items
        print(f"The {val} is a major work of {key}")


art = {}  # dictionary

while True:
    name = input("enter name of artist: ")
    work = input("enter artist's famous works: ")

    art[name] = work
    another = input("feed me? (y/n): ")
    if another == "y":
        continue
    else:
        break

artworks(art)
print(art)
