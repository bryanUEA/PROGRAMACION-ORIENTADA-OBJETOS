class Ave:
    def hacer_sonido(self):
        return "Canto de ave"

class Pato(Ave):
    def hacer_sonido(self):
        return "Cuac"

class Gallina(Ave):
    def hacer_sonido(self):
        return "Cloc"

# Función polimórfica
def hacer_cantar(ave):
    print(ave.hacer_sonido())

# Uso
pato = Pato()
gallina = Gallina()

hacer_cantar(pato)     # Salida: Cuac
hacer_cantar(gallina)  # Salida: Cloc
