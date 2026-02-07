"""
*Criar variável para nome (str), idade (int),
*altura (float) de uma pessoa.
*Criar variável com o ano atual (int)
*Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
*Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
*Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""
nome = 'Junio Cezar'
idade = 38
altura = 1.79
peso = 84
imc = peso / (altura ** 2)
ano = 2021
ano_nascimento = ano - idade

print(f'{nome} tem {idade} anos, {altura} de altura e peso {peso}.')
print(f'O IMC de {nome} é {imc: .2f}.')
print(f'{nome} nasceu em {ano_nascimento}.')
print('"ja sei!"')
"""
n1 = 2
n2 = '2'
n3 = n1 + n2
print(n3)
"""
