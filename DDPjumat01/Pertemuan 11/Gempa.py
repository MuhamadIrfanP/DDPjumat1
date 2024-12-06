class Gempa :
    lokasi =''
    skala = ''
    
    # Contraktor
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala
        
    # Fungsi/Mathod
    def dampak(self):
        if self.skala <2 :
            ket = 'Gempa Tidak Terasa'
        elif self.skala >2 and self.skala <4 :
            ket = 'Bangunan Retak-retak'
        elif self.skala >=4 and self.skala <6 :
            ket = 'Bangunan Roboh'
        else :
            ket = 'Bangunan Roboh dan Berpotensi Tsunami'
            
        print('Lokasi Gempa', self.lokasi, '\nSkala Gempa', self.skala, '\nDampak Gempa', ket)
            