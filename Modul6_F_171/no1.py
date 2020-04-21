from Modul6 import *

def convert(arr, obj):
    hasil=[]
    for x in range (len(arr)):
        for i in range (len(arr)):
            if arr[x] == obj[i].NIM:
                hasil.append(obj[i])
    return hasil

def printMerge(arr):
    print("hasil merge sort")
    NIM = []
    for i in arr:
        NIM.append(i.NIM)
    mergeSort(NIM)
    for x in convert(NIM, arr):         
        print(x.NIM) 
        
        

def printQuick(arr):
    print("hasil quick sort")
    A = []
    for x in Daftar:
        A.append(x.NIM)

    quickSort(A)
    for x in convert(A, Daftar):
        print (x.NIM)
printQuick(Daftar)
printMerge(Daftar)

