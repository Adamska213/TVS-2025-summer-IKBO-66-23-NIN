def invert_array(arr):
    """Инвертирует массив в обратном порядке"""
    inverted = []
    for i in range(len(arr) - 1, -1, -1):
        inverted.append(arr[i])
    return inverted

def bubble_sort(arr):
    """Сортирует массив методом пузырька"""
    n = len(arr)
    sorted_arr = arr.copy()  # Создаем копию массива
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
    return sorted_arr

def find_min(arr):
    """Находит минимальный элемент массива"""
    if not arr:
        return None
    min_value = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min_value:
            min_value = arr[i]
    return min_value

def find_max(arr):
    """Находит максимальный элемент массива"""
    if not arr:
        return None
    max_value = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
    return max_value

def sum_array(arr):
    """Сумма всех элементов массива"""
    total = 0
    for num in arr:
        total += num
    return total

def average_array(arr):
    """Среднее арифметическое элементов массива"""
    if not arr:
        return 0
    total = sum_array(arr)
    avg = total / len(arr)
    return avg

def count_occurrences(arr, value):
    """Подсчитывает количество вхождений элемента в массиве"""
    count = 0
    for num in arr:
        if num == value:
            count += 1
    return count

def main():
    """Основная функция программы"""
    while True:
        print("\nВыберите операцию:")
        print("1. Инвертировать массив")
        print("2. Сортировка массива (пузырьковая сортировка)")
        print("3. Найти минимальный элемент массива")
        print("4. Найти максимальный элемент массива")
        print("5. Сумма всех элементов массива")
        print("6. Среднее арифметическое элементов массива")
        print("7. Подсчитать количество вхождений элемента в массиве")
        print("8. Выйти")

        choice = input("Ваш выбор: ")
        
        if choice == '8':
            print("Выход из программы...")
            break
        
        if choice not in ['1', '2', '3', '4', '5', '6', '7']:
            print("Неверный выбор. Попробуйте снова.")
            continue

        try:
            arr_input = input("Введите массив чисел через пробел: ")
            arr = list(map(int, arr_input.split()))
            
            if not arr:
                print("Массив не может быть пустым!")
                continue
                
            if choice == '1':
                print("Инвертированный массив:", invert_array(arr))
            elif choice == '2':
                print("Отсортированный массив:", bubble_sort(arr))
            elif choice == '3':
                print("Минимальный элемент массива:", find_min(arr))
            elif choice == '4':
                print("Максимальный элемент массива:", find_max(arr))
            elif choice == '5':
                print("Сумма всех элементов массива:", sum_array(arr))
            elif choice == '6':
                print("Среднее арифметическое элементов массива:", average_array(arr))
            elif choice == '7':
                value = int(input("Введите элемент для подсчета: "))
                print(f"Элемент {value} встречается {count_occurrences(arr, value)} раз(а)")
                
        except ValueError:
            print("Ошибка: введите корректные числа!")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()