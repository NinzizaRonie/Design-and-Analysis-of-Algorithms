#DIVIDE

import re


def merge_sort(arr):
    
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2

    arr_a =arr[:mid]
    arr_b =arr[mid:]

    arr_a = merge_sort(arr_a)
    arr_b = merge_sort(arr_b)

    return merge_sort(arr_a,arr_b)
    
G = [38,27,43,3,9,82,10]

print(merge_sort(G))

        
