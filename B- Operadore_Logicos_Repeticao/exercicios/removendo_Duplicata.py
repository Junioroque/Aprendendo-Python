# Leitura da linha de identificadores de transações
entrada = input()

# TODO: Crie uma lista com as transações sem duplicatas, mantendo a ordem da primeira ocorrência
lista_transacoes = entrada.split()
transacoes_unicas = []
# Dica: Percorra cada transação e adicione à lista apenas se ainda não estiver presente

for transacao in lista_transacoes:
    if transacao not in transacoes_unicas:
        transacoes_unicas.append(transacao)

# Descomente após implementar a lógica

print(' '.join(transacoes_unicas))