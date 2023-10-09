# Soal Kedua
print("=" * 35)
print("    Menghitung Banyaknya Bilangan       ")
print("=" * 35)
print()

# Proses Input User
bil1 = int(input("Masukkan Bilangan Pertama : "))
bil2 = int(input("Masukkan Bilangan Kedua : "))

print()
list_bil = [i for i in range(bil1, bil2 + 1)]
print("Daftar Bilangan : {}".format(list_bil))
print()

genap = []
ganjil = []

for bil in list_bil:
      if bil % 2 == 0:
            genap.append(bil)
      else:
            ganjil.append(bil)
            
print("Bilangan Genap : {}".format(", ".join([str(bil) for bil in genap])))
print("Bilangan Ganjil : {}".format(", ".join([str(bil) for bil in ganjil])))
print()