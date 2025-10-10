def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        chave = array[i]
        j = i - 1
        while j >= 0 and array[j] > chave:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = chave  
    return array 


def lista_numerica(array):
    l = []
    ls = []
    for i in array:
        n = len(i)
        l.append(n)
    lista_ordenada = insertion_sort(l)
    for j in array:
        n = len(j)
        print(n)
        
    return array
    
    

lista = ['Ana', 'Lu', 'Roberto']
lista_numerica(lista)
