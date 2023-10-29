import sys

def algoritmoDijkstra(grafo, origem):
    print(f"-----> ALGORITMO DE DIJKSTRA <-----")  
    distancia = {no: sys.maxsize for no in grafo}
    distancia[origem] = 0
    visitado = set()
    caminho = {}

    while len(visitado) < len(grafo):
        #Busca o nó visitado com a distância minima
        min_distancia = sys.maxsize
        min_no= None
        for no in grafo:
            if no not in visitado and distancia[no] < min_distancia:
                min_distancia = distancia[no]
                min_no = no
        
        #Marca o atual como visitado
        visitado.add(min_no)
        
        #Atualiza as distancias dos nós 
        for vizinho, peso in grafo[min_no].items():
            if distancia[min_no] + peso < distancia[vizinho]:
                distancia[vizinho] = distancia[min_no] + peso
                caminho[vizinho] = min_no
    return distancia, caminho

def algoritmoBellmanFord(grafo, origem):
    print(f"-----> ALGORITMO DE BELLMAN-FORD <-----")  
    distancia = {no: sys.maxsize for no in grafo}
    distancia[origem] = 0
    visitado = set()
    caminho = {}

    for n in range(len(grafo)-1):
        #Por todas as arestas (u, v, w)
        for u, edges in grafo.items():
            for v, peso in edges.items():
                #Atualiza a distancia -> caminho menor
                if distancia[u] + peso < distancia[v]:
                    distancia[v] = distancia[u] + peso
   
    #Verifica ciclos negativos -> Cai em exceção
    for u, arest in grafo.items():
        for v, pe in arest.items():
            if distancia[u] + pe < distancia[v]:
                raise ValueError(f"Ciclo negativo!!!")
                    
    return distancia

def algoritmoFloydWarshall(grafo):
    print(f"-----> ALGORITMO DE FLOYD WARSHALL <-----")  
    nos = grafo
    tamhanhoGrafo = len(grafo)
    
    #Aplicação do algoritmo deloyd
    for w in range(tamhanhoGrafo):
        for i in range(tamhanhoGrafo):
            for j in range(tamhanhoGrafo):
                nos[i][j] = min(nos[i][j], nos[i][w] + nos[w][j])                
    return nos

def imprimirMatrizFinal(nos):
    print(f"-> Matriz final")
    for no in nos:
        for item in no:
            print("%s\t" % item, end="")
        print("")
        
def imprimirMatrizInicio(grafo):
    print(f"-> Matriz inicial")
    for gra in grafo:
        for item in gra:
            print("%s\t" % item, end="")
        print("")

def imprimirVertices(grafo):
    print(f"-> Informações passadas sobre o grafo")
    for gra in grafo.items():
        print(gra)

def imprimirDistanciaMinima(distancias, origemVertice):
    print(f"-> Distância miníma entre os vértices")
    for no, distancia in distancias.items():
        print(f"{origemVertice}-{no}: {distancia}")
    
def imprimirCaminhoMinimo(grafoInicial, origemVertice, caminho):
    print(f"-> Caminho de um vértice para outro")
    for no in grafoInicial:
        if no != origemVertice:
            path = []
            noAtu = no
            while noAtu in caminho:
                path.insert(0, noAtu)
                noAtu = caminho[noAtu]
            path.insert(0, origemVertice)
            print(f"{origemVertice}-{no}: {' -> '.join(path)}")
    
    
# Grafo não direcionado
grafoInicial_1Dijkstra = {
    'A': {'B': 5, 'C': 2},
    'B': {'A': 5, 'C': 1, 'D': 3},
    'C': {'A': 2, 'B': 1, 'D': 2},
    'D': {'B': 3, 'C': 2, 'E': 4},
    'E': {'D': 4}
}
#Grafos direcionados
grafoDijkstra = {
    'A': {'B': 100, 'C': 30},
    'B': {'C': 20},
    'C': {'D': 10, 'E': 60},
    'D': {'B': 15, 'E': 50},
    'E': {}
}
grafo_1BellmanFord = {
    'A': {'B': -1, 'C': 4},
    'B': {'C': 3, 'D': 2, 'E': 2},
    'C': {},
    'D': {'B': 1, 'C': 5},
    'E': {'D': -3}
}
grafoBellmanFord = {
    'A': {'B': 10, 'C': 5},
    'B': {'C': 2, 'D': -7},
    'C': {'B': 3, 'D': 9, 'E': -2},
    'D': {'E': 4},
    'E': {'D': 6}
}
origemVertice = 'A'

print(f'---------- DIJKSTRA ----------')
distancias, caminho = algoritmoDijkstra(grafo=grafoDijkstra, origem=origemVertice)
imprimirVertices(grafoDijkstra)
imprimirDistanciaMinima(distancias=distancias, origemVertice=origemVertice)

print(f'---------- BELLMAN FORD ----------')
distancia = algoritmoBellmanFord(grafoBellmanFord, origemVertice)
imprimirVertices(grafoBellmanFord)
imprimirDistanciaMinima(distancia, origemVertice)

print(f'---------- FLOYD WARSHALL ----------')
#Representando infinito
INF = float("inf")
#Matriz base
grafo = [[0, 1, 2, INF],
        [INF, 0, 3, -1],
        [INF, INF, 0,   -2],
        [INF, 2, INF, 0]
        ]
no = algoritmoFloydWarshall(grafo)
imprimirMatrizInicio(grafo)
imprimirMatrizFinal(no)