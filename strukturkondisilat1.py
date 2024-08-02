# Menginputkan 2 buah bilangan
bilangan1 = int(input("Masukkan bilangan pertama: "))
bilangan2 = int(input("Masukkan bilangan kedua: "))

# Menggunakan statement if untuk menentukan bilangan terbesar
if bilangan1 > bilangan2:
    print("Bilangan terbesar adalah:", bilangan1)
elif bilangan2 > bilangan1:
    print("Bilangan terbesar adalah:", bilangan2)
else:
    print("Kedua bilangan bernilai sama.")