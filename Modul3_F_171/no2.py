#no2

#a. membuat matriks berisi 0 dengan ukuran tertentu
def buatNol(n,m=None):
    if(m==None):
        m=n
    print("membuat matriks 0 dengan ordo "+str(n)+"x"+str(m))
    print([[0 for j in range(m)] for i in range(n)])


#b. membuat matriks identitas dengan ukuran tertentu
def buatIden(n):
    print("membuat matriks identitas dengan ordo "+str(n)+"x"+str(n))
    print([[1 if j==i else 0 for j in range(n)] for i in range(n)])


buatNol(2,3)
buatNol(4)

buatIden(3)
buatIden(4)
