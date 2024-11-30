import math

def luas_kubus(sisi):
    hitung = 6 * (sisi**2)
    print(f'luas kubus dengan sisi {sisi} adalah = {hitung}')
    

def luas_balok(p, l, t):
    hitung = 2 * (p*l)+(p*t)+(l*t)
    print(f'luas balok dengan panjang {p}, lebar {l}, tinggi {t} adalah = {hitung}')
    
def luas_tabung(r, t):
    hitung = 2 * math.pi * r * (r + t)
    print (f'luas tabung dari jari_jari {r} dan tinggi {t} adalah = hitung')
    
def luas_limas(alas, tinggi_alas, sisi_tegak, tinggi_sisi):
    hitung_alas = alas * tinggi_alas
    hitung_sisi_tegak = sisi_tegak * tinggi_sisi / 2
    # Total luas limas
    hitung_total_luas = hitung_alas + 4 * hitung_sisi_tegak
    print(f'luas alas prisma dari alas {alas}, tinggi alas {tinggi_alas}, sisi tegak {sisi_tegak}, tinggi sisi {tinggi_sisi} adalah = {hitung_total_luas}')
    
def luas_prisma(alas, tinggi_alas, tinggi_prisma):
    hitung_luas_alas = 0.5 * alas * tinggi_alas
    hitung_keliling_alas = 3 * alas
    # Total luas prisma
    hitung_total_luas = 2 * hitung_luas_alas + hitung_keliling_alas * tinggi_prisma
    print(f'luas prisma dari alas {alas}, tinggi alas {tinggi_alas}, tinggi prisma {tinggi_prisma} adalah = {hitung_total_luas}')