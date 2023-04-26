from pathlib import Path

words = [w for w in Path('Python_strings.txt').read_text(encoding="utf-8").replace("\n", " ").split()]
known_words = [w for w in Path('know.txt').read_text(encoding="utf-8").replace("\n", " ").split()]
dont_known_words = [w for w in Path('dont_know.txt').read_text(encoding="utf-8").replace("\n", " ").split()]

f1 = open('dont_know.txt', 'a')
f2 = open('know.txt', 'a')
words_lower = []

for i in words:
    if i.isalpha():
        words_lower.append(i.lower())

sorted_list = sorted(words_lower)

one_word_list = []

for k in sorted_list:
    if k not in one_word_list:
        one_word_list.append(k)

for n in one_word_list:
    if n not in known_words:
        if n not in dont_known_words:
            print(n)
            know = input('Know? no=1: ')
            if know == '1':
                f1.write(f'{n}\n')
            else:
                f2.write(f'{n}\n')
