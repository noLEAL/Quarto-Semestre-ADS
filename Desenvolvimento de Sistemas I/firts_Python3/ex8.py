#8. Lê o saldo de uma aplicação e imprima o novo saldo, considerado o reajuste de 1%.

balance =  float(input('Digite o valor do saldo:'))

result = (balance*100)/99

print('Seu novo saldo é de:{:.2f}'.format(result))

