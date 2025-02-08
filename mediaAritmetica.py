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
    return print(sum(lista) / len(lista))

mediaAritmetica(lista)