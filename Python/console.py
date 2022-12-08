from server import Server

class Console:
    def __init__(self):
        self.comandos = ["hola", "start", "help", "exit"]
        self.funciones = [self.saludar, self.start, self.help, self.exit]
        self.on = True

    def mostrarMenu(self):
        print("    .-.                     .-. ")
        print(" .--' /                     \ '--. ")
        print(" '--. \       _______       / .--' ")
        print("     \ \   .-\"       \"-.   / / ")
        print("      \ \ /             \ / / ")
        print("       \ /               \ / ")
        print("        \|   .--. .--.   |/ ")
        print("         | )/   | |   \( | ")
        print("         |/ \__/   \__/ \| ")
        print("         /      /^\      \ ")
        print("         \__    '='    __/ ")
        print("           |\         /| ")
        print("           |\\'\"VUUUV\"'/| ")
        print("           \ `\"\"\"\"\"\"\"` / ")
        print("            `-._____.-' ")
        print("              / / \ \ ")
        print("             / /   \ \ ")
        print("            / /     \ \ ")
        print("         ,-' (       ) `-,")
        print("         `-'._)     (_.'-` ")

    def pedirComnado(self):
        return input(">")

    def ejecutarComando(self):
        comando = self.pedirComnado()
        if comando in self.comandos:
            index = self.comandos.index(comando)
            self.funciones[index]()
        else:
            print("No existe el comando introducido")

    def saludar(self):
        print("Hola perro")

    def help(self):
        print("no hay ayuda que valga")

    def run(self):
        self.mostrarMenu()
        while self.on:
            self.ejecutarComando()
            print()

    def start(self):
        self.socket = Server("localhost" , 8080)
        self.socket.run()

    def exit(self):
        self.on = False