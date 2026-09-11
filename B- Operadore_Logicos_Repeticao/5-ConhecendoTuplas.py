def soma_tupla(numeros):
    """
    Recebe uma tupla de números inteiros e retorna a soma de todos os elementos.
    
    Parâmetros:
    numeros (tuple): Uma tupla contendo números inteiros.
    
    Retorno:
    int: A soma de todos os elementos da tupla.
    """
    return sum(numeros)

# Exemplo de uso:
entrada = input("Digite os números inteiros separados por espaço: ")
lista_strings = entrada.split()  # Divide a string de entrada em uma lista de strings

# Converte cada string para inteiro e cria uma tupla
elementos = tuple(map(int, lista_strings))

resultado = soma_tupla(elementos)
print(f"A soma dos elementos da tupla é: {resultado}")
