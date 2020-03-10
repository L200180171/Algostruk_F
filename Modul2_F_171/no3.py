class Manusia(object):
    """class 'Manusia' dengan inisiasi 'nama'"""
    keadaan = "lapar"
    def __init__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print("Salam, namaku ",self.nama)
    def makan(self, s):
        print("Saya baru saja makan ", s)
        self.keadaan = 'kenyang'
    def olahraga(self, k):
        print("Saya baru saja latihan ", k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self, n):
        return n * 2


class Mahasiswa(Manusia):
    def __init__ (self,nama,NIM,kota,us):
        self.nama = nama
        self.NIM = NIM
        self.kota = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', NIM '+ str(self.NIM)\
            +', tinggal di '+ self.kota \
            +', uang saku '+ str(self.uangSaku)\
            +', tiap bylannya'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangS(self):
        return self.uangSaku
    def Makan(self, s):
        print("saya baru saja makan ", s," sambil belajar")
        self.keadaan = 'kenyang'

#no3       
print("Silahkan melengkapi data berikut")
a = input ('Masukkan nama      : ')
b = int(input ('Masukkan NIM       : '))
c = input ('Masukkan Kota      : ')
d = int(input ('Masukkan Uang Saku : '))

maha = Mahasiswa(a,b,c,d)
