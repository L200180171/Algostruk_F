from time import time as detak
from random import shuffle as kocok
from Modul5 import *

k = list(range(1,6001))
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw=detak();bubbleSort(u_bub);ak=detak();print('bubble sort: %g detik' %(ak-aw) );
aw=detak();selectionSort(u_bub);ak=detak();print('selection sort: %g detik' %(ak-aw) );
aw=detak();insertionSort(u_bub);ak=detak();print('insertion sort: %g detik' %(ak-aw) );


print("""
jadi menurut perhitungan waktu diatas insection sort lebih cepat \n
dilanjut kedua selection sort dan yang paling lambat bubble sort
""")
