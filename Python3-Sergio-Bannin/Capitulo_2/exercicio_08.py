"""Escreva em Python as seguintes expressões aritméticas para as
 fórmulas a seguir e teste as quatro primeiras para os valores A = 4, B
 = 5, C = 1 e a última para os valores x1 = 1, y1 = 1, x2 = 4 e y2 = 5.
"""
A = 4
B = 5
C = 1
X1 = 1
Y1 = 1
X2 = 4
Y2 = 5

# R = A + B/2
R = (A + B) / 2
print(R)
# X = - B + RAIZ B**2 - 4A*C/2*A
import math 
X = (-B + (math.sqrt(B**2) - 4*A*C)) / (2*A)
print(X)
# R = (3*A + 2*B)/(A+B)
R = (3*A + 2*B)/(A + B)
print(f"{R:.2f}")
# Z = 7.6*A - B**1.7
Z = 7.6 * A - pow(B, 1.7)
print(Z)
# D = RAIZ (X1 - X2)**2 + (Y1 - Y2)**2
D = math.sqrt((X1 - X2)**2 + (Y1 -Y2)**2)
print(D)