def criar_matriz(n_linhas, n_coluna, valor):
    #lista vazia
    matriz = []
    for i in range(n_linhas):
        linha= []
        for j in range(n_coluna):
            linha.append(valor)
        matriz.append(linha)
    return matriz


a = criar_matriz(4,4,0)
print(a)
