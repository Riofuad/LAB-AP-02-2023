# Muhammad Qaffal Al Fifaiz | H071231032 | Tugas Praktikum Pekan Kedua

print("\nPenghitung Jumlah Tagihan Listrik\n=================================\n")

# Input golongan dan penanganan traceback-nya
gol = input("Pilih golongan:\n1. R1\t4. B2\t7. P1\n2. R2\t5. B3\n3. R3\t6. I3\n")
if gol.isdigit() == False or gol not in ('1','2','3','4','5','6','7'):
    print("\nInvalid data.\n")
    quit()
gol = int(gol)

# Input daya dan penanganan traceback-nya
daya = input("\nDaya: ")
if daya.isdigit() == False:
    print("\nInvalid data.\n")
    quit()
daya = int(daya)

# Penentuan tarif per kWh
match gol:
    case 1:
        if daya == 900:
            TARIF = float(1352)
        elif daya == 1300 or daya == 2200:
            TARIF = float(1444.70)
        else:
            print("\nInvalid data.\n")
            quit()
                
    case 2:  
        if 3500 <= daya <= 5500:
            TARIF = float(1699.53)
        else:
            print("\nInvalid data.\n")
            quit()

    case 3:     
        if daya >= 6600:
            TARIF = float(1699.53)
        else:
            print("\nInvalid data.\n")
            quit()

    case 4: 
        if 6600 <= daya <= 200000:
            TARIF = float(1444.70)
        else:
            print("\nInvalid data.\n")
            quit()

    case 5:        
        if daya > 200000:
            TARIF = float(1114.74)
        else:
            print("\nInvalid data.\n")
            quit()

    case 6:      
        if daya >= 200000:
            TARIF = float(1314.12)
        else:
            print("\nInvalid data.\n")
            quit()

    case 7:        
        if 6600 <= daya <= 200000:
            TARIF = float(1523.28)
        else:
            print("\nInvalid data.\n")
            quit()

    case _:
        print("Invalid input.")
        quit()

# Input pemakaian dan penanganan traceback-nya
pakai = input("Pemakaian: ")
if pakai.isdigit() == False:
    print("\nInvalid data.\n")
    quit()
pakai = int(pakai)

# Menghitung jumlah tagihan sesuai dengan data yang telah dimasukkan
tagihan = float(TARIF * pakai)

# Mengatur format tulisan jumlah tagihan sesuai dengan Kaidah Bahasa Indonesia dan mencetak jumlah tagihan
depan,koma = str(tagihan).split('.')
depan = int(depan); koma = koma[:2]
depan = f"{depan:,}".replace(',','.')
print(f'\nJumlah tagihan Anda sebesar: Rp{depan},{koma}\n')