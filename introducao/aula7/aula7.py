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
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e sue imc é {:.2f}'. format(nome, idade, imc))
print('{0} {0} tem {1} anos de idade e sue imc é {2:.2f}'. format(nome, idade, imc))#repete com ordem de impressão
print('{i} tem {im} {n} anos de idade e sue imc é {im:.2f}'. format(n=nome, i=idade, im=imc))#dei o siguinificado agora posso mudar de ordem