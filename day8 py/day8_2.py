import math
def paint_calc(height, width, cover):
          area = height * width
          number_of_cans = math.ceil(area / cover) #ceil for roundup
          print(f"You will need {number_of_cans} of paint.")

test_h = int(input("Height of the wall is: "))
test_w = int(input("Width of the wall is: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)