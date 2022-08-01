def append_sum(lst):
  for i in range(len(lst)):
    lst.append(lst[-1] + lst[-2])
  return lst


#Uncomment the line below when your function is done
#print(append_sum([1, 1, 2]))
