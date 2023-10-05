def permutasiKata(kata):
    permutasi = [kata[-i:] + kata[:-i] + " | " for i in range(1, len(kata) + 1)]
    hasil = ""
    for p in permutasi:
        hasil += p
    print(hasil)
kata_input = input("Masukkan kata: ")
permutasiKata(kata_input)