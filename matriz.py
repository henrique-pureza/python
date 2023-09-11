from subprocess import call

call("clear")

matriz = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

for i in range(1, len(matriz) + 1):
    for j in range(1, len(matriz[i - 1]) + 1):
        if i == j:
            matriz[i - 1][j - 1] = -i + j
        elif i != j:
            matriz[i - 1][j - 1] = i*j

for linha in matriz:
    for elem in linha:
        print(elem, end=" ")
    print()
