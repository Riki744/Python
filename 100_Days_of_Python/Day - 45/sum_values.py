#Write a function named sum_values that takes a dictionary named my_dictionary as a parameter. The function should return the sum of the values of the dictionary

def sum_values(my_dictionary):
  counter = 0
  for value in my_dictionary.values():
    counter += value
  return counter
