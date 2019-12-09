A = [2, 3, 5, 6, 7, 8, 9, 10]
valor = 7

esquerda = 0
direita = len(A) - 1
posicao = -1
while esquerda <= direita:
	meio = (esquerda + direita)//2
	if A[meio] == valor:
		posicao = meio
		break
	elif A[meio] < valor:
		esquerda = meio + 1
	else:
		direita = meio - 1

if posicao != -1:
	print(f'{valor} encontrado na posição {posicao}')
else:
	print('Valor não encontrado')
