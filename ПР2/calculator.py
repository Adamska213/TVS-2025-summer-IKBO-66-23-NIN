import operator

# Функция для вычисления выражений, введенных в одну строку
def calculate_expression(expr):
    try:
        result = eval(expr)
        return result
    except Exception as e:
        return f"Error in expression: {str(e)}"

# Словарь операторов для пошаговых операций
operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

def step_by_step_calculator():
    current_result = None
    current_operator = None

    while True:
        if current_result is None:
            try:
                current_result = float(input("Введите число: "))
            except ValueError:
                print("Ошибка: Введите корректное число.")
                continue
        else:
            input_value = input("Введите знак операции (+, -, *, /) или число: ").strip()

            # Если это оператор
            if input_value in operations:
                current_operator = input_value
            else:
                try:
                    num = float(input_value)
                    if current_operator is None:
                        print("Ошибка: Введите сначала операцию.")
                    else:
                        # Применяем последнюю операцию
                        try:
                            current_result = operations[current_operator](current_result, num)
                            print(f"Текущий результат: {current_result}")
                        except ZeroDivisionError:
                            print("Ошибка: Деление на ноль!")
                            current_result = None
                except ValueError:
                    print("Ошибка: Введите корректное число или оператор.")

if __name__ == "__main__":
    print("Добро пожаловать в калькулятор!")
    mode = input("Выберите режим работы (1 - строковый ввод, 2 - пошаговый ввод): ").strip()

    if mode == "1":
        expression = input("Введите выражение (например, '10 + 10 / 2'): ")
        result = calculate_expression(expression)
        print(f"Результат: {result}")
    elif mode == "2":
        step_by_step_calculator()
    else:
        print("Неверный выбор режима.")