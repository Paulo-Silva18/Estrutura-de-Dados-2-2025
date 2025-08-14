def bubble_sort(lista):
  n = len(lista)
  for i in range(n):
    for j in range(0, n-i-1):
      if lista[j] > lista[j+1]:
        lista[j], lista[j+1] = lista[j+1], lista[j]
  return lista

minha_lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:")
print(minha_lista)
print("Lista ordenada:")
print(bubble_sort(minha_lista))

def bubble_sort_otimizado(lista):
  n = len(lista)
  for i in range(n):
    trocou = False
    for j in range(0, n-i-1):
      if lista[j] > lista[j+1]:
        lista[j], lista[j+1] = lista[j+1], lista[j]
        trocou = True
    if not trocou:
      break
  return lista

minha_lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:")
print(minha_lista)
print("Lista ordenada:")
print(bubble_sort_otimizado(minha_lista))