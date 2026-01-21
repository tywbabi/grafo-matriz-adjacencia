import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# Cria uma matriz de adjacência 4x4 inicializada com zeros
matriz_adjacencia = [[0, 0, 0, 0],
		                 [0, 0, 0, 0],
                     [0, 0, 0, 0],
		                 [0, 0, 0, 0]]

# Defina as arestas no grafo
aresta_AB = 1
aresta_AC = 1
aresta_BA = 1
aresta_BD = 1
aresta_CA = 1
aresta_DB = 1

# Preenche a matriz de adjacência com as informações das arestas
matriz_adjacencia[0][1] = aresta_AB # A está conectado a B
matriz_adjacencia[0][2] = aresta_AC # A está conectado a C
matriz_adjacencia[1][0] = aresta_BA # B está conectado a A
matriz_adjacencia[1][3] = aresta_BD # B está conectado a D
matriz_adjacencia[2][0] = aresta_CA # C está conectado a A
matriz_adjacencia[3][1] = aresta_DB # D está conectado a B

# Converter para NumPy
matriz_numpy = np.array(matriz_adjacencia)

# Criar grafo a partir da matriz
G = nx.from_numpy_array(matriz_numpy)

# Renomear nós
mapeamento_labels = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}
G = nx.relabel_nodes(G, mapeamento_labels)

# Definir posições fixas dos nós no mesmo estilo do exemplo
posicoes_dos_nos = {
    'A': [1, 2],  # topo
    'B': [2, 1.5],  # direita
    'C': [1, 0.5],  # embaixo
    'D': [0, 1.5]   # esquerda
}

# Desenhar o grafo
nx.draw(G, posicoes_dos_nos,
        with_labels=True,
        node_color='black',
        node_size=1200,
        edge_color='red',
        width=3.0,
        font_size=16,
        font_color='white',
        font_weight='bold')

plt.title("Grafo com posições fixas (A, B, C, D)")
plt.show()


# Imprime a matriz de adjacência
for linha in matriz_adjacencia:
   print(linha)

# Exemplo de como acessar a matriz de adjacência
linha_escolhida = int(input("Digite um valor de linha entre 0 e 3: "))
coluna_escolhida = int(input("Digite um valor de coluna entre 0 e 3: "))


if matriz_adjacencia[linha_escolhida][coluna_escolhida] == 1:
   print(f"Sim, Existe uma aresta entre {linha_escolhida} e {coluna_escolhida}: ")
else:
   print("Não existe adjacência!")
