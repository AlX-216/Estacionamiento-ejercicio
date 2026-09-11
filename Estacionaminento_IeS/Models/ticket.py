class Ticket:
    def __init__(self, numero, vehiculo, lugar):
        self.numero = numero
        self.vehiculo = vehiculo
        self.lugar = lugar
    def mostrar(self):
        print("----- TICKET -----")
        print(f"Ticket: {self.numero}")
        print(f"Vehículo: {self.vehiculo.placa}")
        print(f"Lugar: {self.lugar.numero}")