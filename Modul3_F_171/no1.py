#no1

#a. mengecek isi matriks
def cek(n):
    x = len(n[0])
    y = type(n[0][0])
    z = 0
    a = True
    for i in range (len(n)):
        for j in range (len(n[i])):
            #mengecek apakah matris mempunyai isi yg bertipe sama
            c = type(n[i][j])
            if (c!=y):
                a = False
                break
        #mengecek apakah matriks mempunyai ukuran yg sama
        if (len(n[i]) == x):
            z+=1
        
    if(z == len(n) and a==True):
        print("isi matriks bertipe sama dan ukuran matriks konsisten")
    else:
        print("isi matriks bertipe tidak sama dan ukuran matrik tidak konsisten")


#b. mengecek ukuran matriks
def ordo(n):
    x,y = 0,0
    for i in range(len(n)):
        x+=1
        y = len(n[i])
    print("mempunyai ordo "+str(x)+"x"+str(y))


#c. menambahkan 2 matriks yg ukuran sama
def tambah(n,m):
    x,y = 0,0
    for i in range(len(n)):
        x+=1
        y = len(n[i])
    xy = [[0 for j in range(x)] for i in range(y)]
    
    z = 0
    if(len(n)==len(m)):
        for i in range(len(n)):
            if(len(n[i]) == len(m[i])):
                z+=1
    if(z==len(n) and z==len(m)):
        print("ukuran sama")
        for i in range(len(n)):
            for j in range(len(n[i])):
                xy[i][j] = n[i][j] + m[i][j]
        print(xy)
    else:
        print("ukuran beda")


#c. mengalikan 2 matriks yg ukuran sama   
def kali(n,m):
    aa = 0
    x,y = 0,0
    for i in range(len(n)):
        x+=1
        y = len(n[i])
    v,w = 0,0
    for i in range(len(m)):
        v+=1
        w = len(m[i])
        
    if(y==v):
        print("bisa dikalikan")
        hasilKali = [[0 for j in range(w)] for i in range(x)]
        for i in range(len(n)):
            for j in range(len(m[0])):
                for k in range(len(m)):
                    #print(n[i][k], m[k][j])
                    hasilKali[i][j] += n[i][k] * m[k][j]
        print(hasilKali)
            
    else:
        print("tidak memenuhi syarat")


#d. menghitung determinan dari matriks
def determHitung(A, total=0):
    x = len(A[0])
    z = 0
    for i in range(len(A)):
        if (len(A[i]) == x):
           z+=1
    if(z == len(A)):
        if(x==len(A)):
            indices = list(range(len(A)))
            if len(A) == 2 and len(A[0]) == 2:
                val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
                return val
            for fc in indices: 
                As = A 
                As = As[1:] 
                height = len(As) 
                for i in range(height): 
                    As[i] = As[i][0:fc] + As[i][fc+1:] 
                sign = (-1) ** (fc % 2) 
                sub_det = determHitung(As)
                total += sign * A[0][fc] * sub_det
        else:
            return "tidak bisa dihitung determinan, bukan matrix bujursangkar"
    else:
        return "tidak bisa dihitung determinan, bukan matrix bujursangkar"
    return total

a = [[1,2],[3,4]]
b = [[5,6],[7,8]]
c = [[12,3,"y"],[12,33,4]]
d = [[3,4],[2,4],[1,5]]
e = [[5,6,7],[7,8,9]]
x = [[1,2,1],[3,3,1],[2,1,2]]
v = [[1,-2,0,0],
     [3,2,-3,1],
     [4,0,5,1],
     [2,3,-1,4]]

print('cek konsisten matriks')
cek(a)
cek(b)
cek(c)
cek(d)
cek(e)
cek(x)
cek(v)

print("""
menghitung jumlah ordo matriks""")
ordo(a)
ordo(b)
ordo(c)
ordo(d)
ordo(e)
ordo(x)
ordo(v)

print("""
menambahkan jumlah 2 matriks""")
tambah(a,b)
tambah(a,d)

print("""
mengalikan 2 matriks""")
kali(a,b)
kali(a,e)

print("""
menghitung determinan matriks""")
print(determHitung(a))
print(determHitung(b))
print(determHitung(c))
print(determHitung(d))
print(determHitung(e))
print(determHitung(x))
print(determHitung(v))
