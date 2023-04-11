class Tab:
    menu = {
        "Breakfast Croissant": 750.00,
        "French Toast": 790.00,
        "Eggs & Toast": 600.00,
        "Chickern Schnitzel": 1390.00,
        "Salmon Fillet": 2450.00,
        "Lasagna Bolognese": 1390.00,
        "Fish and Chips": 1390.00,
        "Chicken Tikka Skewers": 1390.00,
        "Slow Cooked BBQ Beef": 1390.00,
        "Cheese Burger": 1290.00,
        "Texas Burger": 1390.00,
        "Classic Beef Burger": 1190.00,
        "Barbecue Wings": 990.00,
        "BBQ Chicken in Rustic Ciabatta Sandwich": 990.00,
        "Beef Steak Sandwich": 990.00,
        "Spicy Chicken Sandwich": 990.00,
        "Smoked Salmon Bagel": 990.00,
        "Smoked Beef Pastrami in Farm Bread Sandwich": 990.00,
        "Chicken Ceasar Salad": 1290.00,
        "Greek Salad": 890.00,
        "Nicoise Salad": 1090.00,
        "Cobb Salad": 1290.00,
        "Seafood Pizza": 1890.00,
        "All Veggie Pizza": 1390.00,
        "Hawaiian Pizza": 1290.00,
        "Pollo Pizza": 1390.00,
        "Diavola Pizza": 1390.00,
        "Spicy Chicken Tikka Pizza": 1390.00,
        "Spaghetti Meatballs": 1290.00,
        "Mushroom Penne Pasta": 1290.00,
        "Prawns Tagliatelle": 1690.00,
    }

    def __init__(self):  # constructor
        self.total = 0  # sum cost orders (value)
        self.orders = []  # list of meals (key)

    def add(self, order):  # add specific meals to a list
        self.orders.append(order)  # add each order to orders
        self.total += self.menu[order]  #
        print(self.total)

    def charges(self, tips, service):
        tips = tips / 100 * self.total
        service = service / 100 * self.total
        total = tips + service + self.total

        for order in self.orders:
            print(f"{order} KES {self.menu[order]}")

        print(f"{'Total'} KES {total:.2f}")
