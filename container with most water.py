h = int(input(""))
height = list(map(int, str(h)))
max1 = max(height)
max1_index = height.index(max1)
height.remove(max1)
max2 = max(height)
max2_index = height.index(max2)
if max1 >= max2:
   MAX = max2
else:
   MAX = max1
area = MAX * MAX
print(area)