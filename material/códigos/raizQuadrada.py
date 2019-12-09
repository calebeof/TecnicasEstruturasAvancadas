x = 8

esquerda = 0
direita = x
eps = 1e-9
while direita - esquerda > eps:
	meio = (esquerda + direita)/2
	if meio*meio < x:
		esquerda = meio
	else:
		direita = meio

print(f'A raiz de {x} é {esquerda:.7f}.')
