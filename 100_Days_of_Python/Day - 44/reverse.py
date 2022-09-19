#Write a function named reverse_string that has a string named word as a parameter. The function should return word in reverse.

def reverse_string(word):
  reverse_string = ""
  for i in reversed(range(len(word))):
    reverse_string += word[i]
  return reverse_string


# Uncomment these function calls to test your  function:
#print(reverse_string("Codecademy"))
# should print ymedacedoC
#print(reverse_string("Hello world!"))
# should print !dlrow olleH
#print(reverse_string("test"))
# should print tset
