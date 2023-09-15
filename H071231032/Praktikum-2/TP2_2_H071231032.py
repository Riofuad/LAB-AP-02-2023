# Muhammad Qaffal Al Fifaiz
# H071231032
# Tugas Praktikum Pekan Kedua

a = input("\nMasukkan inputan pertama: ")
a = a.lower()

if a.isalpha():
    b = input("Masukkan inputan kedua: ")
    b = b.lower()
    if b.isalpha():
        c = input("Masukkan inputan ketiga: ")
        c = c.lower()
        print()
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
                                    print('Invalid input.')
                        case 'mamifero':
                            match c:
                                case 'onivoro':
                                    print('homem')
                                case 'herbivoro':
                                    print('vaca')
                                case _:
                                    print('Invalid input.')
                        case _:
                            print('Invalid input.')
                case 'invertebrado':
                    match b:
                        case 'inseto':
                            match c:
                                case 'hematofago':
                                    print('pulga')
                                case 'herbivoro':
                                    print('lagarta')
                                case _:
                                    print('Invalid input.')
                        case 'anelideo':
                            match c:
                                case 'hematofago':
                                    print('sanguessuga')
                                case 'onivoro':
                                    print('minhoca')
                                case _:
                                    print('Invalid input.')
                        case _:
                            print('Invalid input.')
                case _:
                    print('Invalid input.')
        else:
            print('Invalid input.')
    else:
        print('Invalid input.')
else:
    print('Invalid input.')