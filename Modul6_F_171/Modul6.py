class MhsTIF(object):
    """Class MhsTIF yang dibangun dari class Mahasiswa"""

    def __init__(self,nama,NIM,kota,us):
        """Metode inisialisasi ini menutupimetode inisiasi di class Manusia."""
        self.nama=nama
        self.NIM=NIM
        self.kotaTinggal=kota
        self.uang=us
    def __str__(self):
        s = self.nama + " " + str(self.NIM) + " " + self.kotaTinggal + " " + str(self.uang)
        return s
    def ambilNama(self):
        return self.nama
    def ambilNim(self):
        return self.nim
    def ambilUangSaku(self):
        return self.uang

c0 = MhsTIF('Ika', 10, 'sukoharjo', 240000)
c1 = MhsTIF('Budi', 51, 'sragen', 230000)
c2 = MhsTIF('Ahmad', 2, 'surakarta', 250000)
c3 = MhsTIF('Chandra', 18, 'surakarta', 235000)
c4 = MhsTIF('Eka', 4, 'boyolali', 240000)
c5 = MhsTIF('Fandi', 31, 'salatiga', 250000)
c6 = MhsTIF('Deni', 13, 'klaten', 245000)
c7 = MhsTIF('Galuh', 5, 'wonogiri', 245000)
c8 = MhsTIF('Janto', 23, 'klaten', 245000)
c9 = MhsTIF('Hasan', 64, 'karanganyar', 270000)
c10 = MhsTIF('Khalid', 29, 'purwadadi', 265000)


Daftar = [c0, c1, c2, c3, c4, c5, c6 ,c7 , c8, c9, c10]


        
def mergeSort(A):
    #print("Membelah      ",A)
    if len(A) > 1:
        mid = len(A) // 2
        separuhkiri = A[:mid]
        separuhkanan = A[mid:]

        mergeSort(separuhkiri)
        mergeSort(separuhkanan)

        i = 0;j=0;k=0
        while i < len(separuhkiri) and j < len(separuhkanan):
            if separuhkiri[i] < separuhkanan[j]:
                A[k] = separuhkiri[i]
                i = i + 1
            else:
                A[k] = separuhkanan[j]
                j = j + 1
            k=k+1

        while i < len(separuhkiri):
            A[k] = separuhkiri[i]
            i = i + 1
            k=k+1

        while j < len(separuhkanan):
            A[k] = separuhkanan[j]
            j = j + 1
            k=k+1
    #print("Menggabungkan",A)

def quickSort(A):
    quickSortBantu (A, 0, len(A)-1)

def quickSortBantu(A, awal, akhir):
    if awal < akhir:
        titikBelah = partisi(A, awal, akhir)
        quickSortBantu(A, awal, titikBelah-1)
        quickSortBantu(A, titikBelah+1, akhir)

def partisi(A, awal, akhir):
    nilaipivot = A[awal]

    penandakiri = awal + 1
    penandakanan = akhir

    selesai = False
    while not selesai:

        while penandakiri <= penandakanan and A[penandakiri] <= nilaipivot:
            penandakiri = penandakiri + 1

        while penandakanan >= penandakiri and A[penandakanan] >= nilaipivot:
            penandakanan = penandakanan - 1

        if penandakanan < penandakiri:
            selesai = True
        else:
            temp = A[penandakiri]
            A[penandakiri] = A[penandakanan]
            A[penandakanan] = temp

    temp = A[awal]
    A[awal] = A[penandakanan]
    A[penandakanan] = temp

    return penandakanan
