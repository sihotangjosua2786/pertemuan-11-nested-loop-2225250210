print("MATRIKS PENJUMLAHAN DAN STATISTIK")

n = int(input("Masukkan n : "))

while n <= 0:

    print("n harus lebih dari 0")

    n = int(input("Masukkan n : "))

total_semua = 0
count_ganjil = 0

print("\nTABEL\n")

for i in range(1, n + 1):

    total_baris = 0

    for j in range(1, n + 1):

        hasil = i + j

        print(f"{hasil:4}", end="")

        total_baris += hasil
        total_semua += hasil

        if hasil % 2 != 0:

            count_ganjil += 1

    print(
        f" | Jumlah Baris = "
        f"{total_baris}"
    )

print()
print(
    "Total seluruh nilai =",
    total_semua
)

print(
    "Jumlah nilai ganjil =",
    count_ganjil
)