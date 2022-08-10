#Testing if little_string contains in big_string and if yes it will return boolean value
def contains(big_string, little_string):
  if little_string in big_string:
    return True
  return False

#function will return one common letter comparing both strings and append it to list
def common_letters(string_one, string_two):
    common_letter = []
    for letter in string_one:
      if letter in string_two and not letter in common_letter:
        common_letter.append(letter)
    return common_letter

      
  
#common_letters("banana", "cream") #returns ['a']
#common_letters('manhattan', 'san francisco') # returns ['a', 'n']
