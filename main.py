def is_prime(n):
    """Проверяет, является ли число простым."""
    if n <= 1:
        return False  # Числа меньше или равные 1 не являются простыми
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # Если число делится на любое число от 2 до его квадратного корня, оно не простое
    return True  # Если делителей не найдено, число простое
def find_primes(numbers):
    """Возвращает список простых чисел из исходного списка."""
    primes = [num for num in numbers if is_prime(num)]  # Используем генератор списка для фильтрации простых чисел
    return primes  # Возвращаем список простых чисел
user_input = input("Введите числа через пробел: ")# Запрашиваем ввод чисел
numbers = list(map(int, user_input.split()))  # Преобразуем ввод в список чисел
prime_numbers = find_primes(numbers)  # Находим все простые числа в списке
print("Простые числа:", prime_numbers)  # Выводим список простых чисел 