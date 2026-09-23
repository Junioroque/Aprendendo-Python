resposta = "SIM";

while resposta == "SIM":
    nivel = input("Digite o nível de acesso: ").upper();
    
    if nivel == "ADM" or nivel == "USER":
        genero = input("Digite o sue gênero (MASCULINO ou FEMININO): ").upper();
        
        if nivel == "ADM":
            if genero == "FEMININO":
                print("Olá, Administradora!");
            else:
                print("Olá, Administrador!");
        else:
            if genero == "FEMININO":
                print("Olá, Usuária!");
            else:
                print("Olá, Usuário!");
    elif nivel == "GUEST":
        print("Olá, Visitante!");
    else:
        print("Olá desconhecido(a)!");
    resposta = input("Deseja continuar? (SIM ou NAO): ").upper();