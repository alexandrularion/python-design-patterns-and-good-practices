"""
Decorator - este un design pattern structural care permite adaugarea de
comportament nou unui obiect sau unei functii fara a modifica codul original.

Ex: Avem o functie care salveaza o comanda (shop). Vrei sa adaugi verificare
de autentificare inainte de salvare, fara sa modifici functia originala.

Avantaje:
- Separarea responsabilitatilor -> Logica principala ramane curata, partea de autentificare, login sunt separate
- Codul este mai usor de intretinut -> Daca schimbi decoratorul va afecta toate functionalitatile
- Reutilizarea codului existent -> acelasi decorator poate fi folosit la mai multe functii
"""
# Login Middleware
def require_login(func):
    def wrapper(user):
        if not user['logged_in']:
            # Interogam baza de date ca sa putem verifica utilizatorul
            print("Acces interzis. Utilizator neautentificat.")
            return
        return func(user)
    return wrapper

@require_login
def  place_order(user):
    print(f"Comanda a fost plasata pentru {user['fullName']}")


user1 = { "fullName": "Ion", "logged_in": False }
user2 = { "fullName": "Ana", "logged_in": True }

place_order(user1)
place_order(user2)