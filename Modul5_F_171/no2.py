from Modul5 import *

A = [1,3,5,7,9]
B = [4,6,8,1]

def gabungKan(list1, list2):
    C = list1 + list2
    insertionSort(C)
    return C

print(gabungKan(A, B))
