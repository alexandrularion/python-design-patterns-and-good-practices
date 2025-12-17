"""
Factory - este un pattern de creare folosit pentru a crea obiecte
fara a specifica clasa exacta a obiectului care va fi creat.

Ex: In loc sa apelezi constructorul unei clase direct, folosesti
o metoda de tip "factory" pentru a obtine o instanta.

Avantaje:
- Flexibiltiate in crearea obiectelor
- Clientul nu va sti ce clasa specifica este instantiata
- Putem centraliza logica de creare a obiectelor intr-un singur loc
"""


class Pizza:
    def __init__(self, dough):
        self.dough = dough
    def serve(self):
        pass

class Margherita(Pizza):
    def serve(self):
        print("Pizza margherita is ready")

class Pepperoni(Pizza):
    def serve(self):
        print("Pizza pepperoni is ready")

class Vegetariana(Pizza):
    def serve(self):
        print("Pizza vegetariana is ready")


class PizzaFactory:
    @staticmethod
    def create_pizza(type: str, dough: str = "classic"):
        if type == "margherita":
            return Margherita(dough)
        elif type == "pepperoni":
            return Pepperoni(dough)
        elif type == "vegetariana":
            return Vegetariana(dough)
        else:
            raise ValueError("Pizza type unknown")


pizza1 = PizzaFactory.create_pizza("margherita")
pizza1.serve() # "Pizza margherita is ready"

pizza2 = PizzaFactory.create_pizza("pepperoni")
pizza2.serve()

pizza3 = PizzaFactory.create_pizza("vegetariana")
pizza3.serve()

# pizza4 = PizzaFactory.create_pizza("special") # ne va afisa o eroare "Pizza type unknown"