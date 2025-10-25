# 1
# def partition(array, left, right):
#     pivot = array[right]
#     i = left - 1
#     for j in range(left, right):
#         if array[j] >= pivot:
#             i += 1
#             array[i], array[j] = array[j], array[i]
#     array[i + 1], array[right] = array[right], array[i + 1]
#     return i + 1

# def quicksort(array, left, right):
#     if left < right:
#         pivot_index = partition(array, left, right)
#         quicksort(array, left, pivot_index - 1)
#         quicksort(array, pivot_index + 1, right)

# array = [10, 7, 8, 9, 1, 5]
# print("Array original:", array)

# quicksort(array, 0, len(array) - 1)
# print("Array ordenado:", array)



#2
# import time
# import random
# import copy

# def partition_2(arr, low, high):
#     """
#     Função para particionar o array e encontrar a posição do pivô.
#     """
#     pivot = arr[high]
#     i = low - 1
#     for j in range(low, high):
#         if arr[j] <= pivot:
#             i = i + 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return i + 1

# def iterative_quicksort(arr, low, high):
#     """
#     Implementação iterativa do algoritmo Quicksort.
#     """
#     # Cria uma pilha para armazenar os índices.
#     # A pilha de execução simula o que a recursão faria.
#     stack = []
    
#     # Adiciona o intervalo inicial à pilha.
#     stack.append((low, high))

#     # Loop enquanto a pilha não estiver vazia.
#     while stack:
#         # Remove o primeiro elemento da pilha.
#         low, high = stack.pop()

#         # Encontra a posição do pivô.
#         pivot_index = partition_2(arr, low, high)

#         # Se houver elementos à esquerda do pivô, adiciona o intervalo à pilha.
#         if pivot_index - 1 > low:
#             stack.append((low, pivot_index - 1))

#         # Se houver elementos à direita do pivô, adiciona o intervalo à pilha.
#         if pivot_index + 1 < high:
#             stack.append((pivot_index + 1, high))

# def partition(array, left, right):
#     pivot = array[right]
#     i = left - 1
#     for j in range(left, right):
#         if array[j] >= pivot:
#             i += 1
#             array[i], array[j] = array[j], array[i]
#     array[i + 1], array[right] = array[right], array[i + 1]
#     return i + 1

# def quicksort(array, left, right):
#     if left < right:
#         pivot_index = partition(array, left, right)
#         quicksort(array, left, pivot_index - 1)
#         quicksort(array, pivot_index + 1, right)

# def run_tests():
#     # Tamanhos dos vetores de teste
#     sizes = [1000, 10000 ] 
#     results = []

#     for size in sizes:
#         # Geração do vetor aleatório
#         original_array = [random.randint(1, size * 2) for _ in range(size)]
        
#         # Cria cópias para garantir que ambas as funções trabalhem no mesmo dado não ordenado
#         array_rec = copy.copy(original_array)
#         array_iter = copy.copy(original_array)

#         # Medir tempo - Versão Recursiva
#         start_time_rec = time.perf_counter()
#         quicksort(array_rec, 0, len(array_rec) - 1)
#         end_time_rec = time.perf_counter()
#         time_rec = end_time_rec - start_time_rec

#         # Medir tempo - Versão Iterativa
#         start_time_iter = time.perf_counter()
#         iterative_quicksort(array_iter, 0, len(array_iter) - 1)
#         end_time_iter = time.perf_counter()
#         time_iter = end_time_iter - start_time_iter
        
#         # Verifica se a ordenação foi correta (opcional, mas bom para validação)
#         # assert array_rec == sorted(original_array)
#         # assert array_iter == sorted(original_array)

#         results.append({
#             "Tamanho": size,
#             "Tempo Recursivo (s)": f"{time_rec:.6f}",
#             "Tempo Iterativo (s)": f"{time_iter:.6f}"
#         })

#     return results

# # Executa os testes
# test_results = run_tests()
# print(test_results)

# Tamanho do Vetor	Tempo Quicksort Recursivo (s)	Tempo Quicksort Iterativo (s)
#   1.000	                        0.000982	            0.001094
#   10.000	                        0.012917	            0.013319

# Quicksort Recursivo: Vantagens: A versão recursiva é geralmente mais fácil de escrever, entender e manter, pois reflete diretamente a natureza "dividir e conquistar" do algoritmo. O código é mais curto e direto. Desvantagens: Cada chamada recursiva exige que o sistema operacional (ou o interpretador da linguagem) aloque um novo frame na pilha de chamadas para armazenar variáveis locais e o endereço de retorno. Isso representa uma sobrecarga de memória implícita. 

# Quicksort Iterativo: Vantagens: O programador tem controle total sobre a pilha (tamanho, alocação), e a sobrecarga de memória é mais previsível (embora o consumo total possa ser similar). Desvantagens: A versão iterativa é significativamente mais complexa de implementar, pois requer o gerenciamento manual da pilha. A lógica de empilhamento e desempilhamento dos índices (o que a recursão faria automaticamente) precisa ser codificada.

#3
# def qsrt(array, left, right):
#     """
#     Função principal do QuickSort (Ordem Decrescente)
#     """
#     print(f"QSRT(L={left}, R={right})")

#     # A ÚNICA CORREÇÃO NECESSÁRIA: O CASO BASE
#     if left < right:
#         size = right - left + 1
#         if size == 2:
#             print(f"  -> Subvetor de 2 elementos {array[left:right+1]}. Particionando...")
        
#         j = partition(array, left, right) 

#         print(f"  -> Chamando recursão Esquerda: QSRT(L={left}, R={j-1})")
#         qsrt(array, left, j - 1)
        
#         print(f"  -> Chamando recursão Direita: QSRT(L={j+1}, R={right})")
#         qsrt(array, j + 1, right)
    
#     elif left == right:
#         print(f"  -> Caso Base (1 elemento): L={left}, R={right}. (Subvetor: [{array[left]}]). Nada a fazer.")
#     else: 
#         print(f"  -> Caso Base (0 elementos): L={left}, R={right}. (Subvetor vazio). Nada a fazer.")

# def partition(array, left, right):
#     """
#     Sua função de partição original (Lomuto para ordem DECRESCENTE)
#     """
#     pivot = array[right] 
#     i = left - 1
    
#     print(f"    PARTITION(L={left}, R={right}, PIVOT={pivot}) Array: {array[left:right+1]}")

#     for j in range(left, right):
#         # LÓGICA ORIGINAL (Correta para decrescente):
#         if array[j] >= pivot: 
#             i += 1
#             array[i], array[j] = array[j], array[i]
    
#     # Coloca o pivô no lugar
#     array[i + 1], array[right] = array[right], array[i + 1]
    
#     pivot_index = i + 1
#     print(f"    -> PIVÔ NO ÍNDICE: {pivot_index}. Array após part.: {array[left:right+1]}")
#     return pivot_index

# # --- Função auxiliar para rodar os testes ---
# def run_test(test_name, arr, expected):
#     print(f"\n--- INICIANDO TESTE: {test_name} ---")
#     print(f"Original: {arr}")
    
#     arr_copy = list(arr) 
    
#     qsrt(arr_copy, 0, len(arr_copy) - 1)
    
#     print(f"Resultado:  {arr_copy}")
#     print(f"Esperado:   {expected}")
#     # Usamos assert para garantir que o teste passou
#     assert arr_copy == expected
#     print("Status: OK")
#     print("--------------------------------------")

# # --- Casos de Teste (Ordem Decrescente) ---
# if __name__ == "__main__":
    
#     # Teste 1: Vetor pequeno (2 elementos, já ordenado)
#     run_test("Vetor pequeno (Já ordenado Decr.)", [5, 2], [5, 2])
    
#     # Teste 1b: Vetor pequeno (2 elementos, invertido)
#     run_test("Vetor pequeno (Invertido)", [2, 5], [5, 2])

#     # Teste 2: Vetor padrão
#     run_test("Vetor padrão", [8, 3, 1, 6, 4, 10, 2], [10, 8, 6, 4, 3, 2, 1])
    
#     # Teste 3: Vetor vazio
#     run_test("Vetor vazio", [], [])

#     # Teste 4: Vetor com 1 elemento
#     run_test("Vetor com 1 elemento", [5], [5])
    
#     # Teste 5: Vetor já ordenado (decrescente)
#     run_test("Vetor já ordenado (desc)", [5, 4, 3, 2, 1], [5, 4, 3, 2, 1])
    
#     # Teste 6: Vetor em ordem inversa (crescente)
#     run_test("Vetor ordenado (asc)", [1, 2, 3, 4, 5], [5, 4, 3, 2, 1])

#     # Teste 7: Vetor com elementos duplicados
#     run_test("Vetor com duplicatas", [4, 2, 5, 2, 4, 5, 1], [5, 5, 4, 4, 2, 2, 1])
# # A função original qsrt não tem um "caso base" para parar a recursão. Ela continuará chamando a si mesma mesmo para subvetores vazios (left > right), o que causará um IndexError na função partition (ao tentar acessar array[right]). A correção é adicionar um if left < right: no início da função qsrt.

# 4
# def sep ( array , left , right ) :
#     print(f"    SEP(L={left}, R={right}) - Array: {array[left:right+1]}")
    
#     # O pivô é o valor em array[right]
#     # Nota: O valor em array[right] PODE MUDAR durante o loop
#     print(f"    -> Pivô inicial (valor): {array[right]}")
    
#     j = right
#     # Loop de 'right-1' descendo até 'left'
#     for i in range ( right - 1 , left - 1 , -1) :
        
#         # Compara o elemento atual com o elemento NA ÚLTIMA POSIÇÃO (que pode ter mudado)
#         print(f"      i={i}. Compara array[{i}] ({array[i]}) > array[{right}] ({array[right]})")
        
#         if array [ i ] > array [ right ]:
#             print(f"        -> TROCA: array[{i}] ({array[i]}) <-> array[{right}] ({array[right]})")
            
#             # Executa a troca
#             array [ i ] , array [ right ] = array [ right ] , array [ i ]
#             j = i # Atualiza o índice 'j'
            
#             print(f"        -> Array agora: {array[left:right+1]}, j={j}")
        
#     print(f"    -> SEP Retornando j={j}")
#     return j

# def quicksort(array, left, right):
#     print(f"QUICKSORT(L={left}, R={right})")
    
#     if left < right:
#         # Chama a sua função de partição
#         pivot_index = sep(array, left, right)
        
#         print(f"  -> Pivô final no índice: {pivot_index}")

#         # Chamadas recursivas
#         print(f"  -> Chamando Esq: QUICKSORT(L={left}, R={pivot_index - 1})")
#         quicksort(array, left, pivot_index - 1)
        
#         print(f"  -> Chamando Dir: QUICKSORT(L={pivot_index + 1}, R={right})")
#         quicksort(array, pivot_index + 1, right)
    
#     # Prints para os casos base (o que acontece com subvetores pequenos)
#     elif left == right:
#         print(f"  -> Caso Base (1 elemento): L={left}, R={right}. (Subvetor: [{array[left]}]).")
#     else: 
#         print(f"  -> Caso Base (0 elementos): L={left}, R={right}. (Subvetor vazio).")

# # --- Função auxiliar para rodar os testes ---
# def run_test(test_name, arr, expected_asc):
#     print(f"\n--- INICIANDO TESTE: {test_name} ---")
#     print(f"Original: {arr}")
    
#     arr_copy = list(arr) 
    
#     quicksort(arr_copy, 0, len(arr_copy) - 1)
    
#     print("\n--- TESTE FINALIZADO ---")
#     print(f"Resultado (Seu código):  {arr_copy}")
#     print(f"Esperado (Crescente):    {expected_asc}")
    
#     # Compara o resultado com as duas ordenações
#     if arr_copy == expected_asc:
#         print("Status: OK (Crescente)")
#     elif arr_copy == sorted(arr, reverse=True):
#          print("Status: OK (Decrescente)")
#     else:
#         print("Status: FALHOU (Não ordenado)")
#     print("--------------------------------------")

# # --- Casos de Teste ---
# if __name__ == "__main__":
    
#     # Teste 1: Vetor pequeno (onde a lógica será mais fácil de ver)
#     run_test("Vetor pequeno", 
#              [3, 1, 2], 
#              [1, 2, 3])

#     # Teste 2: Vetor padrão
#     run_test("Vetor padrão", 
#              [8, 3, 1, 6, 4, 10, 2], 
#              [1, 2, 3, 4, 6, 8, 10])
    
#     # Teste 3: Vetor vazio
#     run_test("Vetor vazio", 
#              [], 
#              [])

#     # Teste 4: Vetor com 1 elemento
#     run_test("Vetor com 1 elemento", 
#              [5], 
#              [5])
    
#     # Teste 5: Vetor já ordenado (ascendente)
#     run_test("Vetor já ordenado (asc)", 
#              [1, 2, 3, 4, 5], 
#              [1, 2, 3, 4, 5])
    
#     # Teste 6: Vetor em ordem inversa (descendente)
#     run_test("Vetor ordenado (desc)", 
#              [5, 4, 3, 2, 1], 
#              [1, 2, 3, 4, 5])

#     # Teste 7: Vetor com elementos duplicados
#     run_test("Vetor com duplicatas", 
#              [4, 2, 5, 2, 4, 5, 1], 
#              [1, 2, 2, 4, 4, 5, 5])

# O problema central da função sep é que ela não implementa corretamente um algoritmo de particionamento. Uma partição de Quicksort deve garantir uma de duas coisas:
# Que o pivô esteja em sua posição final, com todos os menores à esquerda e maiores à direita e Que o array seja dividido em dois sub-vetores (um de menores, um de maiores), sem garantir a posição final do pivô

# 5
# invocation_trace = []

# def quicksort(array_name_str, left, right):
#     """
#     Simula as invocações recursivas do Quicksort com base 
#     na lógica deduzida (pivot_index = right - 1).
#     """
    
#     # Adiciona a invocação atual à lista de rastreamento
#     invocation_str = f"quicksort({array_name_str}, {left}, {right})"
#     invocation_trace.append(invocation_str)
    
#     # Caso base (igual ao do exemplo)
#     if left < right:
        
#         # Lógica de particionamento DEDUZIDA do Exemplo 1:
#         # O pivô é sempre o penúltimo índice.
#         pivot_index = right - 1
        
#         # Chamada recursiva para a "esquerda" do pivô
#         quicksort(array_name_str, left, pivot_index - 1)
        
#         # Chamada recursiva para a "direita" do pivô
#         quicksort(array_name_str, pivot_index + 1, right)

# # --- Execução do Exemplo 1 (para verificação) ---
# # Reinicia o rastreador
# invocation_trace = [] 
# # O primeiro argumento é apenas uma string para corresponder à saída
# quicksort("array", 1, 4)

# print("--- Sequência do Exemplo 1 (array[1..4] = 77 55 33 99) ---")
# for line in invocation_trace:
#     print(line)


# # --- Execução do Exemplo 2 (O exercício) ---
# # Reinicia o rastreador
# invocation_trace = []
# quicksort("array", 1, 6)

# print("\n--- Sequência do Exemplo 2 (array[1..6] = 55 44 22 11 66 33) ---")
# for line in invocation_trace:
#     print(line)