def insertion_sort_original(lista):
    lista_ordenada = []
    lista_a_ordenar = lista.copy()
    n = len(lista_a_ordenar)

    for i in range(n):
        menor = min(lista_a_ordenar)
        lista_ordenada.insert(i, menor)
        lista_a_ordenar.remove(menor)

    return lista_ordenada

vet_pequeno = [42, 28, 9, 1, 45, 18, 19, 33, 31, 14, 5, 34, 4, 37, 12, 12, 13, 23, 44, 11, 6, 3, 29, 10, 25, 43, 8, 30, 50, 47, 42]

print(insertion_sort_original(vet_pequeno))