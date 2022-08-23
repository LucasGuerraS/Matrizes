lista = []

for i in range(3):
    lista.append(["_"] * 3)

for i in lista:
    print(i)

# for i in lista:
#     for x in range(3):
#         print(i[x])


def mudarX( linha,coluna):
    lista[linha -1][coluna -1] = "X"

def mudarO( linha,coluna):
    if (lista[linha -1][coluna -1] == "_"):
        lista[linha -1][coluna -1] = "O"
    else:
        print("Já existe um X nessa posição")

mudarX( 1, 2)

print("-----------------------")
print(lista[0])
print(lista[1])
print(lista[2])
print("-----------------------")


mudarO(2,3)
print("-----------------------")
print(lista[0])
print(lista[1])
print(lista[2])
print("-----------------------")

mudarO(1,2)
print("-----------------------")
print(lista[0])
print(lista[1])
print(lista[2])
print("-----------------------")
