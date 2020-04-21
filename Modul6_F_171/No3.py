from time import time as detak
from random import shuffle as kocok
import time
from Modul5 import *
from Modul6 import *

k = list(range(1,6001))
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]
u_mrg = k[:]
u_qck = k[:]

aw=detak();bubbleSort(u_bub);ak=detak();print('bubble sort: %g detik' %(ak-aw) );
aw=detak();selectionSort(u_bub);ak=detak();print('selection sort: %g detik' %(ak-aw) );
aw=detak();insertionSort(u_ins);ak=detak();print('insertion sort: %g detik' %(ak-aw) );
aw=detak();mergeSort(u_mrg);ak=detak();print('merge sort: %g detik' %(ak-aw) );
aw=detak();quickSort(u_qck);ak=detak();print('quick sort: %g detik' %(ak-aw) );


