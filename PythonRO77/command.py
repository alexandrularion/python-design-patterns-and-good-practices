"""
Command - este un design pattern comportamental care
incapsuleaza o actiune intr-un obiect.

Ex: Avem un sistem de comenzi. Fiecare actiune (plasare, anulare)
este o comanda care poate fi executata independent.

Avantaje:
- Separarea cererii de executia ei
- Usor de adaugat actiuni de genul undo / redo
- Comenzile pot fi puse intr-o coada sau logate intr-un sistem de logging
"""

# Command
class Command:
    def execute(self):
        pass

# Concrete Commands
class PlaceOrderCommand(Command):
    def __init__(self, order):
        self.order = order

    def execute(self):
        self.order.place()

class CancelOrderCommand(Command):
    def __init__(self, order):
        self.order = order

    def execute(self):
        self.order.cancel()

# Receiver
class Order:
    def __init__(self, name):
        self.name = name
        self.status = "Noua"

    def place(self):
        self.status = "Plasata"
        print(f"Comanda {self.name} a fost plasata")

    def cancel(self):
        if self.status != "Plasata":
            print(f"Comanda {self.name} nu poate fi anulata")
        else:
            self.status = "Anulata"
            print(f"Comanda {self.name} a fost anulata")

# Invoker
class OrderInvoker:
    def __init__(self):
        self.history = []

    def execute_command(self, command):
        command.execute()
        self.history.append(command)


# Utilizare
order1 = Order("Comanda1")
invoker = OrderInvoker()

# Cream comenzile
place_command = PlaceOrderCommand(order1)
cancel_command = CancelOrderCommand(order1)

# Executam comenzile prin invoker
invoker.execute_command(place_command)   # Plaseaza comanda
invoker.execute_command(cancel_command)  # Anuleaza comanda