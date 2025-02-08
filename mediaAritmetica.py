lista = []
print(("Digite os numeros da lista aritmetica, e ao terminar digite sair.\n"))
while True:
    novoNumero = input()
    if novoNumero == "sair":
        break
    else:
        novoNumero = int(novoNumero)
        lista.append(novoNumero)

def mediaAritmetica(lista):
    tamanho = 0
    soma = 0
    for item in lista:
        tamanho += 1
    for numero in lista:
        soma += numero

    return print(soma / tamanho)

mediaAritmetica(lista)