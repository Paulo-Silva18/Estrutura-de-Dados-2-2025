-----

# Algoritmos de Ordenação em Python 🐍

Este repositório contém implementações de vários algoritmos de ordenação clássicos em Python. Cada algoritmo é demonstrado com um exemplo prático.

## Pré-requisitos

Para executar estes códigos, você precisa apenas de um interpretador Python (versão 3.x recomendada) instalado em seu sistema.

-----

## Como Executar

1.  Copie o código do algoritmo que você deseja testar.
2.  Salve-o em um arquivo com a extensão `.py` (por exemplo, `meu_algoritmo.py`).
3.  Abra um terminal ou prompt de comando.
4.  Navegue até o diretório onde você salvou o arquivo.
5.  Execute o arquivo com o comando:
    python seu_arquivo.py

-----

## Algoritmos Implementados

### 1\. Bubble Sort (Crescente)

Este código implementa o Bubble Sort, um algoritmo simples que percorre a lista repetidamente, comparando pares de elementos adjacentes e trocando-os se estiverem na ordem errada. A função `inserir` adiciona um novo elemento à lista e a reordena.


#### Código

def buuble_sort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-1-i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def inserir(v, x):
    v.append(x)
    # Chama o bubble sort para ordenar a lista após a inserção
    listaas = buuble_sort(v)
    return listaas

# Exemplo de uso
lista = [3, 8, 6, 7, 4]
lista_or = inserir(lista, 9)
print(lista_or)


#### Saída Esperada

[3, 4, 6, 7, 8, 9]

-----

### 2\. Selection Sort (Decrescente)

A implementação do **Selection Sort** ordena uma lista encontrando repetidamente o maior elemento da parte não ordenada e colocando-o no início da parte ordenada (neste caso, em ordem **decrescente**).

#### Código

def selection_sort_decrescente(v):
    n = len(v)
    # Percorre todas as posições do vetor
    for i in range (n):
        # Assume que o maior está na posição i
        indice_maior = i
        # Procura o maior elemento na parte não ordenada
        for j in range (i+1, n) :
            if v[j] > v[indice_maior]:
                indice_maior = j
        # Troca o maior encontrado com o elemento da posição i
        v[i], v[indice_maior] = v[indice_maior] , v[i]
    return v

# Exemplo de uso
lista = [11, 4, 30, 22, 7, 26]
selection_sort_decrescente(lista)
print(lista)


#### Saída Esperada

[30, 26, 22, 11, 7, 4]

-----

### 3\. Insertion Sort (por Comprimento de String)

Esta é uma variação do **Insertion Sort** que ordena uma lista de strings com base em seu **comprimento**, da menor para a maior.

#### Código

def insertion_sort_por_comprimento(array):
    n = len(array)
    for i in range(1, n):
        chave_string = array[i]
        j = i - 1
        # Compara o comprimento das strings
        while j >= 0 and len(array[j]) > len(chave_string):
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = chave_string
    return array

# Exemplo de uso
lista = ['Ana', 'Lu', 'Roberto']
lista_ordenada = insertion_sort_por_comprimento(lista)
print(lista_ordenada)


#### Saída Esperada

['Lu', 'Ana', 'Roberto']

-----

### 4\. Merge Sort (Crescente)

O **Merge Sort** é um algoritmo eficiente de "dividir para conquistar". Ele divide a lista em metades, ordena cada metade recursivamente e, em seguida, mescla as metades ordenadas para produzir a lista final.

#### Código

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Adiciona os elementos restantes de qualquer uma das metades
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)
    
    return merge(sorted_left, sorted_right)

# Exemplo de uso
lista_para_ordenar = [38, 27, 43, 3, 9, 82, 10]
lista_ordenada = merge_sort(lista_para_ordenar)
print(lista_ordenada)


#### Saída Esperada

[3, 9, 10, 27, 38, 43, 82]
