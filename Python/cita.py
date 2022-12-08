from console import Console

class Cita:
    def __init__(self, Cliente = False):
        self.Cliente = Cliente
        self.Console = Console(["hola"], [self.hola], "CITA")

    def hola(self):
        print("hola!")

    def run(self):
        self.Console.run()
        return 0