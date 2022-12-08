import os

class Console:
    def __init__(self, comandos, funciones, icon):
        comandos.append("cls")
        comandos.append("help")
        comandos.append("exit")
        funciones.append(self.cls)
        funciones.append(self.help)
        funciones.append(self.exit)
        self.comandos = comandos
        self.funciones = funciones
        self.asciIcon = icon
        self.on = True

    def mostrarMenu(self, fin="\n"):
        #os.system('cls')
        print(self.asciIcon, end=fin)

    def pedirComnado(self):
        return input(">")

    def ejecutarComando(self):
        comando = self.pedirComnado()
        if comando in self.comandos:
            index = self.comandos.index(comando)
            if(self.funciones[index]()==0):
                self.cls()
        else:
            print("No existe el comando introducido")

    def run(self):
        self.cls("\n")
        while self.on:
            self.ejecutarComando()
            print()
        self.on = True

    def cls(self, fin=" "):
        os.system('cls')
        self.mostrarMenu(fin)

    def help(self):
        for i in range(len(self.comandos)):
            print()
            print("-"+self.comandos[i])

    def exit(self):
        self.on = False