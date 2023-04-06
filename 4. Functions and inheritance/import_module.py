import sys

sys.path.insert(0, "/Users/brpx/Documents/Python/5. Problem solving")

from classes import Planet

saturn = Planet(
    "Saturn", "Planetary rings", "10.44 m/s\u00b2", "Solar System", "Milky Way"
)
print("\n")
print(f"Name is: {saturn.name}")
print(f"Main feature is: {saturn.features}")
print(f"Gravity is: {saturn.gravity}")
print(f"System is: {saturn.system}")
print(saturn.orbit())
print(f"The planet is: {saturn.shape}")
print(f"{saturn.commons()} because of gravity")
print(f"{saturn.name} {saturn.spin('36,840 km/h')}")
