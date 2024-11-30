import math

#deklarasi fungsi
def luas_persegi(sisi):
    hitung = sisi * sisi
    print (f'Luas persegi dengan sisi {sisi} adalah = {hitung}')
    
def luas_persegi_panjang(p, l):
    hitung = p * l
    print (f'luas persegi panjang dengan panjang {p} dan lebar {l} adalah = {hitung}')
    
def luas_segitiga(a,t):
    hitung = 1/2 * a * t 
    print (f'luas segitiga dengan alas {a} dan tinggi {t} adalah = {hitung}')
    
def luas_lingkaran(r):
    hitung = r * 3.14 * r
    print(f'luas lingkaran dengan jari-jari {r} adalah = {hitung}')
    
def luas_jajargenjang(a, l):
    hitung = a * l 
    print(f'luas jajargenjang dari alas {a} dan lebar {l} adalah = {hitung}')
    