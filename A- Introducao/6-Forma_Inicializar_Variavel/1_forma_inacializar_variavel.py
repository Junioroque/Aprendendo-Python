"""
Iniciar com letra, pode conter números, underline _, letras minusculas.
"""
nome = 'Junio Cezar'
idade = 37 # sabe que isso e um int
altura = 1.79 # sabe que isso e um float
e_maior = idade > 18 # bool
peso = 80  # bool
imc = peso / (altura ** 2)

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior:', e_maior)
print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)

nome = 'joãozinho'
idade = """40"""
peso = 80.5
e_maior = True

print(nome, 'tem', idade, 'anos e pesa', peso, 'quilos')
print(nome, 'é maior de idade', e_maior)