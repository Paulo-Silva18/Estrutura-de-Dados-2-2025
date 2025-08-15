def selection_sort(lista):
  menor = min(lista)
  lista_ordernada = []
  n = len(lista)
  for i in range(n):
    for j in range(0, n-i-1):
      print(f"Valor do menor {menor}")
      print(f"Valor da lista na posição {j}: {lista[j]}")
      if menor < lista[j]:
        lista_ordernada.insert(j, menor)
        menor = lista[j]
  return lista_ordernada

vet = [11, 4, 30, 22, 7, 26]
print(f"Vetor ordenado {selection_sort(vet)}")