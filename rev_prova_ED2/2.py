def selection_sort_decrescente(v):
    n = len(v)
    # percorre todas as posi ções do vetor
    for i in range (n):
        # assume que o maior est á na posi ção i
        indice_maior = i
        # procura o maior elemento na parte não ordenada
        for j in range (i+1, n) :
            if v[j] > v[indice_maior]:
                indice_maior = j
        # troca o maior encontrado com o elemento da posi ção i
        v[i], v[indice_maior] = v[indice_maior] , v[i]
    return v

lista = [11,4,30,22,7,26]
selection_sort_decrescente(lista)
print(lista)
