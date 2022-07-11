from drone_art import drone_logo
from ground_shipping_art import ground_shipping_logo


weight = float(input("What's the weight (lb) for your package? "))
customer_choice = input("What shipping method would you like to choose? type 'g' for Ground shipping and type 'd' for Drone Shipping: ")

"""Ground Shipping"""
if customer_choice == 'g':
  print(ground_shipping_logo)
  if weight <= 2:
    print("cost is 1.50$ per pound + flat charge 20$")
    total = round(weight * 1.50 + 20)
    print(f"Total cost is ${total}")
  elif weight <= 6:
    print("cost is 3.00$ per pound")
    total = round(weight * 3 + 20)
    print(f"Total cost is ${total}")
  elif weight <= 10:
    print("cost is 4.00$ per pound")
    total = round(weight * 4 + 20)
    print(f"Total cost is ${total}")
  else:
    print("cost is 4.75$ per pound")
    total = round(weight * 4.75 + 20)
    print(f"Total cost is ${total}")

"""Drone Shipping"""
if customer_choice == 'd':
  print(drone_logo)
  if weight <= 2:
      print("cost is 4.50$ per pound")
      total = round(weight * 4.50)
      print(f"Total cost is ${total}")
  elif weight <= 6:
    print("cost is 9.00$ per pound")
    total = round(weight * 9)
    print(f"Total cost is ${total}")
  elif weight <= 10:
    print("cost is 12.00$ per pound")
    total = round(weight * 12)
    print(f"Total cost is ${total}")
  else:
    print("cost is 14.25$ per pound")
    total = round(weight * 14.25)
    print(f"Total cost is ${total}")
