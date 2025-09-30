def fatorial(n):
    if n == 0:
        return 1
    
    if n > 0:
        return n * fatorial(n-1)

Palavra = str(input("Digite a palavra: "))

Palavra = Palavra.lower()

Permutações = fatorial(len(Palavra))

while not Palavra == "":
    Letra = Palavra[0]
    x = Palavra.count(Letra)
    Permutações = Permutações/fatorial(x)
    Palavra = Palavra.replace(f'{Letra}', '')

print(Permutações)
