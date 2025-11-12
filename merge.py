# 1
# Função base (ordem crescente)
# def merge(left, right):
#     result = []
#     i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result

# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left_half = arr[:mid]
#     right_half = arr[mid:]
#     sorted_left = merge_sort(left_half)
#     sorted_right = merge_sort(right_half)
#     return merge(sorted_left, sorted_right)

# print(merge_sort([38, 27, 43, 10, 9, 82, 3]))

# 2
# Função base (ordem decrescente)
# def merge(left, right):
#     result = []
#     i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i] > right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result

# def merge_sort_decrescente(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left_half = arr[:mid]
#     right_half = arr[mid:]
#     sorted_left = merge_sort_decrescente(left_half)
#     sorted_right = merge_sort_decrescente(right_half)
#     return merge(sorted_left, sorted_right)

# print(merge_sort_decrescente([38, 27, 43, 10, 9, 82, 3]))

# 3
# Função base (ordem crescente)
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
    result.extend(left[i:])
    result.extend(right[j:])
    return result
def merge_sort_iterativo(arr):
    step = 1
    n = len(arr)
    while step < n:
        for i in range(0, n, 2 * step):
            left = arr[i:i + step]
            right = arr[i + step: i + 2 * step]
            merged = merge(left, right)
            for j, val in enumerate(merged):
                arr[i + j] = val
        step = step * 2
    return arr

print(merge_sort_iterativo([38, 27, 43, 10, 9, 82, 3]))

