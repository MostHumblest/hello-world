import pizza

pizza.make_pizza(16, "pepperoni")
pizza.make_pizza(12, "mushrooms", "green peppers", "extra cheese")

from pizza import make_pizza as mp
mp(14, "extra cheese")