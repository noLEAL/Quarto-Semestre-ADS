nome = input('Digite seu nome: ')

print(f"Seja bem vindo {nome}")

min = int(input("Digite quantos minutos foram falados no mês:"))

if min < 200:
    conta = min * 0.20
elif min <= 400:
    conta = min * 0.18
else:
    conta = min * 0.15
print(f"O total da conta é R$ {conta:.2f}")