class Hewan:
    def __init__(self, nama, umur):
        self.__nama = nama  # Private: Hanya bisa diakses dalam kelas Hewan
        self._umur = umur  # Protected: Bisa diakses dalam kelas Hewan dan kelas turunannya

    def makan(self):
        print(f"{self.__nama} sedang makan.")

    def tidur(self):
        print(f"{self.__nama} sedang tidur.")

    def get_nama(self):
        return self.__nama
    
    def set_nama(self,namabaru):
        self.__nama = namabaru

        
class Mamalia(Hewan):
    def __init__(self, nama, umur, jenis_bulu):
        super().__init__(nama, umur)
        self.jenis_bulu = jenis_bulu  # Public: Bisa diakses dari mana saja

    def menyusui(self):
        print(f"{self.get_nama()} menyusui anaknya.")

class Burung(Hewan):
    def __init__(self, nama, umur, jenis_paruh):
        super().__init__(nama, umur)
        self._jenis_paruh = jenis_paruh  # Protected: Bisa diakses dalam kelas Burung dan kelas turunannya

    def terbang(self):
        print(f"{self.get_nama()} sedang terbang kelangit ke tujuh.")

anjing = Mamalia("Rex", 3, "halus")
print(anjing.jenis_bulu)
kucing = Burung("ayu",7,"tajam")
print(kucing._jenis_paruh) 
