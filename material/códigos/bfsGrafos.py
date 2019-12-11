grafo = [[0, 0, 1, 0, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 1, 0, 1],
         [0, 1, 0, 0, 1, 0, 0, 1],
         [1, 0, 1, 0, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 1, 0, 0]]
vertices = 8
origem = 5
destino = 6

marc = [0] * vertices
fila = [origem]
marc[origem] = 1
while len(fila) > 0:
	v = fila[0]
	fila.pop(0)
	for i in range(0, vertices):
		if grafo[v][i] == 1 and marc[i] == 0:
			fila.append(i)
			marc[i] = 1

if marc[destino] == 1:
	print(f'Existe um caminho de {origem} até {destino}.')
else:
	print(f'Não existe caminho de {origem} até {destino}.')
