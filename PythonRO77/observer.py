"""
Observer - este un design pattern comportamental care defineste
o relatie de tip publisher / subscriber intre obiecte.

Cand starea unui obiect se schimba, toti observatorii abonati
sunt notificati automat.

Ex: Avem un magazin online. Cand statusul unei comenzi se schimba
clientul este notificat prin email, sms sau alte canale.

Avantaje:
- Separarea responsabilitatilor -> Comanda nu stie cum se face notificarea
- Codul este usor de extins -> Poti adauga noi tipuri de notificari fara a modifica comanda
- Comunicare decuplata intre obiecte
"""

# Observer
class Observer:
    def update(self, message):
        pass

class EmailNotifier(Observer):
    def update(self, message):
        print(f"[Email] Notificare: {message}")

class SMSNotifier(Observer):
    def update(self, message):
        print(f"[SMS] Notificare: {message}")

class Order:
    def __init__(self):
        self.status = "Noua"
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(f"Status comanda: {self.status}")

    def change_status(self, status):
        self.status = status
        self.notify()


# Utilizare
order1 = Order()
email_notifier = EmailNotifier()
sms_notifier = SMSNotifier()

# Abonam observatorii
order1.attach(email_notifier)
order1.attach(sms_notifier)

# Schimbam statusul comenzii -> toti observatorii sunt notificati
order1.change_status("Platita")
order1.change_status("Livrata")