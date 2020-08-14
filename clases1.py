class Vehiculo:
    def __init__(self, ruedas, nombre, gasolina=5):
        """
        __init__ es una función especial que se llama constructor
        Se usa para inicializar el objeto
        """
        self.ruedas = ruedas
        self.gasolina = gasolina
        self.kilometro = 0
        self.nombre  = nombre

    def andar(self, kilometros = 1):
        if self.gasolina >= 0.5:
            
            self.gasolina = self.gasolina - 0.5 * kilometros
            self.kilometro = self.kilometro + kilometros
            print( self.nombre + " anda " + str(kilometros) + " km y me queda " + str(self.gasolina) + " de gasolina")
            
        else:
            print("no tengo gasolina")

    def repostar(self, gasolina):
        self.gasolina = self.gasolina + gasolina



moto1 = Vehiculo(2, "vespino")  # moto1 es un objeto creado al instanciar la clase Vehiculo
coche1 = Vehiculo(4, "805", 2)
coche2 = Vehiculo(4, "focus", 3)

moto1.andar()
moto1.andar()
coche2.andar()
moto1.andar(20)
moto1.andar(2)
moto1.repostar(6)
coche2.andar()

