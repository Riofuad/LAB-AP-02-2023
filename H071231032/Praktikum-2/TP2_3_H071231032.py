mskn = input("Pilih golongan:\n1. R1\n2. R2\n3. R3\n4. B2\n5. B3\n6. I3\n7. P1\n")
if mskn.isdigit():
    gol = int(mskn)
    if 1 <= gol <= 7:
        match gol:
            case 1:
                daya = int(input("Daya: "))
                if daya == 900:
                    TARIF = float(1352)
                elif daya == 1300 or daya == 2200:
                    TARIF = float(1444.70)
                else:
                    print("Data invalid.")
                    quit()

                pakai = int(input("Pemakaian: "))
                TAGIHAN = float(TARIF * pakai)
                angka_str = str(TAGIHAN)
                depan,koma = angka_str.split('.')
                depan = int(depan)
                depan = f"{depan:,.0f}".replace(',','.')
                koma = koma[:2]
                print(f'Jumlah tagihan Anda sebesar: Rp. {depan},{koma}')

            case 2:
                daya = int(input("Daya: "))
                if 3500 <= daya <= 5500:
                    TARIF = float(1699.53)
                else:
                    print("Data invalid.")
                    quit()

                pakai = int(input("Pemakaian: "))
                TAGIHAN = float(TARIF * pakai)
                angka_str = str(TAGIHAN)
                depan, koma = angka_str.split('.')
                depan = int(depan)
                depan = f"{depan:,.0f}".replace(',','.')
                koma = koma[:2]
                print(f'Jumlah tagihan Anda sebesar: Rp. {depan},{koma}')

            case 3:
                daya = int(input("Daya: "))
                if daya >= 6600:
                    TARIF = float(1699.53)
                else:
                    print("Data invalid.")
                    quit()

                pakai = int(input("Pemakaian: "))
                TAGIHAN = float(TARIF * pakai)
                angka_str = str(TAGIHAN)
                depan, koma = angka_str.split('.')
                depan = int(depan)
                depan = f"{depan:,.0f}".replace(',','.')
                koma = koma[:2]
                print(f'Jumlah tagihan Anda sebesar: Rp. {depan},{koma}')

            case 4:
                daya = int(input("Daya: "))
                if 6600 <= daya <= 200000:
                    TARIF = float(1444.70)
                else:
                    print("Data invalid.")
                    quit()

                pakai = int(input("Pemakaian: "))
                TAGIHAN = float(TARIF * pakai)
                angka_str = str(TAGIHAN)
                depan, koma = angka_str.split('.')
                depan = int(depan)
                depan = f"{depan:,.0f}".replace(',','.')
                koma = koma[:2]
                print(f'Jumlah tagihan Anda sebesar: Rp. {depan},{koma}')

            case 5:
                daya = int(input("Daya: "))
                if daya > 200000:
                    TARIF = float(1114.74)
                else:
                    print("Data invalid.")
                    quit()

                pakai = int(input("Pemakaian: "))
                TAGIHAN = float(TARIF * pakai)
                angka_str = str(TAGIHAN)
                depan, koma = angka_str.split('.')
                depan = int(depan)
                depan = f"{depan:,.0f}".replace(',','.')
                koma = koma[:2]
                print(f'Jumlah tagihan Anda sebesar: Rp. {depan},{koma}')

            case 6:
                daya = int(input("Daya: "))
                if daya >= 200000:
                    TARIF = float(1314.12)
                else:
                    print("Data invalid.")
                    quit()

                pakai = int(input("Pemakaian: "))
                TAGIHAN = float(TARIF * pakai)
                angka_str = str(TAGIHAN)
                depan, koma = angka_str.split('.')
                depan = int(depan)
                depan = f"{depan:,.0f}".replace(',','.')
                koma = koma[:2]
                print(f'Jumlah tagihan Anda sebesar: Rp. {depan},{koma}')

            case 7:
                daya = int(input("Daya: "))
                if 6600 <= daya <= 200000:
                    TARIF = float(1523.28)
                else:
                    print("Data invalid.")
                    quit()
                    
                pakai = int(input("Pemakaian: "))
                TAGIHAN = float(TARIF * pakai)
                angka_str = str(TAGIHAN)
                depan, koma = angka_str.split('.')
                depan = int(depan)
                depan = f"{depan:,.0f}".replace(',','.')
                koma = koma[:2]
                print(f'Jumlah tagihan Anda sebesar: Rp. {depan},{koma}')

            case _:
                print("Invalid input.")
        

    else:
        print("Invalid input.")
else:
    print("Invalid input.")