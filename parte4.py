from collections import deque

def dfs(grafo, vertice, visitados=None, arvore=None, vertice_inicial=None):
    if visitados is None:
        visitados = set()
    if arvore is None:
        arvore = {}
    visitados.add(vertice)
    if vertice_inicial is not None and vertice not in arvore:
        arvore[vertice] = vertice_inicial
    for vizinho in grafo[vertice]:
        if vizinho not in visitados:
            dfs(grafo, vizinho, visitados, arvore, vertice)
    return arvore

def bfs(grafo, vertice_inicial):
    fila = deque([vertice_inicial])
    visitados = {}
    # visitados = {vertice_inicial: None}  # O vértice inicial não tem pai na árvore de busca
    while fila:
        vertice = fila.popleft()
        for vizinho in grafo[vertice]:
            if vizinho not in visitados:
                visitados[vizinho] = vertice  # Registra a aresta na árvore de busca
                fila.append(vizinho)
    return visitados


grafo = {
    1: [2, 3],
    2: [4],
    3: [5],
    4: [],
    5: []
}
vertice_inicial = 1
arvore_de_buscaBFS = bfs(grafo, vertice_inicial)
arvore_de_buscaDFS = dfs(grafo, vertice_inicial)

print("--> Árvore de Busca gerada pelo DFS(Profundidade):")
for vertice, pai in arvore_de_buscaDFS.items():
    print(f"Vértice {vertice} foi alcançado a partir do vértice {pai}")
    
print("\n--> Árvore de Busca gerada pelo BFS(Largura):")
for vertice, pai in arvore_de_buscaBFS.items():
    print(f"Vértice {vertice} foi alcançado a partir do vértice {pai}")