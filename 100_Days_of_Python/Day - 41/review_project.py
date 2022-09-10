class Student:
  #constructor
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
  
  #Method
  def add_grade(self, grade):
    if type(grade) == Grade:
      self.grades.append(grade)
    else:
      pass

  #Instances
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)


class Grade:
  #Attribute
  minimum_passing = 65
  
  
  #Constructor
  def __init__(self, score):
    self.score = score

pieter.add_grade(Grade(100))
