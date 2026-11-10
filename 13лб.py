import math

total_spam_words = 101
total_ham_words = 44
total_spam_emails = 16
total_ham_emails = 13

words_data = {
    'Remove': [9, 2],
    'Refund': [4, 7],
    'Million': [4, 2],
    'Investment': [29, 5],
    'Bonus': [11, 5]
}

V = 10

p_spam = total_spam_emails / (total_spam_emails + total_ham_emails)
p_ham = total_ham_emails / (total_spam_emails + total_ham_emails)

def calc_F(word_list, word_counts, total_words, V):
    F = 1.0
    for word in word_list:
        count = word_counts[word]
        # Формула Лапласа
        prob = (count + 1) / (total_words + V)
        F *= prob
    return F

email_words = ['Remove', 'Refund', 'Million', 'Investment', 'Bonus']

F_spam = calc_F(email_words, {w: words_data[w][0] for w in words_data}, total_spam_words, V)
F_ham = calc_F(email_words, {w: words_data[w][1] for w in words_data}, total_ham_words, V)

# Формула Байеса
numerator = p_spam * F_spam
denominator = numerator + (p_ham * F_ham)
p_spam_given_email = numerator / denominator

print(f"Вероятность того, что письмо является спамом: {p_spam:.3f}")
print(f"F('спам'): {F_spam:.3f}")
print(f"F('не спам'): {F_ham:.3f}")
print(f"Вероятность P(Класс='спам'|Письмо): {p_spam_given_email:.3f}")