import random

class Equipo:
    def __init__(self, nombre):  
        self.nombre = nombre
        self.partidosGanados = 0
        self.partidosPerdidos = 0
        self.setGanados = 0

def RegistraSet(equipo1, equipo2, ganador_num):
    if ganador_num == 1:
        equipo1.setGanados += 1
        if equipo1.setGanados == 3:
            equipo1.partidosGanados += 1
            equipo2.partidosPerdidos += 1
            equipo1.setGanados = 0
            equipo2.setGanados = 0
    elif ganador_num == 2:
        equipo2.setGanados += 1
        if equipo2.setGanados == 3:
            equipo2.partidosGanados += 1
            equipo1.partidosPerdidos += 1
            equipo1.setGanados = 0
            equipo2.setGanados = 0

def Puntos():
    return random.randint(10, 28)

def PuntosExtras():
    return random.randint(0, 6)

def JugarPartido(equipo1, equipo2):
    while True:
        puntos1 = Puntos()
        puntos2 = Puntos()
        
        if puntos1 >= 25 or puntos2 >= 25:
            if puntos1 >= 25 and puntos1 >= puntos2:
                RegistraSet(equipo1, equipo2, 1)
                print(f"{equipo1.nombre} gana el set con {puntos1} puntos contra {puntos2}")
                break
            elif puntos2 >= 25 and puntos2 > puntos1:
                RegistraSet(equipo1, equipo2, 2)
                print(f"{equipo2.nombre} gana el set con {puntos2} puntos contra {puntos1}")
                break
        else:
            puntos1 += PuntosExtras()
            puntos2 += PuntosExtras()
            print(f"Ningún equipo superó 25 puntos, sumando puntos extras: {equipo1.nombre} {puntos1}, {equipo2.nombre} {puntos2}")

def ResultadoTorneo(equipo1, equipo2):
    print("\nResultados del Torneo:")
    print(f"{equipo1.nombre}: Partidos Ganados: {equipo1.partidosGanados}, Partidos Perdidos: {equipo1.partidosPerdidos}")
    print(f"{equipo2.nombre}: Partidos Ganados: {equipo2.partidosGanados}, Partidos Perdidos: {equipo2.partidosPerdidos}")

if __name__ == "__main__":  # Corrección del error en el bloque principal
    nombre1 = input("Nombre del Equipo 1: ")
    nombre2 = input("Nombre del Equipo 2: ")

    equipo1 = Equipo(nombre1)
    equipo2 = Equipo(nombre2)

    partidos_a_jugar = int(input("¿Cuántos partidos deben jugar ambos equipos? "))

    for _ in range(partidos_a_jugar):
        JugarPartido(equipo1, equipo2)

    ResultadoTorneo(equipo1, equipo2)