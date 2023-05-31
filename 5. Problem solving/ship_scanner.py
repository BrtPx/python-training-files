# import class and function from space_ships_package

import sys

# sys.path.insert(
#     0, "/Users/brpx/Documents/Python/4. Functions and inheritance/space_ships_package"
# )

sys.path.insert(
    0,
    "/home/bpx/Documents/python-training-files/4. Functions and inheritance/space_ships_package",
)


from classified import ship_class
from ships import GreatShips

falcon = GreatShips(
    "Millenium Falcon", "Corellian", "Star Wars", "Fastest Ship in the Galaxy"
)

executor = GreatShips(
    "Executor", "Kuat Drive Yards", "Star Wars", "Largest super star destroyer"
)

enterprise = GreatShips(
    "USS Enterprise", "Earth", "Star Trek", "Pride of the United Federation of Planets"
)
print(f"Designation: {falcon.name}")
print(f"Origins: {falcon.origin}")
print(f"Franchise: {falcon.franchise}")
print(f"SPecial Feature: {falcon.special}")
print(f"The {falcon.name} uses nuclear {falcon.propulsion()}")
ship_class("falcon")
print("\n")

print(f"Designation: {executor.name}")
print(f"Origins: {executor.origin}")
print(f"Franchise: {executor.franchise}")
print(f"SPecial Feature: {executor.special}")
print(f"The {executor.name} uses 13 Executor-50.x engine {executor.propulsion()}")
ship_class("executor")
print("\n")

print(f"Designation: {enterprise.name}")
print(f"Origins: {enterprise.origin}")
print(f"Franchise: {enterprise.franchise}")
print(f"SPecial Feature: {enterprise.special}")
print(f"The {enterprise.name} uses a warp drive {enterprise.propulsion()}")
ship_class("enterprise")
