import random

def Checar_Vitória():
    for c in range(0, 3):
        if((Tabuleiro[c][0] == Tabuleiro[c][1] and Tabuleiro[c][0] == Tabuleiro[c][2] and Tabuleiro[c][0] != '.') or (Tabuleiro[0][c] == Tabuleiro[1][c] and Tabuleiro[0][c] == Tabuleiro[2][c] and Tabuleiro[0][c] != '.')):
            return 1
    
    if((Tabuleiro[1][1] == Tabuleiro[0][0] and Tabuleiro[1][1] == Tabuleiro[2][2] and Tabuleiro[1][1] != '.') or (Tabuleiro[1][1] == Tabuleiro[0][2] and Tabuleiro[1][1] == Tabuleiro[2][0] and Tabuleiro[1][1] != '.')):
        return 1
    
    else:
        return 0


Linha1 = [".", ".", "."]
Linha2 = [".", ".", "."]
Linha3 = [".", ".", "."]

i = 0

while(i < 9):

    Linha = random.randint(0, 2)
    Coluna = random.randint(0, 2)

    Tabuleiro = [Linha1, Linha2, Linha3]

    if Tabuleiro[Linha][Coluna] != '.':
        continue

    Tabuleiro[Linha][Coluna] = "X"

    i = i + 1

    if(i == 9):
        break

    for z in range(0, 3):
        print(Tabuleiro[z])
    
    print()
    
    checar = Checar_Vitória()

    if(checar == 1):
        print()
        print("X ganhou")
        break

    while True:
        Linha_Usuário = int(input("Digite a linha: "))
        Coluna_Usuário = int(input("Digite a coluna: "))

        if Tabuleiro[Linha_Usuário][Coluna_Usuário] != '.':
            print("Quadro inválido.")
        
        else:
            Tabuleiro[Linha_Usuário][Coluna_Usuário] = "O"
            i = i + 1
            break
    
    checar = Checar_Vitória()

    if(checar == 1):
        print()
        print("O ganhou")
        break

        
print()

for i in range(0, 3):
    print(Tabuleiro[i])
