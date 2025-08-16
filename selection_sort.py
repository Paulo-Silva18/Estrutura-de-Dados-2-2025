import time
import random

def selection_sort_original(lista):
    print("--- Iniciando Teste: Versão Original ---")
    lista_ordenada = []
    lista_a_ordenar = lista.copy()
    n = len(lista_a_ordenar)
    iteracoes = 0

    for i in range(n):
        iteracoes += 1
        menor = min(lista_a_ordenar)
        lista_ordenada.append(menor)
        lista_a_ordenar.remove(menor)
        
        print(f"Iteração {i+1}: Menor encontrado = {menor}")
        print(f"  -> Lista Ordenada: {lista_ordenada}")
        print(f"  -> Lista Restante: {lista_a_ordenar}\n")

    print(f"Total de iterações do laço principal: {iteracoes}")
    return lista_ordenada

def selection_sort_otimizada(lista):
    print("--- Iniciando Teste: Versão Otimizada ---")
    lista_a_ordenar = lista.copy() # Copia para não modificar a original e permitir comparação justa
    n = len(lista_a_ordenar)
    comparacoes = 0
    trocas = 0

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparacoes += 1
            if lista_a_ordenar[j] < lista_a_ordenar[min_idx]:
                min_idx = j
        
        if min_idx != i:
            lista_a_ordenar[i], lista_a_ordenar[min_idx] = lista_a_ordenar[min_idx], lista_a_ordenar[i]
            trocas += 1
        
        print(f"Iteração {i+1}: Vetor atual: {lista_a_ordenar}")

    print(f"Total de comparações: {comparacoes}")
    print(f"Total de trocas: {trocas}")
    return lista_a_ordenar


vet_pequeno = [11, 4, 30, 22, 7, 26]

# --- Teste com a Versão Original ---
start_time = time.perf_counter()
selection_sort_original(vet_pequeno)
end_time = time.perf_counter()
tempo_original = end_time - start_time

print(f"\nTempo de execução (Original): {tempo_original:.6f} segundos\n")

# --- Teste com a Versão Otimizada ---
start_time = time.perf_counter()
selection_sort_otimizada(vet_pequeno)
end_time = time.perf_counter()
tempo_otimizado = end_time - start_time

print(f"\nTempo de execução (Otimizado): {tempo_otimizado:.6f} segundos\n")