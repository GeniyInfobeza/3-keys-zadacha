"""
Программа для нахождения суммы отрицательных элементов,
расположенных между максимальным и минимальным элементами одномерного массива.
"""

def find_sum_between_extremes(arr):
    """
    Находит сумму отрицательных элементов между первыми вхождениями min и max.
    
    Аргументы:
        arr: список чисел
        
    Возвращает:
        float: сумма отрицательных элементов между min и max
    """
    if len(arr) < 2:
        return 0
    
    # Поиск индексов первого вхождения min и max
    min_val = arr[0]
    max_val = arr[0]
    min_idx = 0
    max_idx = 0
    
    for i in range(1, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
            min_idx = i
        if arr[i] > max_val:
            max_val = arr[i]
            max_idx = i
    
    # Определение границ интервала (от меньшего индекса к большему)
    left = min(min_idx, max_idx) + 1
    right = max(min_idx, max_idx)
    
    # Суммирование отрицательных элементов
    total = 0
    for i in range(left, right):
        if arr[i] < 0:
            total += arr[i]
    
    return total


def main():
    """Основная функция для ввода данных и вывода результата."""
    try:
        n = int(input("Введите размер массива N: "))
        if n <= 0:
            print("Размер массива должен быть положительным числом")
            return
        
        arr = []
        print(f"Введите {n} элементов массива:")
        for i in range(n):
            val = float(input(f"arr[{i}] = "))
            arr.append(val)
        
        result = find_sum_between_extremes(arr)
        
        print(f"\nМассив: {arr}")
        print(f"Сумма отрицательных элементов между min и max: {result}")
        
    except ValueError:
        print("Ошибка: введите корректные числа")


if __name__ == "__main__":
    main()