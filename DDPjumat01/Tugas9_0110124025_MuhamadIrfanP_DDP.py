print ('nomor 01')
def celcius_ke_fahrenheit (celcius):
    perhitungan = (celcius *9/5) + 32
    return perhitungan
    
print (f"Hasil dari 0 adalah {celcius_ke_fahrenheit(0)}")
print (f"Hasil dari 100 adalah {celcius_ke_fahrenheit(100)}")

print('============================================================================')
print('nomor 02')
def is_genap(bilangan):
    return bilangan % 2 == 0
print(f"apakah 4 bilangan genap? {is_genap(4)}")
print(f"apakah 7 bilangan genap? {is_genap(7)}")

print ('============================================================================')
print('nomor 03')
def nilai_kelulusan(nilai):
    if nilai >=80:
        return 'lulus'
    else :
        return 'gagal'
print(f"jika nilai 80 maka {nilai_kelulusan(80)}")
print(f"jika nilai 60 maka {nilai_kelulusan(60)}")
print('==============================================================================')
print('nomor 04')
def bil_ganjil(angka):
    for i in range(1, angka, 2):
        print(i, end=" ")
bil_ganjil(20)