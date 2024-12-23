from Animal import Animal

class ikan(Animal):
    def __init__(self, nama, makanan, habitat, berkembang_biak, jenis_air, cara_hidup):
        super().__init__(nama, makanan, habitat, berkembang_biak)
        self.jenis_air = jenis_air
        self.cara_hidup =  cara_hidup
      
    def info_ikan(self):
        super().info_animal(),
        print("Jenis Air \t\t : ", self.jenis_air,
              "\nCara Hidup \t\t : ", self.cara_hidup
              )
        
ikan_mas = ikan("Mas", "Pelet", "Air",  "Bertelur", "Air Tawar", "Berkoloni")
ikan_mas.info_ikan()
print("=============================================================================")
Paus = ikan("Paus", "Plankton", "Air",  "Melahirkan", "Air Laut", "Mandiri")
Paus.info_ikan()
print("=============================================================================")