"""Um vendedor ambulante vendeu os produtos indicados na tabela a
 seguir. Informe quanto ele faturou com cada produto e quanto ele
 faturou no total.
 
Produto             Quantidade    vendida Valor unitário R$
Boneco Malandrinho  17            18,50
Spinner Pequeno     36            12,00
Cubo Mágico          7             5,90

Todos os dados devem ser lidos do teclado, sendo que o nome do
produto é string, a quantidade vendida é um número inteiro e o valor
unitário é um número real.
"""

produtoBoneco = "Boneco Malandrinho"
produtoSpinner = "Spinner Pequeno"
produtoCubo = "Cubo Mágico"
resultado = 0.0;

texto = """
  1 - Boneco Malandrinho  valor unitário R$ 18,50
  2 - Spinner Pequeno     valor unitário R$ 12,00
  3 - Cubo Mágico         valor unitário R$ 5,90
"""

print(texto);

sim = True;

while (sim):
  
   escolha = int(input("Qual produto que você vendeu: "));
   quantidade = int(input("Quantidade vendidas: "));
   
   if(escolha == 1):
     boneco = 18.50
     resultado = int(boneco) * float(quantidade)
     print(f"Você faturou com o produto {produtoBoneco} R$ {resultado:.2f}") 
     break;
   elif(escolha == 2):
     spinner = 12.00
     resultado = spinner * int(quantidade)
     print(f"Você faturou com o produto {produtoSpinner} R$ {resultado:.2f}")
     break;
   elif(escolha == 3):
     cubo = 5.90
     resultado = cubo * int(quantidade)
     print(f"Você faturou com o produto {produtoCubo} R$ {resultado:.2f}")
   else:
     print("Escolha errada! Deseja repetir S- Sim ou N- Não");
   



