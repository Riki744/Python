inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

#check how many items in inventory
inventory_len = len(inventory)
print(inventory_len)

#select first item from a list
first = inventory[0]
print(first)

#last item
last = inventory[-1]
print(last)

#some of items from inventory
inventory_2_6 = inventory[2:6]
print(inventory_2_6)

#first three items from list
first_3 = inventory[:3]
print(first_3)

#check how many twin beds we have
twin_beds = inventory.count("twin bed")
print(twin_beds)

#remove 5h item from a inventory
removed_item = inventory.pop(4)
print(removed_item)

#add new item
inventory.insert(10, "19th Century Bed Frame")
print(inventory)

#sort inventory
print(inventory.sort())
