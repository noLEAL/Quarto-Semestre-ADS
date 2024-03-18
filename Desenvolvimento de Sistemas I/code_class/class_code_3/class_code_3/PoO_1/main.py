from carro import Carro

fusca = Carro()
fusca.marca = "Volkswagen"
fusca.modelo = "Fusca"
fusca.ano = 1965

print(f"Carro: {fusca.marca} - {fusca.modelo} - {fusca.ano}")

cheva = Carro()
cheva.ano = 1965
cheva.marca = "Chevrolet"
cheva.modelo = "Chevette Tubarão"

print("Carro: {} - {} - {}".format(cheva.marca, cheva.modelo, cheva.ano)))

sonic = Carro()
sonic.ano = 2012
sonic.marca = "Chevrolet"
sonic.modelo = "Sonic LTZ"

print("Carro: {} - {} - {}".format((sonic.marca, sonic.modelo, sonic.ano)))