n = int(input("Masukkan n : "))

count = 0

for i in range(1, n + 1):

    for j in range(1, n + 1):

        if (i * j) % 3 == 0:

            count += 1

print(
    "Jumlah pasangan "
    "kelipatan 3 =",
    count
)