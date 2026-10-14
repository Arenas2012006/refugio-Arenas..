class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        self.energia = 50

    def presentarse(self):
        text = f"Hola, soy {self.name}. Especie: {self.species}. Edad: {self.age} años)"
        print(text)

    def presentarse(self):
            pass
    def jugar(self):
        self.energia -= 20
        if self.energia < 0:
            self.energia = 0
        print(f'Jugando... energia actual: {self.energia}')

        
    def comer(self, gramos: int):
        self.energia += (gramos // 10)
        if self.energia > 100:
                    self.energia = 0
        print(f'Comiendo... energia nueva: {self.energia}')
        
    def dormir(self):
        self.energia += 30
        if self.energia > 100:
            self.energia = 100 
        print (f'Durmiendo... energia nueva: {self.energia}')

