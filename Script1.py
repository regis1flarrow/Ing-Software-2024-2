# Simulador de marcador de Tenis
# Autora Regina del Razo Castillo 

class Jugador:
    def __init__(self, nombre="", puntos_ranking=0):
        self.nombre = nombre
        self.puntos_ranking = puntos_ranking

    def actualizar_puntos_ranking(self, cambio_puntos):
        self.puntos_ranking += cambio_puntos

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return (
            f"Jugador(nombre='{self.nombre}', "
            f"puntos_ranking={self.puntos_ranking})"
        )


class Unidad:
    def __init__(self, jugadores=(Jugador(), Jugador())):
        self.jugadores = jugadores
        self.marcador = {
            self.jugadores[0]: 0,  
            self.jugadores[1]: 0,
        }
        self.ganador = None

    def obtener_ganador(self):
        return self.ganador

    def obtener_marcador(self):
        return self.marcador

    def esta_en_juego(self):
        return self.ganador is None


class Partido(Unidad):
    def __init__(
        self,
        jugador_1=Jugador(),
        jugador_2=Jugador(),
        al_mejor_de_5=True,
    ):
        super().__init__(jugadores=(jugador_1, jugador_2))
        self.al_mejor_de_5 = al_mejor_de_5
        self.sets_a_jugar = 5 if al_mejor_de_5 else 3
        self.sets = []

    def jugar_set(self):
        set = Set(self, len(self.sets) + 1)
        self.sets.append(set)

        while set.esta_en_juego():
            set.jugar_juego()
        ganador_set = set.obtener_ganador()
        self.marcador[ganador_set] += 1

        if self.marcador[ganador_set] == self.sets_a_jugar // 2 + 1:
            self.ganador = ganador_set

    def jugar_partido(self):
        while self.esta_en_juego():
            self.jugar_set()
        print(f"\nGanador: {self.ganador}")
        print(f"Marcador: {self}")

    def __str__(self):
        return " ".join([str(set) for set in self.sets])

    def __repr__(self):
        return (
            f"Partido("
            f"jugador_1={self.jugadores[0]}, "
            f"jugador_2={self.jugadores[1]}, "
            f"al_mejor_de_5={self.al_mejor_de_5})"
        )


class Set(Unidad):
    def __init__(self, partido: Partido, numero_set=0):
        super().__init__(partido.jugadores)
        self.partido = partido
        self.numero_set = numero_set
        self.juegos = []

    def jugar_juego(self, tiebreak=False):
        if tiebreak:
            juego = Tiebreak(self, len(self.juegos) + 1)
        else:
            juego = Juego(self, len(self.juegos) + 1)
        self.juegos.append(juego)

        print(
            f"\nRegistrar ganador del punto: "
            f"Pulse 1 para {self.jugadores[0]} | "
            f"Pulse 2 para {self.jugadores[1]}"
        )
        while juego.esta_en_juego():
            try:
                indice_ganador_punto = int(input("\nGanador del punto (1 o 2) -> ")) - 1
                if indice_ganador_punto not in [0, 1]:
                    raise ValueError("Por favor, ingrese 1 o 2.")
            except ValueError as ve:
                print(f"Error: {ve}")
            else:
                jugador_ganador_punto = self.jugadores[indice_ganador_punto]
                juego.registrar_punto(jugador_ganador_punto)
                print(juego)

        self.marcador[juego.ganador] += 1
        print(f"\nJuego {juego.ganador.nombre}")
        print(f"\nMarcador actual: {self.partido}")

        if (
            6 not in self.marcador.values()
            and 7 not in self.marcador.values()
        ):
            return
        if list(self.marcador.values()) == [6, 6]:
            self.jugar_juego(tiebreak=True)
            return
        for jugador in self.jugadores:
            if self.marcador[jugador] == 7:
                self.ganador = jugador
                return
            if self.marcador[jugador] == 6:
                if 5 not in self.marcador.values():
                    self.ganador = jugador

    def __str__(self):
        return "-".join(
            [str(valor) for valor in self.marcador.values()]
        )

    def __repr__(self):
        return (
            f"Set(partido={self.partido!r}, "
            f"numero_set={self.numero_set})"
        )


class Juego(Unidad):
    puntos = 0, 15, 30, 40, "Ad"  

    def __init__(self, set: Set, numero_juego=0):
        super().__init__(set.jugadores)
        self.set = set
        self.numero_juego = numero_juego

    def registrar_punto(self, jugador: Jugador):
        if self.ganador:
            print(
                "Error: Intentaste agregar un punto a un juego completado"
            )
            return
        juego_ganado = False
        punto_actual = self.marcador[jugador]

        if punto_actual == 40:
            if "Ad" in self.marcador.values():
                for cada_jugador in self.jugadores:
                    self.marcador[cada_jugador] = 40
            elif list(self.marcador.values()) == [40, 40]:
                self.marcador[jugador] = "Ad"
            else:
                juego_ganado = True
        elif punto_actual == "Ad":
            juego_ganado = True
        else:
            self.marcador[jugador] = Juego.puntos[Juego.puntos.index(punto_actual) + 1]

        if juego_ganado:
            self.marcador[jugador] = "Game"
            self.ganador = jugador

    def __str__(self):
        valores_marcador = list(self.marcador.values())
        return f"{valores_marcador[0]} - {valores_marcador[1]}"

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(set={self.set!r}, "
            f"numero_juego={self.numero_juego})"
        )


class Tiebreak(Juego):
    def __init__(self, set: Set, numero_juego=0):
        super().__init__(set, numero_juego)

    def registrar_punto(self, jugador: Jugador):
        if self.ganador:
            print(
                "Error: Intentaste agregar un punto a un juego completado"
            )
            return
        self.marcador[jugador] += 1
        if (
            self.marcador[jugador] >= 7
            and self.marcador[jugador] - min(self.marcador.values()) >= 2
        ):
            self.ganador = jugador


def main():
    try:
        nombre_jugador1 = input("Ingrese el nombre del jugador 1: ")
        nombre_jugador2 = input("Ingrese el nombre del jugador 2: ")
        jugador1 = Jugador(nombre=nombre_jugador1)
        jugador2 = Jugador(nombre=nombre_jugador2)
        partido = Partido(jugador_1=jugador1, jugador_2=jugador2, al_mejor_de_5=False)
        partido.jugar_partido()
    except Exception as e:
        print(f"Error: {e}")
        print("Ha ocurrido un error, por favor inténtelo de nuevo.")
        main()


if __name__ == "__main__":
    main()

