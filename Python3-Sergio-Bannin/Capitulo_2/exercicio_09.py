"""Escreva um programa que leia do teclado as coordenadas (x1, y1) do
 ponto 1 e (x2, y2) do ponto 2. Utilizando a expressão do item 8.e,
 determine a distância entre esses dois pontos e exiba-a na tela com três
 casas decimais. Teste-o com os dados da tabela a seguir.
 Tabela:
  x1    y1    x2    y2    d
  0,0   0,0   3,0   4,0   5,000
  2,0   1,0   0,0   5,0   4,472
 -3,0   1,5   7,1   5,5   10,863
  0,0   3,5   0,0   7,0   3,500
  8,2   2,5  -5,0  -5,0   15,182
  6,9   2,0   16,0 -1,8   9,862
"""
import math

x1 = float(input("Digite a coordenada x1: "))
y1 = float(input("Digite a coordenada y1: "))
x2 = float(input("Digite a coordenada x2: "))
y2 = float(input("Digite a coordenada y2: "))
    
distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"Distância entre os pontos: {distancia:.3f}")