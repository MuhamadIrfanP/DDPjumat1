#Membuat class Animal
class Animal :
    
    def __init__(self, nama, makanan, habitat, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.habitat = habitat
        self.berkembang_biak = berkembang_biak
        
    def info_animal(self):
        print("Nama \t\t\t : ", self.nama,
              "\nMakanan \t\t : ", self.makanan,
              "\nHabitat \t\t : ", self.habitat,
              "\nBerkembang Biak \t : ", self.berkembang_biak
              )
        
