# class of planet objects
class Planet:

    # class is a blue print of how an object should look and behave
    # class attribute
    shape = "round"

    def __init__(
        self, name, features, gravity, system, galaxy
    ):  # init/constructor function

        # self.name = "centauri"
        # self.features = "Size"
        # self.gravity = "24.79 m/s\u00b2"
        # self.system = "Solar System"
        # self.galaxy = "Milky Way"

        # instance attributes/properties
        # attributes are different for each instance
        self.name = name
        self.features = features
        self.gravity = gravity
        self.system = system
        self.galaxy = galaxy

    # instance methods.
    def orbit(self):
        return (
            f"{self.name} is in the {self.system} located in the {self.galaxy} Galaxy"
        )

    @classmethod
    def commons(cls):
        return f"All planets are {cls.shape}"

    # static methods have no access to class and instance methods.
    # Attributes and methods have to be explicitly defined
    @staticmethod
    def spin(speed="2000 m/s\u00b2"):
        return f"spins and spins at {speed}"


jupiter = Planet(
    "Jupiter", "Size", "24.79 m/s\u00b2", "Solar System", "Milky Way"
)  # new instance of planet
print(f"Name is: {jupiter.name}")
print(f"Main feature is: {jupiter.features}")
print(f"Gravity is: {jupiter.gravity}")
print(f"System is: {jupiter.system}")
print(jupiter.orbit())
print(f"The planet is: {jupiter.shape}")
print(f"{jupiter.commons()} because of gravity")
# print(Planet.orbit())
print(f"{jupiter.name} {jupiter.spin('45,583 km/h')}")
print("\n")

centauri = Planet(
    "Proxima Centauri b", "Closest", "8.50 m/s\u00b2", "Binary Sytem", "Milky Way"
)
print(f"Name is: {centauri.name}")
print(f"Main feature is: {centauri.features}")
print(f"Gravity is: {centauri.gravity}")
print(f"System is: {centauri.system}")
print(centauri.orbit())
print(f"The planet is: {centauri.shape}")
print(f"{centauri.commons()} because of gravity")
# print(Planet.orbit())
print(f"{centauri.name} {centauri.spin('< 0.1km/s')}")


# instance attributes and methods = only accessible to instance attributes and instance methods
# class attributes and methods = accessible to both class and instance attibutes and methods
# static attributes and methods = accessible to both class and instance attibutes and methods
