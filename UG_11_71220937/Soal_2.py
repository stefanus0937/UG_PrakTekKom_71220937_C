#soal 2
def kelipatan_sembilan(angka):
    hasil = angka%9
    return hasil

print("Pemeriksa Kelipatan 9")
angka = int(input("Masukan Kelipatan 9 yang ingin diperiksa: "))

if kelipatan_sembilan(angka) == 0:
    print("Benar")
else:
    print("Salah")