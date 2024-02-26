#Entre com a base e a altura de um retângulo e mostre os resultados:
#   a. Perímetro (Perímetro é igual à soma dos 4 lados)
#   b. Área (Área é igual à lado vezes lado)

height = float(input('Valor da altura:'))
base = float(input('Valor da base:'))


perimeter = (height * 2) + (base * 2)
zone = height * base

print('Perímetro:', perimeter)
print('Área:', zone)