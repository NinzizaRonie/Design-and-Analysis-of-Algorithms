

def merge(a,b):
    sorted_arr = []       #O(1)


    x = 0                 #O(1)
    y = 0

    len_a = len(a)
    len_b = len(b)        # O(1)


    while x < len_a and y < len_b:  #O(n)

        if a[x] <= b[y]:
          sorted_arr.append(a[x])
          x+=1

        else:
            sorted_arr.append(b[y])
            y+=1 
    while x < len_a:                #O(n)
        sorted_arr.append(a[x]) 
        x+=1 

    while y < len_b:                #O(n)
        sorted_arr.append(b[y]) 
        y+=1        

    return sorted_arr           #O(1)

A = [2,100,1000]
B = [1,699,1000000,1000001]
C = [99,300,501,10003]
D = [99,300]


print(merge(A,B))
print(merge(C,D))





           

        

         
           


           

