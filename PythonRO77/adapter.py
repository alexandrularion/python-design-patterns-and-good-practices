"""
Adapter - este un pattern structural care permite
colaborarea intre doua interfete incompatibile.

Ex: Adaptor de priza -> Un smartphone -> asteapta 5V Type-C
Priza -> ofera 230V
Adaptorul -> face conversia de la 230V c.a. la 5V c.c.

Avantaje:
- Reutilizarea codului existent -> foarte util cand codul este legacy sau biblioteca este third-party
- Respecta principiul de Deschis / Inchis -> clasele existente nu sunt modificate, ci sunt extinse
- Creste flexibilitatea sistemului -> putem schimba implementarea reala fara a afecta clientul (legacy/third-party)
"""
# Legacy code
class EuropeanSocket:
    def voltage_230(self):
        return 230

class USDevice:
    def voltage_120(self):
        pass

class SocketAdapter(USDevice):
    def __init__(self, socket):
        self.socket = socket

    def voltage_120(self):
        # socket este un obiect instantiat de EuropeanSocket()
        return self.socket.voltage_230() / 2


eu_socket = EuropeanSocket()
print(eu_socket) # socket object

adapter = SocketAdapter(eu_socket)

print(adapter.voltage_120()) # 115.0

# Dispozitivul american functioneaza cu priza europeana