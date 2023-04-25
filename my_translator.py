from random import choice

d = {}
with open("25-04-23.txt", encoding='utf-8') as f:
    for line in f:
        (key, val) = line.split('/')
        d[key] = val

question = int(input('If en-ru = 1, ru-en = 2: '))
i = len(d)

while i > 0:
    word, translate = choice(list(d.items()))

    if question == 1:
        print(word)
        my_translate = input('Enter a translation: ')
        print(translate)

    elif question == 2:
        print(translate)
        my_word = input('Enter a word: ')
        print(word)

    del d[word]
    i -= 1
    print('')
