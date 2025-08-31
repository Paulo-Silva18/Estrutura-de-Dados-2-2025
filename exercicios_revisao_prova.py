def esta_em_ordem_crescente(v):
  n = len(v)
  if n <= 1:
    return True
  for i in range(n - 1):
    if v[i] > v[i + 1]:
      return False
  return True

def insere_em_ordem(x, v):
  i = 0
  while i < len(v) and v[i] < x:
    i += 1
  v.insert(i, x)

def insertion_sort_recursivo(v, n):
  if n <= 1:
    return

  insertion_sort_recursivo(v, n - 1)

  ultimo = v[n - 1]
  j = n - 2
  while j >= 0 and v[j] > ultimo:
    v[j + 1] = v[j]
    j -= 1
  v[j + 1] = ultimo

def selection_sort_recursivo(v, inicio=0):
  n = len(v)
  if inicio >= n - 1:
    return

  indice_minimo = inicio
  for i in range(inicio + 1, n):
    if v[i] < v[indice_minimo]:
      indice_minimo = i

  v[inicio], v[indice_minimo] = v[indice_minimo], v[inicio]

  selection_sort_recursivo(v, inicio + 1)


def ordena_por_selecao_decrescente(v):
  n = len(v)
  for i in range(n):
    indice_maximo = i
    for j in range(i + 1, n):
      if v[j] > v[indice_maximo]:
        indice_maximo = j
    v[i], v[indice_maximo] = v[indice_maximo], v[i]


def merge_sort(v):
  if len(v) > 1:
    meio = len(v) // 2
    metade_esquerda = v[:meio]
    metade_direita = v[meio:]

    merge_sort(metade_esquerda)
    merge_sort(metade_direita)

    i = j = k = 0

    while i < len(metade_esquerda) and j < len(metade_direita):
      if metade_esquerda[i] < metade_direita[j]:
        v[k] = metade_esquerda[i]
        i += 1
      else:
        v[k] = metade_direita[j]
        j += 1
      k += 1

    while i < len(metade_esquerda):
      v[k] = metade_esquerda[i]
      i += 1
      k += 1

    while j < len(metade_direita):
      v[k] = metade_direita[j]
      j += 1
      k += 1
        