def train(N):
    lista_buena = []
    distancia = input()
    tiempo = input()
    distancia = distancia.split()
    tiempo = tiempo.split()
    for i in range(len(distancia)):
        distancia[i] = int(distancia[i])
    for i in range(len(tiempo)):
        tiempo[i] = int(tiempo[i])
    
    tiempo.insert(tiempo[2], distancia[0])
    lista_buena = tiempo.copy()
    print(tiempo)
    print(lista_buena)
    print(tiempo[2])
    lista_buena.insert(lista_buena[2], distancia[1])
    print(tiempo)
    print(lista_buena)x

e = int(input())
train(e)