tabuada = int(input("Digite um número para exibir a tabuada: "));
print("Tabuada do número: "+ str(tabuada));

for valor in range(1, 11, 1):
    print (str(tabuada) + " x " + str(valor) + " = " + str(tabuada * valor));