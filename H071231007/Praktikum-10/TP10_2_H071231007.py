# from abc import ABC, abstractmethod
# #Implementasian Metode Enkapsulasi

# class Mobil:
#     def __init__(self, warna, merk):
#         self.__warna = warna
#         self.__merk = merk
    
#     def getWarna(self):
#         return self.__warna
#     def getMerk(self):
#         return self.__merk
#     def setWarna(self, warna):
#         self.__warna = warna
#     def setMerk(self, merk):
#         self.__merk = merk
        
# #Pengimplementasian Abstract Class, Inheritance, dan Polymorphism
# class Bentuk(ABC):
#     @abstractmethod
#     def HitungLuas(self):
#         pass

# class Persegi(Bentuk):
#     def __init__(self, sisi):
#         self.sisi = sisi
    
#     def HitungLuas(self):
#         return self.sisi ** 2
    
# class Segitiga(Bentuk):
#     def __init__(self, panjang, alas, tinggi):
#         self.panjang = panjang
#         self.alas = alas
#         self.tinggi = tinggi
#     def HitungLuas(self):
#         return 1/2 * self.alas * self.tinggi
    


n = int(input()).split()
x= len(n)

hasil=0
for i in range(1, n+1):
    hasil +=i
a=hasil(n)
print(a)