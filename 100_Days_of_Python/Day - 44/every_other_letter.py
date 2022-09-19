#Create a function named every_other_letter that takes a string named word as a parameter. The function should return a string containing every other letter in word.

#Power of the range() function.

def every_other_letter(word):
  other_letter = ''
  for w in range(0, len(word), 2):
    other_letter += word[w]
  return other_letter

# Uncomment these function calls to test your function:
#print(every_other_letter("Codecademy"))
# should print Cdcdm
#print(every_other_letter("Hello world!"))
# should print Hlowrd
#print(every_other_letter(""))
# should print 
