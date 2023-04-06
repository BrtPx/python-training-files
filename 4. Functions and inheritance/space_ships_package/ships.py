class GreatShips:  # package class to be imported

    power = "energy"

    def __init__(self, name, origin, franchise, special):

        self.name = name
        self.origin = origin
        self.franchise = franchise
        self.special = special

    @classmethod
    def propulsion(cls):
        return f"{cls.power} propulsion system"
