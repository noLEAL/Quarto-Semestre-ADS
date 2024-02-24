# 2. Mostrar a média aritmética entre 3 números fornecidos pelo usuário.

a = float(input('Digite o primeio numero:'))
b = float(input('Digite o primeio segundo:'))
c = float(input('Digite o primeio teceiro:'))

sum = a + b + c

result = sum/3

print('Sua média aritimética é:{:.2f}'.format(result))

print('Outra forma')

print(f'Sua média aritimética é:{result:.2f}')

