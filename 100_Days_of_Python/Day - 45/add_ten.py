#Create a function named add_ten that takes a dictionary with integer values named my_dictionary as a parameter. The function should add 10 to every value in my_dictionary and return my_dictionary

def add_ten(my_dictionary):
  for key in my_dictionary.keys():
    my_dictionary[key] += 10
  return my_dictionary


# Uncomment these function calls to test your  function:
#print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
#print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}
