import numpy as np

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")


import random


def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Задаем начальный и конечный пределы для поиска
    lower_bound = 1
    upper_bound = 100
    
    # Генерируем случайное число, которое нужно угадать
    target_number = random.randint(lower_bound, upper_bound)
    
    # Инициализируем счетчик попыток
    count = 0

    # Начинаем бесконечный цикл (пока число не угадано)
    while True:
        # Предполагаемое число - среднее значение текущего диапазона
        guess = (lower_bound + upper_bound) // 2
        # Увеличиваем счетчик попыток
        count += 1

        # Проверяем, угадано ли число
        if guess == target_number:
            print(f"Угадано число {target_number} за {count} попыток.")
            break
        # Если предполагаемое число меньше загаданного, сужаем диапазон вниз
        elif guess < target_number:
            print(f"Попытка {count}: Предполагаю, что число больше {guess}.")
            lower_bound = guess + 1
        # Если предполагаемое число больше загаданного, сужаем диапазон вверх
        else:
            print(f"Попытка {count}: Предполагаю, что число меньше {guess}.")
            upper_bound = guess - 1

    return count


print('Run benchmarking for game_core_v3: ', end='')
if __name__ == "__main__":
    # RUN
    score_game(game_core_v3)

