import random

Tabuleiro = [[0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

i = 0

pontos = 0
contador = 0

while i < 5:

    while True:
        Orientação = random.randint(1, 2) # Define a orientação
        Tamanho = random.randint(1, 2) # Define o tamanho
        x = random.randint(0, 4) # Define a linha
        y = random.randint(0, 4) # Define a coluna

        if Tabuleiro[x][y] == 0 and Tamanho == 1:
            Tabuleiro[x][y] = 1
            i = i + 1
            break

        elif Tabuleiro[x][y] == 0 and Tamanho == 2 and Orientação == 1 and i != 4:
            if y < 4:
                if Tabuleiro[x][y + 1] == 0:
                    Tabuleiro[x][y] = 2
                    Tabuleiro[x][y + 1] = 2
                    i = i + 2
                    break
            
            if y > 0:
                if Tabuleiro[x][y - 1] == 0:
                    Tabuleiro[x][y] = 2
                    Tabuleiro[x][y - 1] = 2
                    i = i + 2
                    break
                
        elif Tabuleiro[x][y] == 0 and Tamanho == 2 and Orientação == 2 and i != 4:
            if x < 4:
                if Tabuleiro[x + 1][y] == 0:
                    Tabuleiro[x][y] = 2
                    Tabuleiro[x + 1][y] = 2
                    i = i + 2
                    break
            
            if x > 0:
                if Tabuleiro[x - 1][y] == 0:
                    Tabuleiro[x][y] = 2
                    Tabuleiro[x - 1][y] = 2
                    i = i + 2
                    break

        else:
            continue


while True:
    
    LinhaU = int(input("Digite a linha: "))
    ColunaU = int(input("Digite a coluna: "))

    if LinhaU > 4 or LinhaU < 0 or ColunaU > 4 or ColunaU < 0:
        print("Quadro inválido")
        continue

    # LinhaU = random.randint(0, 4)
    # ColunaU = random.randint(0, 4)

    if Tabuleiro[LinhaU][ColunaU] == 1: # Confere se o valor da casa é 1, concede um ponto se sim, aumenta o contador e modifica o valor da casa para não poder ser escolhida de novo
        print("Você ganhou um ponto")
        print()
        pontos += 1
        contador += 1
        Tabuleiro[LinhaU][ColunaU] = 10
    
    elif Tabuleiro[LinhaU][ColunaU] == 2:
        print("Você ganhou um ponto")
        print()
        pontos += 1
        contador += 1
        Tabuleiro[LinhaU][ColunaU] = 11
    
    elif Tabuleiro[LinhaU][ColunaU] == 0:
        Tabuleiro[LinhaU][ColunaU] = 7
        contador += 1
    
    else:
        print("Quadro já escolhido")
        continue

    print("------------------------------------")

    for n in range(0, 5):
        for z in range(0,5):
            if Tabuleiro[n][z] == 10:
                print("\033[0;31m1\033[0m", end =" ")
            
            elif Tabuleiro[n][z] == 11:
                print("\033[0;31m2\033[0m", end = " ")
            
            elif Tabuleiro[n][z] == 7:
                print("\033[0;34m0\033[0m", end = " ")
            
            else:
                print("0", end = " ")
        
        print()
    
    print("------------------------------------")
    
    print()

    if pontos == 5:
        break

    if contador == 15:
        break


for i in range(0, 5):
    for j in range(0, 5):
        if Tabuleiro[i][j] == 1 or Tabuleiro[i][j] == 10:
            print(1, end = " ")
        
        elif Tabuleiro[i][j] == 2 or Tabuleiro[i][j] == 11:
            print(2, end = " ")
        
        else:
            print(0, end = " ")
        
    print()


print()

print(f"Você ganhou {pontos} pontos")
