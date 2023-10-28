
def detalheGrafo(nomeArquivo):
    """Nesta função será recebido um arquivo txt com as informações do grafo, e ela retornará os detalhes da mesma por print já.

    Args:
        nomeArquivo (string): O nome do arquivo txt com os dados do grafo
    """
    with open(nomeArquivo, 'r') as arquivo:
        nomeGrafo, numeroVertices, numeroArestas = arquivo.readline().split()
        numeroVertices = int(numeroVertices)
        numeroArestas = int(numeroArestas)
        
        listaAdjacencia = [[] for _ in range(numeroVertices + 1)]
        
        for _ in range(numeroArestas):
            vi, vj, peso = map(float,arquivo.readline().split())
            listaAdjacencia[int(vi)].append((int(vj), peso))
   
        return nomeGrafo, numeroVertices, numeroArestas, listaAdjacencia

# Nome do arquivo de texto
arquivoText = "arquivoTexto.txt"

# Passando as informações do grafo para detalheGrafo(arquivoText)
nomeGrafo, numeroVertices, numeroArestas, listaAdjacencia  = detalheGrafo(arquivoText)

# Exibindo as informações do grafo
print(f'\n--------- Informações do grafo ---------')
print(f'-> Nome do Grafo: {nomeGrafo}')
print(f'-> Número de Vértices: {numeroVertices}')
print(f'-> Número de Arestas: {numeroArestas}')
print(f'-> Informações das arestas:')

for vertice, vizinhos in enumerate(listaAdjacencia):
        for vizinho, peso in vizinhos:
            print(f"Vértice {vertice} - Vértice {vizinho} \t| Peso: {peso}")