for kolom in range(1, 5):

    total_kolom = 0

    for baris in range(1, 4):

        nilai = kolom + baris

        total_kolom += nilai

    print(
        f"Total kolom {kolom} = "
        f"{total_kolom}"
    )