from no2 import Manusia

class SiswaSMA(Manusia):
    def __init__(self, nama, NISN, uangSaku, alamat):
        self.nama = nama
        self.nisn = NISN
        self.uangSaku = uangSaku
        self.alamat = alamat
    def __str__(self):
        a = 'Nama      : ' + str(self.nama) + '\n' \
            + 'NISN      : ' + str(self.nisn) + '\n' \
            + 'Alamat    : ' + str(self.alamat) + '\n' \
            + 'Uang Saku : ' + str(self.uangSaku)
        return a
