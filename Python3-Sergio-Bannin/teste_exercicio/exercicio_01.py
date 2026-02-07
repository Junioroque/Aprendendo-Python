"""Escreva um programa que calcule o faturamento de um representante
 comercial que recebe R$ 500,00 fixos e 6% de comissão sobre as
 vendas do mês. Considere que ele fechou o mês com um valor de R$
12.398,00 em vendas. Exiba o resultado com duas casas decimais.
"""
venda = float(input("Digite o valor de vendas: "))
fixo = 500.00
comissao = 0.6

faturamento = (fixo + venda) * comissao

print("Faturamento do mês - {0:.2f}".format(faturamento))