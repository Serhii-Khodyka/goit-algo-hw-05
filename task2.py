def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        mid = (left + right) // 2
        iterations += 1

        if arr[mid] == target:
            return iterations, arr[mid]
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            upper_bound = arr[mid] if upper_bound is None or arr[mid] < upper_bound else upper_bound

    return iterations, upper_bound

# Приклад використання:
sorted_array = [0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.5, 1.7, 1.9]
target_value = 1.0
iterations, upper_bound = binary_search(sorted_array, target_value)
print(f"Кількість ітерацій: {iterations}")
print(f"Верхня межа: {upper_bound}")
