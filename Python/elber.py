from console import Console
from cita import Cita
cita = Cita()
Consola = Console(["pedir"], [cita.run], "ELBER")
Consola.run()