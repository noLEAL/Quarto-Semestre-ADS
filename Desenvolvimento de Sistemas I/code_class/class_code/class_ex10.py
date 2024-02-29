# Questão 31. Elabore um algoritmo que lê 6 números decimais e mostra a soma e a subtração dos valores digitados.

control = 0

numbers = []

while control < 6:
    numbers.append(float(input("Informe um número decimal:")))

    control += 1

result = sum(numbers)

print(f"O resultado é:{result}")

result = -sum(numbers)

print(f"O resultado é:{result}")
