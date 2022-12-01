#Soal 1
def rumus_jumlah(bil1, bil2):
    jumlah = (bil1+bil2)
    return jumlah

def rumus_kurang(bil1, bil2):
    kurang = (bil1-bil2)
    return kurang

def rumus_perkalian(bil1,bil2):
    kali = (bil1*bil2)
    return kali

def rumus_pembagian(bil1,bil2):
    bagi = (bil1/bil2)
    return bagi

#hasil print
print("="*20)
print("Operasi Matematika")
print("1. Jumlah    [+]")
print("2. Kurang    [-]")
print("3. Kali      [*]")
print("4. Bagi      [/]")

print("="*20)
n = int(input("Pilih operasi (1/2/3/4): "))
print("="*20)
bil1 = int(input("Masukan bilangan pertama: "))
bil2 = int(input("Masukan bilangan kedua: "))

if n == 1:
    print("Hasil operasi dari",bil1,"+",bil2,"=",rumus_jumlah(bil1, bil2))
elif n == 2:
    print("Hasil operasi dari",bil1,"-",bil2,"=",rumus_kurang(bil1, bil2))
elif n == 3:
    print("Hasil operasi dari",bil1,"*",bil2,"=",rumus_perkalian(bil1, bil2))
elif n == 4:
    print("Hasil operasi dari",bil1,"/",bil2,"=",rumus_pembagian(bil1, bil2))
else:
    print("INVALID!!")
    print("Try Again")