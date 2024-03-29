#Task - Create a function called x_length_words that takes a string named sentence and an integer named x as parameters. This function should return True if every word in sentence has a length greater than or equal to x.


def x_length_words(sentence, x):
  letters = sentence.split(" ")
  for letter in letters:
    if len(letter) < x:
      return False
    return True
  


# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True
