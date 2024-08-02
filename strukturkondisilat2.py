# Fungsi untuk mengurutkan data berdasarkan input sejumlah
def urut_data():
    # Mengambil input sejumlah data
    n = int(input("Masukkan sejumlah data yang ingin diurutkan: "))

    # Mengambil input data yang ingin diurutkan
    data = []
    for i in range(n):
        value = input(f"Masukkan data {i+1}: ")
        data.append(value)

    # Mengurutkan data yang ada dalam list `data`
    data.sort()

    # Menampilkan hasil data yang telah diurutkan
    print("Hasil data yang telah diurutkan:", data)

# Menjalankan fungsi untuk mengurutkan data berdasarkan input sejumlah
urut_data()