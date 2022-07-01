import random

print("Welcome to a virtual coin toss game")
toss = input("Please toss a coin now - 'Write toss' ")

# print(type(toss))

coin = ["Heads", "Tails"]

random_numb = random.randint(0, 1)

if toss == "toss":
  if random_numb == 1:
    print(coin[0])
  else:
    print(coin[1])
else:
  print("Please don't break my game and just toss the coin")
