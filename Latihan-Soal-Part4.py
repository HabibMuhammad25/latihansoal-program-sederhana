# Soal Keempat
print("=" * 30)
print("     Program Segitiga Angka   ")
print("=" * 30)

tinggiSegitiga = int(input("Masukkan Tinggi Segitiga : "))
print()

for i in range(1, tinggiSegitiga + 1):
      for j in range(1, i + 1):
            print(j,' ',end='',sep='')
      print()
