'class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro=16):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = 26
         
    def buzinar(self):
        print("Plin plin...")
            
    def parar(self):
        print("Parando bicicleta.")
        print("Bicicleta parada.")
        
    def correr(self):
        print("Vrummmmmmmm...")
        
   # def __str__(self):
   #     return f'{self.__class__.__name__}: {', '.join(f'{chave} = {valor}' for chave, valor in self.__dict__.items())}'
        
tipo = Bicicleta('vermelha', 'caloi', 2020, 500.00)
print(f'A bicicleta é {tipo.modelo}, cor {tipo.cor}, do ano {tipo.ano} e custa R$ {tipo.valor:.2f}.')

tipo.buzinar()
tipo.correr()
tipo.parar()    

#Acessar os atributos da classe Bicicleta
print(f'''
      cor: {tipo.cor} 
      modelo: {tipo.modelo} 
      ano: {tipo.ano} 
      valor: {tipo.valor:.2f}''')

print('-----------------------------')

tipo2 = Bicicleta('azul', 'monark', 2021, 600.00)

tipo2.buzinar()
tipo2.correr()  
print(f''' Bicicleta: {tipo2.modelo}:      
      cor: {tipo2.cor} 
      ano: {tipo2.ano} 
      valor: {tipo2.valor:.2f}''')


print(tipo)
print(tipo2)