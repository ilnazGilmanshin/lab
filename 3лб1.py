def grade(score):
    if 0 <= score < 60:
        return "неудовлетворительно"
    elif 60 <= score <= 74:
        return "удовлетворительно"
    elif 74 < score <= 90:
        return "хорошо"
    elif 90 < score <= 100:
        return "отлично"
    else:
        return "Некорректный балл"

user_score = int(input("Введите количество баллов (от 0 до 100): "))

print("Оценка:", grade(user_score))