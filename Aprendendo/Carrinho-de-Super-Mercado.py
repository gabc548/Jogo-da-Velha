Produtos = ["Leite", "Arroz", "Maçã", "Feijão", "Carne de boi"]
Preços = ["5.00", "10.00", "2.00", "13.00", "50.00"]

Preço = 0

for x in range(0, 5):
    print(f"Produto: {Produtos[x]}, preço: {Preços[x]}")

while True:

    print("")

    Produto = input("Digite o produto que gostaria de comprar (s para sair e encerrar o carrinho): ")
    if Produto.lower() == "s":
        break

    Produto = Produto.lower() #Uniformiza a entrada do usuário
    Produto = Produto.capitalize()

    if Produto not in Produtos: #Checa se o produto está na lista
        print("O produto não está na lista")
        continue

    print("")

    Posição = Produtos.index(Produto) #Pega a posição do produto na lista para uso futuro

    Quantidade = float(input("Digite a quantidade ou o peso: "))
    if Quantidade < 0:
        print("A quantidade ou o peso não pode ser menor que 0")
        continue

    Preço_individual = float(Preços[Posição]) * Quantidade #Calcula o preço individual do produto da atual repetição, usando a posição adquirida anteriormente
    Preço = Preço + Preço_individual

print("")

print(f"Preço total = R${Preço:.2f}")
