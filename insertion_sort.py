import time

def insertion_sort(lista):
    iteracoes_externas = 0
    comparacoes_e_deslocamentos = 0

    for i in range(1, len(lista)):
        iteracoes_externas += 1
        chave = lista[i]
        j = i - 1

        while j >= 0 and chave < lista[j]:
            comparacoes_e_deslocamentos += 1
            lista[j + 1] = lista[j]
            j -= 1
        
        lista[j + 1] = chave

    return (iteracoes_externas, comparacoes_e_deslocamentos)

import random

tamanho_vetor = 1000

vetor_aleatorio = [random.randint(0, tamanho_vetor * 10) for _ in range(tamanho_vetor)]

vetor_ordenado = sorted(vetor_aleatorio)

copia_aleatorio = vetor_aleatorio.copy()
copia_ordenado = vetor_ordenado.copy()

print("--- Analisando Vetor Aleatório ---")
start_time = time.perf_counter()
stats_aleatorio = insertion_sort(copia_aleatorio)
end_time = time.perf_counter()

print(f"Tempo de execução: {end_time - start_time:.6f} segundos")
print(f"Iterações do laço externo: {stats_aleatorio[0]}")
print(f"Comparações e deslocamentos (laço interno): {stats_aleatorio[1]}")
print("-" * 35)


print("\n--- Analisando Vetor Já Ordenado ---")
start_time = time.perf_counter()
stats_ordenado = insertion_sort(copia_ordenado)
end_time = time.perf_counter()

print(f"Tempo de execução: {end_time - start_time:.6f} segundos")
print(f"Iterações do laço externo: {stats_ordenado[0]}")
print(f"Comparações e deslocamentos (laço interno): {stats_ordenado[1]}")
print("-" * 35)