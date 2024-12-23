from Animal import Animal

class Burung(Animal):
    def __init__(self, nama, makanan, habitat, berkembang_biak, paruh, warna_bulu):
        super().__init__(nama, makanan, habitat, berkembang_biak)
        self.paruh = paruh
        self.warna_bulu = warna_bulu
        
    def info_burung(self):
        super().info_animal(),
        print("Paruh \t\t\t : ", self.paruh,
              "\nWarna Bulu \t\t : ", self.warna_bulu)
        
beo = Burung("Beo", "Jagung", "Udara",  "Bertelur", "Bengkok", "Warna-warni")
beo.info_burung()
print("=============================================================================")
Gagak = Burung("Gagak", "Bangkai", "Udara",  "Bertelur", "Lurus", "Hitam")
Gagak.info_burung()
print("=============================================================================")