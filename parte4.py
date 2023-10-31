from collections import deque

def dfs(grafo, vertice, arvore=None):
    if arvore is None:
        arvore = {}
    pilha = [vertice]
    visita = set()

    while pilha:
        atual = pilha.pop()
        if atual not in visita:
            visita.add(atual)
            for vizinho in grafo[atual]:
                if vizinho not in visita:
                    arvore[vizinho] = atual
                    pilha.append(vizinho)
    return arvore

def bfs(grafo, vertice_inicial):
    fila = deque([vertice_inicial])
    visita = {}
    while fila:
        vertice = fila.popleft()
        for vizinho in grafo[vertice]:
            if vizinho not in visita:
                visita[vizinho] = vertice
                fila.append(vizinho)
    return visita


grafo = {
    1: [2, 3],
    2: [4],
    3: [5],
    4: [1],
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