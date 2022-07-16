last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ["physics", "calcus", "poetry", "history"]
grades = [98, 97, 85, 88]
gradebook = [["physics", 98], ["calcus", 97], ["poetry", 85], ["history", 88]]


#new subject with grade came in
gradebook.append(["computer science", 100])

#another new subject with grade came in
gradebook.append(["visual arts", 93])


#mistake made by grade on visual arts
gradebook[-1][-1] = 97


#changing poetry class from number to pass/fail
gradebook[2].remove(85)
gradebook[2].append("Pass")

#combining both semester gradebooks
full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)
