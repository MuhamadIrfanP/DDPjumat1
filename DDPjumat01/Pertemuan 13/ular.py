from Animal import Animal

class ular(Animal):
    def __init__(self, nama, makanan, habitat, berkembang_biak, berbisa, cara_berburu):
        super().__init__(nama, makanan, habitat, berkembang_biak)
        self.berbisa = berbisa
        self.cara_berburu = cara_berburu
        
    def info_ular(self):
        super().info_animal(),
        print("Berbisa \t\t : ", self.berbisa,
              "\nCara Berburu \t\t : ", self.cara_berburu
              )
        
piton = ular ("Piton", "Daging", "Hutan", "Melahirkan", "Tidak","Melilit Mangsa Hingga Tewas")
piton.info_ular()
print("=============================================================================")
anaconda = ular ("Anaconda", "Daging", "Hutan", "Melahirkan", "Tidak","Melilit Mangsa Hingga Tewas")
anaconda.info_ular()