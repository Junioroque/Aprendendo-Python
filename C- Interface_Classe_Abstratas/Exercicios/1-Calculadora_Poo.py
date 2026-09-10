# TODO: Crie uma classe e método para realizar a soma:

class Calculadora:
  
  def __init__(self, num1=None, num2=None):
      self.num1 = num1
      self.num2 = num2
  
  
Calculadora.num1 = int(input())
Calculadora.num2 = int(input())

 
# Criando uma instância da calculadora
calc = Calculadora()

resultado = calc.soma(num1, num2)
print(resultado)