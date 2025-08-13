def bubble_sort(lista):
  """
  Ordena uma lista de elementos em ordem crescente utilizando o algoritmo Bubble Sort.

  Args:
    lista: A lista a ser ordenada.
  """
  n = len(lista)
  # Percorre todos os elementos da lista
  for i in range(n):
    # O último i elementos já estão no lugar
    for j in range(0, n-i-1):
      # Percorre a lista de 0 a n-i-1
      # Troca se o elemento encontrado for maior que o próximo
      if lista[j] > lista[j+1]:
        lista[j], lista[j+1] = lista[j+1], lista[j]

# Exemplo de uso:
minha_lista = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(minha_lista)
print("Lista ordenada:")
print(minha_lista)