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


class Moto(Vehiculo):
    def __init__(self, nombre, gasolina=5):
        self.ruedas = 2
        self.gasolina = gasolina
        self.kilometro = 0
        self.nombre  = nombre 

    def andar(self, kilometros = 1):
        # Aquí estoy sobreescribiendo el método andar de Vehículo (overwrite)
        if self.gasolina >= 0.5:
            
            self.gasolina = self.gasolina - 0.1 * kilometros
            self.kilometro = self.kilometro + kilometros
            print( self.nombre + " anda " + str(kilometros) + " km y me queda " + str(self.gasolina) + " de gasolina")
            
        else:
            print("no tengo gasolina")        self.gasolina = self.gasolina + gasolina + 2



class Coche(Vehiculo):
    # Esto se llama herencia:
    # Coche hereda de Vehículo sus propiedades y métodos
    # Vehículo es la clase padre

    # This is inheritance
    # Coche inherits from Vehiculo its properties and methods
    # Vehiculu is the parent class
    def __init__(self, nombre, gasolina=5):
        super().__init__(4, nombre, gasolina)
        





moto1 = Moto("vespino")  # moto1 es un objeto creado al instanciar la clase Vehiculo
coche1 = Vehiculo(4, "805", 2) # coche1 is an object created after instanciate the class Vehículo
coche2 = Coche( "focus", 3)

moto1.andar()
moto1.andar()
coche2.andar()
moto1.andar(20)
moto1.andar(2)
moto1.repostar(6)
coche2.andar()
print (coche2.nombre, coche2.gasolina, coche2.kilometro)
print (coche1.nombre, coche1.gasolina, coche1.kilometro)
print (moto1.nombre, moto1.gasolina, moto1.kilometro)

