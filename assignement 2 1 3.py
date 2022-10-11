#Number 3

def insertion_sort_descending(list):
 x=1
 while x < len(list):
  c = list[x]

  y = x-1
  while y >= 0 and list[y] < c:
   list[y+1] = list[y]

   y -= 1

 list[y+1] = c
 x += 1
 print(list)

insertion_sort_descending(z1)