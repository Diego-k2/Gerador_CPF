"""
Gerador de CPF
"""
from random import randint

numero_cpf = str(randint(100000000, 999999999))

contador = 0
soma = 0

for numero in numero_cpf:
    if contador < 9:
        multi = int(numero) * (10 - contador)
        soma = soma + multi
        contador += 1

conta_dig_1 = 11 - (soma % 11)

if conta_dig_1 > 9:
    dig_1 = "0"
else:
    dig_1 = str(conta_dig_1)

numero_cpf = numero_cpf + dig_1

contador = 0
soma = 0
for numero_2 in numero_cpf:
    if contador <= 9:
        multi = int(numero_2) * (11 - contador)
        soma = soma+ multi
        contador += 1

conta_dig_2 = 11 - (soma % 11)
if conta_dig_2 > 9:
    dig_2 = "0"
else:
    dig_2 = str(conta_dig_2)

numero_cpf = numero_cpf + dig_2

print(F"o CPF gerado foi: {numero_cpf}")






