# Muhammad Qaffal Al Fifaiz
# H071231032
# Tugas Praktikum Pekan Kedua

print("\nPencocokan Organisme\n====================")

a = input("\nMasukkan inputan pertama: ")
a = a.lower()
if a.isalpha():
    b = input("Masukkan inputan kedua: ")
    b = b.lower()
    if b.isalpha():
        c = input("Masukkan inputan ketiga: ")
        c = c.lower()
        if c.isalpha():
            match a:
                case 'vertebrado':
                    match b:
                        case 'ave':
                            match c:
                                case 'carnivoro':
                                    print('agula')
                                case 'onivoro':
                                    print('pomba')
                                case _:
                                    print('\nInvalid input.\n')
                        case 'mamifero':
                            match c:
                                case 'onivoro':
                                    print('homem')
                                case 'herbivoro':
                                    print('vaca')
                                case _:
                                    print('\nInvalid input.\n')
                        case _:
                            print('\nInvalid input.\n')
                case 'invertebrado':
                    match b:
                        case 'inseto':
                            match c:
                                case 'hematofago':
                                    print('pulga')
                                case 'herbivoro':
                                    print('lagarta')
                                case _:
                                    print('\nInvalid input.\n')
                        case 'anelideo':
                            match c:
                                case 'hematofago':
                                    print('sanguessuga')
                                case 'onivoro':
                                    print('minhoca')
                                case _:
                                    print('\nInvalid input.\n')
                        case _:
                            print('\nInvalid input.\n')
                case _:
                    print('\nInvalid input.\n')
        else:
            print('\nInvalid input.\n')
    else:
        print('\nInvalid input.\n')
else:
    print('\nInvalid input.\n')