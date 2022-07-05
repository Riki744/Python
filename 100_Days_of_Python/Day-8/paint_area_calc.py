import math

def paint_calc(height, width, cover):
  area = height * width
  total = math.ceil(area / cover) #round number
  print(f"You'll need {total} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
