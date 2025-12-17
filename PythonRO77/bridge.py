"""
Bridge - este un pattern structural care separa abstractia de
implementare astfel incat ambele sa poata evolua independent.

Ex: Notificari -> Tipuri: Alerta, Mesaj, Reminder -> Canale: Email, SMS, Push
Fara Bridge -> Explozie de clase: EmailAlert, SMSAlert, PushAlert, EmailMessage, SMSMessage, PushMessage...

Avantaje:
- Evitam exploza de clase (adesea nr-ul de clase este mare)
- Decuplare puternica care ne ajuta scalabilitate
- Testare usoara (nr redus de clase)
"""

class NotificationSender:
    def send(self, message):
        raise NotImplementedError

class EmailSender(NotificationSender):
    def send(self, message):
        print(f"Email: {message}")

class SMSSender(NotificationSender):
    def send(self, message):
        print(f"SMS : {message}")

class PushSender(NotificationSender):
    def send(self, message):
        print(f"Push : {message}")


class Notification:
    def __init__(self, sender: NotificationSender):
        self.sender = sender

    def notify(self, message):
        raise NotImplementedError


class Alert(Notification):
    def notify(self, message):
        self.sender.send(f"[ALERT]: {message}")

class Reminder(Notification):
    def notify(self, message):
        self.sender.send(f"[REMINDER]: {message}")


email_sender = EmailSender()
email_alert = Alert(email_sender)

push_sender = PushSender()
push_alert = Alert(push_sender)

email_alert.notify("The server is down.")
push_alert.notify("Ai incasat 10.000 RON.")

"""
Ce castigam?
- Putem adauga un nou canal (oricand, de ex: WhatsAppSender)
- Putem adauga un nou tip de notificare (oricand, de ex: MarketingNotification"
FARA a modifica codul existent.
"""