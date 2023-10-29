from collections import deque

def novoGrafo():
    """ NovoGrafo(): Retorna um grafo vazio, ou seja, com apenas um novo vértice """
    return {1: {}}  

def grafo(g):
    """ Grafo(G): Retorna uma representação por listas de adjacências de G """
    return g

def eVertice(G, v):
    """ EVertice(G, v): Verifica se v ∈ V (G) ou não

    Args:
        G (dict): Será passado o grafo
        v (int): Será passado o vértice desejado

    Returns:
        boolean: Retorna True se v ∈ V(G) (v está no dicionário G), False caso contrário.
    """
    return v in G 
 
def addAresta(grafo, vi, vj, peso):
    """ AddAresta(G, vi, vj , ω): Adiciona uma aresta em G entre os vértices vi e vj com peso ω. Deve verificar se vi , vj ∈ V (G), caso contrário a operação não poderá ser efetuada

    Args:
        grafo (dict): Será passado o grafo
        vi (int): Será passado o vértice
        vj (int): Será passado o vértice
        peso (int): Será passado o peso

    Returns:
        dict: Retorna o grafo
    """
    if vi in grafo and vj in grafo:
        grafo[vi][vj] = peso  
        grafo[vj][vi] = peso
    else:
        print("Que pena Vi ou Vj não pertence ao Grafo")
    return grafo

def removeAresta(grafo, vi, vj, peso):
    """ RemoveAresta(G, vi, vj , ω): Remove uma aresta em G entre os vértices vi e vj com peso ω. Deve verificar se vi , vj ∈ V (G) e se existe uma tal aresta, caso contrário a operação não poderá ser efetuada

    Args:
        grafo (dict): Será passado o grafo
        vi (int): Será passado o vértice
        vj (int): Será passado o vértice
        peso (int): Será passado o peso

    Returns:
        dict: Retorna o grafo
    """
    
    if vi in grafo and vj in grafo and grafo[vi].get(vj) == peso:
        del grafo[vi][vj] 
        del grafo[vj][vi]
    else:
        print("Que pena Vi ou Vj não pertence ao Grafo")
    return grafo

def existeAresta(G, vi, vj, ω):
    """ ExisteAresta(G, vi, vj , ω): Verifica se existe uma aresta em G entre os vértices vi e vj com peso ω.

    Args:
        grafo (dict): Será passado o grafo
        vi (int): Será passado o vértice
        vj (int): Será passado o vértice

    Returns:
        boolean: Retorna se existe uma aresta entre vi e vj, True se existir, False senão existir
    """
    
    if vi in G and vj in G and G[vi].get(vj) == ω:
        return True
    else:
        return False

def mudaPeso(G, vi, vj, w, ww):
    """ MudaPeso(G, vi, vj , ω, ω′): Modifica valor de peso de uma aresta em G entre os vértices vi e vj de valor ω para o valor ω′. Deve verificar se vi, vj ∈ V (G) e se existe uma tal aresta, caso contrário a operação não poderá ser efetuada

    Args:
        G (dict): Será passado o grafo
        vi (int): Será passado o vértice
        vj (int): Será passado o vértice
        w (int): Será passado o peso a ser trocado
        ww (int): Será passado o peso que irá ficar após a troca

    Returns:
        dict: Retorna o grafo após a alteração
    """
    if vi in G and vj in G and G[vi].get(vj) == w:
        G[vi][vj] = ww
    else:
        print("Erro: vi ou vj não pertencem a V(G) ou a aresta com o peso ω não existe.")
    return G
 
def imprimeGrafo(G):
    """ImprimeGrafo(G): Imprime todos os vértices e arestas de G

    Args:
        G (dict): Fornece o Grafo
    """
    for vi in G:
        for vj, peso in G[vi].items():
            print(f" * Vértice: {vi} - Vértice {vj}  | Peso: {peso}")

def removeGrafo(G):
    """RemoveGrafo(G): Libera todo o espaço utilizado pela representação de G

    Args:
        G (dict): Passa o grafo

    Returns:
        dict: Retorna o grafo
    """
    G.clear()
    return G
        
def recuperaPeso(G, vi, vj):
    """RecuperaPeso(G, vi, vj ): Devolve a lista de pesos de todas as arestas entre os vértices vi e vj em V (G). Deve verificar se vi, vj ∈ V (G), caso contrário a operação não poderá ser efetuada

    Args:
        G (dict): Será passado o grafo
        vi (int): Será passado o vértice
        vj (int): Será passado o vértice
    """
    if vi in G and vj in G and vj in G[vi]:
        
        return G[vi][vj]
    else:
        print("Erro: vi ou vj não pertencem a V(G). A operação não pode ser efetuada.")
        return []

def grafoSimples(G):
    """GrafoSimples(G): Retorna se o grafo G é um grafo simples ou não

    Args:
        G (dict): Fornencendo o grafo desejado

    Returns:
        boolean: Retorna True caso o grafo seja simples, e False se ele não for simples, por exemplo se existir mais de uma arestas entre os mesmos vértices, se há laços
    """
    for vi in G:
        if len(G[vi]) != len(set(G[vi].values())):
            return False
        if vi in G[vi]:
            return False
    return True

def eArvore(G):
    """ EArvore(G): Retorna se o grafo G é uma árvore ou não. 
    Extra: Verifica se o grafo é conectado. Se há ciclos no grafo. Se o grafo é acíclico e conectado, e não possui vértices isolados, é uma árvore
    
    Args:
        G (dict): Passa o Grafo
        
    Returns:
        _type_: _description_
    """
    def conectado(v, visited):
        visited[v] = True
        for neighbor in G[v]:
            if not visited[neighbor]:
                conectado(neighbor, visited)
    def ciclo(v, visited, parent):
        visited[v] = True
        for neighbor in G[v]:
            if not visited[neighbor]:
                if ciclo(neighbor, visited, v):
                    return True
            elif neighbor != parent:
                return True
        return False
    visited = {v: False for v in G}
    connected_components = 0
    for v in G:
        if not visited[v]:
            conectado(v, visited)
            connected_components += 1
    return connected_components == 1 and not ciclo(list(G.keys())[0], {v: False for v in G}, None) and all(visited.values())

def eBipartido(G):
    """ EBipartido(G): Retorna se o grafo G é bipartido ou não

    Args:
        G (dict): Grafo fornecido
    """
    def bfs(v):
        queue = deque([v])
        color[v] = 0
        while queue:
            current_vertex = queue.popleft()

            for neighbor in G[current_vertex]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[current_vertex]
                    queue.append(neighbor)
                elif color[neighbor] == color[current_vertex]:
                    return False
        return True
    color = {v: -1 for v in G}
    for v in G:
        if color[v] == -1:
            if not bfs(v):
                return False
    return True

def complementoG(G):
    """ Complemento(G): Retorna o grafo complementar G de G

    Args:
        G (dict): Grafo passado
    """
    complemento = {v: {} for v in G}
    for vi in G:
        for vj in G:
            if vi != vj and vj not in G[vi]:
                complemento[vi][vj] = 1
    return complemento

def eAdj(G, vi, vj):
    """ EAdj(G, vi, vj ): Verifica se vivj ∈ E(G)

    Args:
        G (dict): Será passado o grafo
        vi (int): Será passado o vértice
        vj (int): Será passado o vértice

    Returns:
        boolean: Retorna True ou False verificando se vivj pertence E(G)
    """
    if vi in G and vj in G[vi]:
        return True
    else:
        return False

def adjacencia(G, v):
    """ Adjacencia(G, v): Devolve a lista de adjacência de v em G. Deve verificar se v ∈ V (G), caso contrário a operação não poderá ser efetuada

    Args:
        G (dict): Grafo desejado
        v (int): Vértice desejado
    """
    if v in G:
        return list(G[v].keys())
    else:
        print("Erro: v não pertence a V(G). A operação não pode ser efetuada.")
        return []

def incidencia(G, v):
    """Incidencia(G, v): Devolve as arestas incidentes a v em G. Deve verificar se v ∈ V (G), caso contrário a operação não poderá ser efetuada

    Args:
        G (dicst): Passa o grafo desejado
        v (int): Fornece o vértice

    """
    if v in G:
        arestas_incidentes = []
        for vi in G:
            if v in G[vi]:
                arestas_incidentes.append((vi, v, G[vi][v]))  # Aresta (vi, v, peso)
        return arestas_incidentes
    else:
        print("Erro: v não pertence a V(G). A operação não pode ser efetuada.")
        return []

def matrizAdj(G):
    """ MatrizAdj(G): Constrói a matriz de adjacência de G, onde a posição ai,j corresponde ao peso da aresta vivj, para todo 1 ≤ i ≤ j ≤ n

    Args:
        G (dict): Passa o grafo desejado
    """
    vertices = list(G.keys())
    n = len(vertices)
    
    matriz_adj = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(i, n):
            vi, vj = vertices[i], vertices[j]
            if vi in G and vj in G[vi]:
                matriz_adj[i][j] = G[vi][vj]
                matriz_adj[j][i] = G[vi][vj]
    return matriz_adj

def imprimeMatrizAdj(G):
    """ ImprimeMatrizAdj(G): Imprime a matriz de adjacência de G. Primeiro vai obter a matriz de adjacência do grafo, e depois vai imprimir a mema

    Args:
        G (dict): Passa o grafo desejado
    """
    matriz_adj = matrizAdj(G)
    
    for row in matriz_adj:
        print(" ".join(map(str, row)))

def conexo(G):
    """ Conexo(G): Retorna se G é conexo ou não.

    Args:
        G (dict): Fornece o grafo desejado

    Returns:
        boolean: Vai retornar True ou False na verificação dele ser conexo ou não
    """
    if not G:
        return True
    
    start_vertex = next(iter(G))
    visited = {v: False for v in G}
    queue = deque([start_vertex])
    
    while queue:
        current_vertex = queue.popleft()
        visited[current_vertex] = True
        for neighbor in G[current_vertex]:
            if not visited[neighbor]:
                queue.append(neighbor)
    return all(visited.values())


print(f'----> Resultado final\n')
grafoTeste = {
    1: {2: 3}, 
    2: {1: 3, 3: 4}, 
    3: {2:4}}
grafoTesteComplementar = {
    1: {2: 1},
    2: {1: 1, 4: 1},
    3: {1: 1, 4: 1},
    4: {2: 1}
}

print(f'-> Novo Grafo\n', novoGrafo())
print(f'-'*50)
print(f'-> Grafo representação por listas de adjacências\n', grafo(grafoTeste))
print(f'-'*50)
print(f'-> Verifica vértice\n', eVertice(grafoTeste, 4))
print(f'-'*50)
print(f'-> Adicionando aresta\n', addAresta(grafoTeste, 1, 3, 10))
# print(f'-'*50)
#print(f'-> Removendo aresta\n', removeAresta(grafoTeste, 1, 2, 3))
print(f'-'*50)
print(f'-> Verifica se existe Aresta\n', existeAresta(grafoTeste, 1, 3, 1)) # 1, 2, 3
print(f'-'*50)
print(f'-> Modifica o peso de uma aresta em G\n', mudaPeso(grafoTeste, 1, 2, 3, 5))
print(f'-'*50)
print(f'-> Todos os vértices:')
imprimeGrafo(grafoTeste)
print(f'-'*50)
print(f'-> Devolve peso das arestas entre os vértices passados\n', recuperaPeso(grafoTeste,3,1))
print(f'-'*50)
print(f'-> Verifica se é um Grafo Simples\n', grafoSimples(grafoTeste))
print(f'-'*50)
print(f'-> Verifica se é uma árvore\n', eArvore(grafoTeste))
print(f'-'*50)
print(f'-> Verifica se é Bipartido\n', eBipartido(grafoTeste))
print(f'-'*50)

print(f'-> Complementar\n', complementoG(grafoTesteComplementar))
print(f'-'*50)
print(f'-> Verifica se vivj ∈ E(G)\n', eAdj(grafoTesteComplementar, 1,3))
print(f'-'*50)
print(f'-> Lista de adjacência de v em G\n', adjacencia(grafoTesteComplementar, 2))
print(f'-'*50)
print(f'-> Arestas incidentes a v em G\n', incidencia(grafoTesteComplementar, 2))
print(f'-'*50)

print(f'-> Constrói a matriz de adjacência de G\n', matrizAdj(grafoTeste))
print(f'-'*50)
print(f'-> Imprime a matriz de adjacência de G')
imprimeMatrizAdj(grafoTeste)
print(f'-'*50)
print(f'-> Grafo Conexo\n', conexo(grafoTeste))
print(f'-'*50)

print(f'-> Liberando todo o espaço utilizado pela representação de G: \n', removeGrafo(grafoTeste))