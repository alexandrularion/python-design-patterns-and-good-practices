"""
State - este un design pattern comportamental care permite unu obiect
sa-si schimbe comportamentul atunci cand starea interna se modifica.

Obiectul isi schimba clasa.

Ex: O comanda poate fi in stari diferite: Noua, Neplatita, Platita, Livrata, Anulata
Fiecare stare permite sau blocheaza anumite actiuni.

Avantaje:
- Elimina scenariile in care avem instructiuni if/elif/else complexe
- Cod mai clar si extensibil
- Fiecare stare are responsabilitatea ei
"""

# State
# PascalCase
class NewOrder:
    def next(self, order):
        order.state = PaidOrder()

    def status(self):
        return "Noua"

class PaidOrder:
    def next(self, order):
        order.state = ShippedOrder()

    def status(self):
        return "Platita"

class ShippedOrder:
    def next(self, order):
        print("Comanda a fost deja livrata")

    def status(self):
        return "Livrata"


class Order:
    def __init__(self):
        self.state = NewOrder()

    def next_state(self):
        self.state.next(self)

    def get_status(self):
        print(f"Status comanda: {self.state.status()}")


# Utilizare
order1 = Order()
order1.get_status() # "Status comanda: Noua"

order1.next_state()
order1.get_status()

order1.next_state()
order1.get_status()

order1.next_state() # "Comanda a fost deja livrata"
order1.get_status()