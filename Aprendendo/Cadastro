a = 0

while(a == 0):

    nomecadastro = str(input("Digite o seu nome: "))

    if(nomecadastro.isalpha() and nomecadastro.istitle() and nomecadastro.find(" ") == -1):
        print("Você está cadastrado!")
        nomecadastro = nomecadastro.lower()
        nomecadastro = nomecadastro.capitalize()
        a = 1
    
    else:
        print("Nome inválido. Lembre-se de usar apenas o seu primeiro nome.")

    
escolha = "N"

while(escolha == "N"):

    senha = str(input("Escolha a sua senha: "))

    if(len(senha) < 8):
        print("Senha muito pequena.")

    elif(len(senha) >= 8 and senha.find(" ") != -1):
        print("Senha inválida.")

    elif(len(senha) >= 8 and (senha.isalpha() or senha.isdigit() or senha.isspace())):
        print("Senha muito fraca.")

    elif(len(senha) >= 8 and (senha.isascii() and not senha.isalnum())):
        print("Senha escolhida!")
        escolha = "S"

    elif(len(senha) >= 8 and ((not senha.islower() and not senha.isupper() and senha.isalnum() and (not senha.isalpha() and not senha.isdigit())))):
        escolha = str(input("Senha moderada. Continuar com essa senha? (S/N): "))

    else:
        print("Senha inválida")
