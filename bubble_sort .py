list=[2,7,9,4,1]
print(sorted(list))
name=['ronie','bellz','noella']
print(sorted(name))

def bubble_sort(array):
    a=len(array)
    for i in range(a):
        sort_status=True
        for j in range ((a)-i-1):
           if array[j]>array[j+1]:
               array[j],array[j+1]=array[j+1],array[j]
               sort_status=False
        if sort_status:
             break           
             
    return array 
array=[1,2,3,4]
array=[3,5,8,4,1,2]
print(bubble_sort(array))