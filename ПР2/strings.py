def to_uppercase(s):
    result = ""
    for char in s:
        # Если символ является строчной буквой (a-z)
        if 'a' <= char <= 'z':
            # Преобразует его в заглавную, изменив ASCII-код
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

def to_lowercase(s):
    result = ""
    for char in s:
        # Если символ является заглавной буквой (A-Z)
        if 'A' <= char <= 'Z':
            # Преобразует его в строчную, изменив ASCII-код
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

def invert_string(s):
    result = ""
    # Итерирует строку в обратном порядке
    for i in range(len(s) - 1, -1, -1):
        result += s[i]
    return result

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        # Проверяем является ли символ гласной
        if char in vowels:
            count += 1
    return count

def count_consonants(s):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0
    for char in s:
        # Проверяем является ли символ согласной
        if char in consonants:
            count += 1
    return count

def remove_spaces(s):
    result = ""
    for char in s:
        # Добавляем символ только если он не пробел
        if char != ' ':
            result += char
    return result

def capitalize_first_letter(s):
    if len(s) == 0:
        return s
    return s[0].upper() + s[1:]

def main():
    while True:
        print("\nВыберите операцию:")
        print("1. Инвертировать строку")
        print("2. Перевести все буквы в заглавные")
        print("3. Перевести все буквы в строчные")
        print("4. Посчитать количество гласных")
        print("5. Посчитать количество согласных")
        print("6. Удалить пробелы")
        print("7. Сделать первую букву заглавной")
        print("8. Выйти")

        choice = input("Ваш выбор: ")
        if choice == '8':
            break

        string = input("Введите строку: ")
        if choice == '1':
            print("Инвертированная строка:", invert_string(string))
        elif choice == '2':
            print("Заглавные буквы:", to_uppercase(string))
        elif choice == '3':
            print("Строчные буквы:", to_lowercase(string))
        elif choice == '4':
            print("Количество гласных:", count_vowels(string))
        elif choice == '5':
            print("Количество согласных:", count_consonants(string))
        elif choice == '6':
            print("Строка без пробелов:", remove_spaces(string))
        elif choice == '7':
            print("Первая буква заглавная:", capitalize_first_letter(string))
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == '__main__':
    main()