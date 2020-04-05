import numpy as np

def game_core_v2(number):
    '''—начала устанавливаем любое random число, а потом 
       уменьшаем или увеличиваем его в зависимости от того, 
       больше оно или меньше нужного. ‘ункци€ принимает 
       загаданное число и возвращает число попыток'''
    count = 1
    a=1
    b=101
    predict = np.random.randint(a,b)
    while number != predict:
        count+=1
        if number > predict: 
            a = predict + 1
            predict = np.random.randint(a,b)
        elif number < predict: 
            b = predict
            predict = np.random.randint(a,b)
    return(count) # выход из цикла, если угадали

def score_game(game_core_v1):
    '''«апускаем игру 1000 раз, чтобы узнать, 
       как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v1(number))
    score = int(np.mean(count_ls))
    print(f"јлгоритм угадывает число в среднем за {score} попыток")
#     return(score)

# ѕровер€ем
score_game(game_core_v2)