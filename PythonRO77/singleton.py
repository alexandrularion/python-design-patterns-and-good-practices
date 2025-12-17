"""
Singleton - este un pattern de design care se asigura ca putem
crea o singura instanta si pune la dispozitie acea instanta global.
"""

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


my_object_1 = Singleton() # instanta 1
my_object_2 = Singleton() # instanta 2

print(my_object_1 is my_object_2) # True

# Exemplu real in generare de id-uri unice prin incrementare
class IdGenerator:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.id = 0
        return cls._instance

    # incrementeaza id-ul cu 1 la fiecare apel
    def next(self):
        self.id = self.id + 1
        return self.id


id1 = IdGenerator() # vom crea instanta global
id2 = IdGenerator() # vom obtine instanta creata la pasul anterior (36)
id3 = IdGenerator() # vom obtine instanta creata la pasul anterior (36)
id4 = IdGenerator() # vom obtine instanta creata la pasul anterior (36)

print(id1, id2, id3, id4)
print(id1 is id2, id2 is id4)

# am incrementat de 4 ori id-ul
id2.next() # 1
id4.next() # 2
id1.next() # 3
id3.next() # 4

print(id1.id) # 4
print(id2.id) # 4
print(id3.id) # 4
print(id4.id) # 4