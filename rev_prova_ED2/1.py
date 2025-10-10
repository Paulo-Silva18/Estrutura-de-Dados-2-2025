def buuble_sort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-1-i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def inserir(v, x):
    v.append(x)
    listaas = buuble_sort(v)
    return listaas

lista = [3, 8, 6, 7, 4]
lista_or = inserir(lista, 9)
print(lista_or)