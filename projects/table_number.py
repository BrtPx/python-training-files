from restaurant_tab import Tab

table_one = Tab()

table_one.add("Breakfast Croissant")
table_one.add("Lasagna Bolognese")
table_one.add("Spicy Chicken Sandwich")
table_one.add("All Veggie Pizza")
table_one.charges(10, 15)

table_two = Tab()

table_two.add("Eggs & Toast")
table_two.add("Greek Salad")
table_two.charges(5, 15)


table_three = Tab()

table_three.add("Classic Beef Burger")
table_three.add("Mushroom Penne Pasta")
table_three.add("Cobb Salad")
table_three.charges(8, 15)
