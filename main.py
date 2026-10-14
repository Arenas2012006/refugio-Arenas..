from animal import Animal 


Luna = Animal("Luna", "Gato", 3)
Rocky = Animal("Rocky", "Perro", 5)
Kiwi = Animal("Kiwi", "Loro", 2)

Luna.presentarse()
Rocky.presentarse()
Kiwi.presentarse()

Luna.jugar()
Luna.comer(150)
Luna.dormir()
Rocky.jugar()
Rocky.jugar()
Rocky.jugar()
Rocky.comer(300)
Kiwi.comer(100)
Kiwi.dormir()
print(f'\nLa energia de Luna es: {Luna.energia}')
print(f'\nLa energia de Rocky es: {Rocky.energia}')
print(f'\nLa energia de Kiwi es: {Kiwi.energia}')
