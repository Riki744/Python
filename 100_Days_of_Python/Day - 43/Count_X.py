#Task - Write a function named count_char_x that takes a string named word and a single character named x as parameters. The function should return the number of times x appears in word.

def count_char_x(word, x):
  count = 0
  for c in word:
    if c == x:
      count += 1
  return count

# Uncomment these function calls to test tip function:
#print(count_char_x("mississippi", "s"))
# should print 4
#print(count_char_x("mississippi", "m"))
# should print 1
