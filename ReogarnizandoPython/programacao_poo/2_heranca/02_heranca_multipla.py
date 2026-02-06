class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
        
    def __str__(self):
        return f'{self.__class__.__name__}: {", ".join
    (f"{chave} = {valor}" for chave, valor in self.__dict__.items())}'
        
    
class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)
        
class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw) 
        
class FalarMixin:
    def falar(self):
        return 'Oi estou falando...'
        
class Ornitorrinco(Mamifero, Ave, FalarMixin):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        super().__init__(cor_bico=cor_bico, cor_pelo=cor_pelo, nro_patas=nro_patas)
        
        
class Cachorro(Mamifero):
    pass
    
class Gato(Mamifero):
    pass
    
class Leao(Mamifero):
    pass


gato = Gato(nro_patas=4, cor_pelo='cinza')
print(gato)

print('-----------------------------')

ornitorrinco = Ornitorrinco(nro_patas=5, cor_bico='amarelo', cor_pelo='marrom')
print(ornitorrinco)
print(ornitorrinco.falar())