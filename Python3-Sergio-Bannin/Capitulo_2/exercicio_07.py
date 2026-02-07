"""Escreva a sequência de comandos para calcular o salário bruto de um
profissional que ganha por hora, sabendo que ele ganha R$ 14,25/h e
 trabalhou 163 horas normais e 20 horas extras (pagam o dobro).
"""

hora = 14.25
horaTrabalhada = 163
horaExtra = 20

trabalhou = horaTrabalhada * hora
horaExtraTrabalhou = (2 * hora) * horaExtra

print(f"Salario do trabalhador com horas trabalhada: {trabalhou}")

print(f"Hora extra trabalhada: {horaExtraTrabalhou}")