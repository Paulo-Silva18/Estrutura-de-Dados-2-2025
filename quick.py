# 1
# def partition(array, left, right):
#     pivo = array[right]
#     i = left - 1
#     for j in range(left, right):
#         if array[j] <= pivo:
#             i = i + 1
#             array[i], array[j] = array[j], array[i]
#     array[i + 1], array[right] = array[right], array[i + 1]
#     return i + 1

# def quick_sort(array, left, right):
#     if left < right:
#         pivo_index = partition(array, left, right)
#         quick_sort(array, left, pivo_index - 1)
#         quick_sort(array, pivo_index + 1, right)

# teste_qs = [40, 10, 80, 70, 30, 50, 20]
# quick_sort(teste_qs, 0, len(teste_qs) - 1)
# print(teste_qs)

# 2
# import random
# def partition_random(arr, left, right):
#     pivo_index = random.randint(left, right)                                                                                                  
#     arr[pivo_index], arr[right] = arr[right], arr[pivo_index]
#     pivo = arr[right]
#     i = left - 1
#     for j in range(left, right):
#         if arr[j] <= pivo:
#             i = i + 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i + 1], arr[right] = arr[right], arr[i + 1]
#     return i + 1

# def quick_sort(array, left, right):
#     if left < right:
#         pivo_index = partition_random(array, left, right)
#         quick_sort(array, left, pivo_index - 1)
#         quick_sort(array, pivo_index + 1, right)

# teste_qs = [40, 10, 80, 70, 30, 50, 20]
# quick_sort(teste_qs, 0, len(teste_qs) - 1)
# print(teste_qs)

# 3 
def partition(arr, left, right):
    pivo = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivo:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1

def quickselect(arr, left, right, k):
    pivo_index = partition(arr, left, right)
    if pivo_index == k:
        return arr[pivo_index]
    elif k < pivo_index:
        return quickselect(arr, left, pivo_index - 1, k)
    elif k > pivo_index:
        return quickselect(arr, pivo_index + 1, right, k)

def find_kth_smallest(arr, k):
    if k < 0 or k >= len(arr):
        return "Erro: 'k' está fora dos limites do array."
        
    arr_copy = list(arr)
    
    return quickselect(arr_copy, 0, len(arr_copy) - 1, k)

print(find_kth_smallest([38, 27, 43, 10, 9, 82, 3], 2))