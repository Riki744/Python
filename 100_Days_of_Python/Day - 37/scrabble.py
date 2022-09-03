letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#combining letter to points as new dictionary
letters_to_points = {key:value for key, value in zip(letters, points)}
#print(letters_to_points)


#Adding blank space as key and value of 0
letters_to_points[" "] = 0
#print(letters_to_points)

def score_word(word):
  points_total = 0
  for letter in word:
    points_total += letters_to_points.get(letter, 0)
  return points_total

#Testing function it should be (3 + 1 + 1 + 4 + 4 + 1 + 1) = 15
brownie_points = score_word("BROWNIE")
#print(brownie_points)

#Score A Game
players_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd":["EARTH", "EYES", "MACHINE"], "Lexi Con":["ERASER", "BELLY", "HUSKY"], "Prof Reader":["ZAP", "COMA", "PERIOD"]}

player_to_points = {}

#Calculates each player words to new dictionary score table
for player, words in players_to_words.items():
  player_points = 0
  for word in words:
    value = score_word(word)
    player_to_points[player] = value

print(player_to_points)
