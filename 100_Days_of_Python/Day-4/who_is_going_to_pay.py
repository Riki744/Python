import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

num_item = len(names)

random_choice = random.randint(0, num_item -1)
pays = names[random_choice]
print(pays + " is going to buy the meal today.")
