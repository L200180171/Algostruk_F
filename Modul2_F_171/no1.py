class Pesan(object):
    """Sebuah class bernama Pesan.
       Untuk memahami konsep Class dan Object.
    """
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print('kalimatku mempunyai', len(self.teks), 'karakter.')
    def perbarui(self, stringBaru):
        self.teks = stringBaru
    def apakahTerkandung(self, a):
        if a in self.teks:
            return True
        else :
            return False
    def hitungKonsonan(self):
        jmlKons = 0
        x = self.teks
        alfaKon = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        for i in x:
            if i in alfaKon:
                jmlKons += 1
        return jmlKons
    def hitungVokal(self):
        jmlVoc = 0
        x = self.teks
        Vocal = "aiueoAIUEO"
        for i in x:
            if i in Vocal:
                jmlVoc += 1
        return jmlVoc
