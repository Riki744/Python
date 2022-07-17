from art import logo

print(logo)
print("Welcome to our pizza store :)")

toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

#look for $2 dollar slices
num_two_dollar_slices = prices.count(2)

#how many pizza topping we have
num_pizzas = len(toppings)
print(f"We sell {num_pizzas} different kinds of pizza!")

#toppings + prices
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
print(f"Here is our todays menu {pizza_and_prices}")
order = input("What would you like to order? : ")

#Sorting and Slicing
pizza_and_prices.sort()
#print(pizza_and_prices)

#Cheapest pizza
cheapest_pizza = pizza_and_prices[0]
#print(cheapest_pizza)

#Most expensive pizza
priciest_pizza = pizza_and_prices[-1]
#print(priciest_pizza)

#Since the pizza is bought we can remove it from the list
removed_pizza = pizza_and_prices.pop()
#print(pizza_and_prices)

#Adding new pizza
pizza_and_prices.insert(4, [2.5, "peppers"])
#print(pizza_and_prices)


#Poor customer comes in and asks for first 3 cheapest pizzas we have
three_cheapest = pizza_and_prices[:3]
#print(three_cheapest)
