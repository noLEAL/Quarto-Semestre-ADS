#Lê dois números e mostre os seguintes resultados:
#    a. Dividendo:
#    b. Divisor:
#    c. Quociente:
#    d. Resto (para calcular o resto de uma divisão, utilize o operador MOD (em C: %)

a = float(input('Digite o Dividendo valor:'))
b = float(input('Digite o Divisor valor:'))

result = a/b

print('Dividendo:', a)
print('Divisor:', b)
print('Quociente:{:.2f}'.format(result))

result = a % b

print('Resto:', result)

print('Operador divMOD(Quociente,Restante)', divmod(a, b))