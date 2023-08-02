import string
def _get_part_text(text, start, page_size):
    punctuation_marks = {',', '.', '!', ':', ';', '?'}

    end = min(start + page_size, len(text))

    while end > start and text[end - 1] not in punctuation_marks and text[end-2] in string.ascii_letters:
        end -= 1

    return text[start:end], end - start


# Тестовые примеры

text1 = 'Раз. Два. Три. Четыре. Пять. Прием!'
print(*_get_part_text(text1, 5, 9), sep='\n')  # Sample Output 1

text2 = 'Да? Вы точно уверены? Может быть, вам это показалось?.. Ну, хорошо, приходите завтра, тогда и посмотрим, что можно сделать. И никаких возражений! Завтра, значит, завтра!'
print(*_get_part_text(text2, 22, 145), sep='\n')  # Sample Output 2

text3 = '— Я всё очень тщательно проверил, — сказал компьютер, — и со всей определённостью заявляю, что это и есть ответ. Мне кажется, если уж быть с вами абсолютно честным, то всё дело в том, что вы сами не знали, в чём вопрос.'
print(*_get_part_text(text3, 54, 70), sep='\n')  # Sample Output 3

text = 'Да? Вы точно уверены? Может быть, вам это показалось?.. Ну, хорошо, приходите завтра, тогда и посмотрим, что можно сделать. И никаких возражений! Завтра, значит, завтра!'

print(*_get_part_text(text, 0, 54), sep='\n')