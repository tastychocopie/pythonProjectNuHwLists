import random

months = {
    '01': 'января',
    '02': 'февраля',
    '03': 'марта',
    '04': 'апреля',
    '05': 'мая',
    '06': 'июня',
    '07': 'июля',
    '08': 'августа',
    '09': 'сентября',
    '10': 'октября',
    '11': 'ноября',
    '12': 'декабря'
}
days = {
    '01': 'первое',
    '02': 'второе',
    '03': 'третье',
    '04': 'четвертое',
    '05': 'пятое',
    '06': 'шестое',
    '07': 'седьмое',
    '08': 'восьмое',
    '09': 'девятое',
    '10': 'десятое',
    '11': 'одиннадцатое',
    '12': 'двенадцатое',
    '13': 'тринадцатое',
    '14': 'четырнадцатое',
    '15': 'пятьнадцатое',
    '16': 'шестнадцатое',
    '17': 'семнадцатое',
    '18': 'восемнадцатое',
    '19': 'девятнадцатое',
    '20': 'двадцатое',
    '21': 'двадцать первое',
    '22': 'двадцать второе',
    '23': 'двадцать третье',
    '24': 'двадцать четвертое',
    '25': 'двадцать пятое',
    '26': 'двадцать шестое',
    '27': 'двадцать седьмое',
    '28': 'двадцать восьмое',
    '29': 'двадцать девятое',
    '30': 'тридцатое',
    '31': 'тридцать первое',
}

# date = "09.02.2024"
# day, month, year = date.split('.')
# print(days[day], months[month], year, "года")

# Choose 5 people
# 1 Lionel Messi 24.06.1987
# 2 Elon Musk 28.06.1971
# 3 Steve Jobs 24.02.1955
# 4 Christiano Ronaldo 05.02.1985
# 5 Jeon Jungkook 01.09.1997
# 6 Drake 24.10.1986
# 7 Keshi 04.11.1994
# 8 Joji 18.09.1992
# 9 The Weekend 16.02.1990
# 10 Justin Bieber 01.03.1994

# messi_born_year = 1987
# elon_born_year = 1971
# steve_born_year = 1955
# ronaldo_born_year = 1985
# jk_born_year = 1997
people = {
    1: "Lionel Messi",
    2: "Elon Musk",
    3: "Steve Jobs",
    4: "Christiano Ronaldo",
    5: "Jeon Jungkook",
    6: "Drake",
    7: "Keshi",
    8: "Joji",
    9: "The Weekend",
    10: "Justin Bieber"
}
# 1 Lionel Messi 24.06.1987
# 2 Elon Musk 28.06.1971
# 3 Steve Jobs 24.02.1955
# 4 Christiano Ronaldo 05.02.1985
# 5 Jeon Jungkook 01.09.1997
# 6 Drake 24.10.1986
# 7 Keshi 04.11.1994
# 8 Joji 18.09.1992
# 9 The Weekend 16.02.1990
# 10 Justin Bieber 01.03.1994
people_bday = {
    1: "24.06.1987",
    2: "28.06.1971",
    3: "24.02.1955",
    4: "05.02.1985",
    5: "01.09.1997",
    6: "24.10.1986",
    7: "04.11.1994",
    8: "18.09.1992",
    9: "16.02.1990",
    10: "01.03.1994"
}

chosen = random.sample(range(1, 11), 5)
play_again = "да"
while play_again == "да":
    print("Привет! Добропожаловать на викторину! Ответы принимаются ввиде даты(дд.мм.гггг) ")
    correct_counter = 0
    incorrect_counter = 0
    for key in chosen:
        answer = input(f"День рождения {people[key]}: ")
        if answer == people_bday[key]:
            correct_counter += 1
        else:
            incorrect_counter += 1
            day, month, year = people_bday[key].split(".")
            print(f"Ошибка +1! правильный ответ:", days[day], months[month], year, "года." )
    print("РЕЗУЛЬТАТ:")
    print("Количество правильных ответов: ", correct_counter)
    print("Количество ошибок: ", incorrect_counter)
    correct_percent = correct_counter * 100 / 5
    print("Процент правильных ответов: ", correct_percent, "%")
    incorrect_percent = incorrect_counter * 100 / 5
    print("Процент ошибок", incorrect_percent, "%")
    play_again = input("Хочешь заново сыграть?")
    if play_again == "да":
        play_again = "да"
    else:
        play_again = "нет"