class Lugar:
    def __init__(self, numero):
        self.numero = numero
        self.ocupado = False
    def ocupar(self):
        if not self.ocupado:
            self.ocupado = True
            return True
        return False
    def liberar(self):
        self.ocupado = False