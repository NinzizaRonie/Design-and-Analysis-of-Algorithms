#Number 2

""" Z = (20,35,45,10,40,60).
 Write the INSERTION-SORT procedure to sort array Z above into
ascending order
"""



z1 = [20,35,45,10,40,60]
print(len(z1))

def insertion_sort(list):
 x=1
 while x < len(list):
  c = list[x]

  y = x-1
  while y >= 0 and list[y] > c:
   list[y+1] = list[y]

   y -= 1

 list[y+1] = c
 x += 1
 print(list)

insertion_sort(z1)