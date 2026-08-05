"""
Escreva um programa que calcule o faturamento de um representante
comercial que recebe R$ 500,00 fixos e 6% de comissão sobre as
vendas do mês. Considere que ele fechou o mês com um valor de R$
12.398,00 em vendas. Exiba o resultado com duas casas decimais.
"""
fixo = 500.00;
vendas = 12398.00;
comissao = 0.06;

faturamento = fixo + (vendas * comissao);

print(f"Faturamento do mês: R$ {faturamento:.2f}");

    