"""
Builder - este un pattern de design folosit pentru a construi un obiect
pas cu pas in loc sa avem foarte multi parametrii la constructor
"""

# Problema fara Builder pattern
class Car:
    def __init__(self, engine, color=None, sunroof=False, heated_chairs=False):
        self.engine = engine
        self.color = color
        self.sunroof = sunroof
        self.heated_chairs = heated_chairs

car = Car("V8", None, True, False) # neclar


# Solutia Builder pattern
"""
Product - obiectul care se construieste
Builder - o interfata abstracta pentru a construi parti ale obiectului
ConcreteBuilder - implementeaza Builder-ul cosntruit
Director (optional) - controleaza pasii de constructie
"""

# Componenta Product
class Car:
    def __init__(self, engine, color, sunroof, heated_chairs):
        self.engine = engine
        self.color = color
        self.sunroof = sunroof
        self.heated_chairs = heated_chairs

# Componenta Builder
class CarBuilder:
    def __init__(self, engine):
        self.engine = engine
        self.color = None
        self.sunroof = False
        self.heated_chairs = False

    def set_color(self, color):
        self.color = color
        return self

    def set_sunroof(self, sunroof):
        self.sunroof = sunroof
        return self

    def set_heated_chairs(self, heated_chairs):
        self.heated_chairs = heated_chairs
        return self

    def build(self):
        return Car(self.engine, self.color, self.sunroof, self.heated_chairs)


car1 = (CarBuilder("V8")
        .set_color("red")
        .set_sunroof(True)
        .build())

# Avantaj 1: Usor de citit
# Avantaj 2: Ordinea metodelor nu conteaza, metoda build se va apela mereu ultima
# Avantaj 3: Claritate in datele membre optionale sau necesare