# Тема 6. Строки. Байты. Файлы

### Инвариантная самостоятельная работа
Задание 1:
[Аннотированный список](https://github.com/python-basic/sem3-t3-DenisNyux/blob/master/ISR/task1.docx)

Задание 2:
```python
def main():
    input_str = input("Введите строку для поиска: ")

    searchable_str = input("Введите строку, по которой мы ищем: ")

    choice = None
    while choice != '4':
        print('1 - поиск первого вхождения подстроки')
        print('2 - замена первой подстроки')
        print('3 - найти все вхождения подстроки' )
        print('4 - для выхода')
        choice = input("Сделайте  выбор (1..4) ")
        if choice == '1':
            print('\n', search_str_first(input_str, searchable_str), '\n', sep='')
        if choice == '2':
            replacer = input('Введите то, на что стоит заменить: ')
            print('\n', search_n_replace_str(input_str, replacer, searchable_str), '\n', sep='')
        if choice == '3':
            print('\n', search_str_all(input_str, searchable_str), '\n', sep='')


def search_str_first(what, where):
    i = 0
    k = len(where)
    res = list()
    while k != 0:
        j = i + len(what)
        if what in where[i:j]:
            res.append(i)
        i += 1
        k -= 1
    if len(res) == 0:
        return 'Ничего не найдено'
    else:
        return res[0]


def search_n_replace_str(what, to_what, where):
    index = search_str_first(what, where)
    changed = where[0:index] + to_what + where[index + len(what):len(where)]
    return changed


def search_str_all(what, where):
    i = 0
    k = len(where)
    res = list()
    while k != 0:
        j = i + len(what)
        if what in where[i:j]:
            res.append(i)
        i += 1
        k -= 1
    if len(res) == 0:
        return 'Ничего не найдено'
    else:
        return res


main()
```
Задание 3: https://github.com/python-basic/sem3-t3-DenisNyux/tree/master/ISR/task3

Задание 4:
```python
def changer(letter):
    if ord('a') + 13 > ord(letter) >= ord('a'):
        return chr(ord(letter) + 13)
    elif ord('z') >= ord(letter) >= ord('a') + 13:
        return chr(ord(letter) - 13)
    else:
        return letter


def main():
    string_to_encrypt = input('Введите строчку которую нужно зашифровать: ')
    encrypted_res = ''.join(list((map(changer, string_to_encrypt))))
    print('Результат шифрования:', encrypted_res)


main()
```

### Вариативная самостоятельная работа
Задание 1:
```python
from random import *


def main():
    guess = randint(0, 100)
    x = None
    more = 'число больше загаданного'
    less = 'число меньше загаданного'
    print('Угадайте число: ')
    while x != guess:
        x = int(input())
        if x < guess:
            print('Не угадал, {}'.format(more))
        elif x > guess:
            print('Не угадал, {}'.format(less))
        else:
            print('Угадали!')



main()
from random import *


def main():
    guess = randint(0, 100)
    x = None
    more = 'число больше загаданного'
    less = 'число меньше загаданного'
    print('Угадайте число: ')
    while x != guess:
        x = int(input())
        if x < guess:
            print('Не угадал, {}'.format(more))
        elif x > guess:
            print('Не угадал, {}'.format(less))
        else:
            print('Угадали!')



main()
```
Задание 2:
```python
engl_alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
russ_alphabet = [chr(i) for i in range(ord('а'), ord('я') + 1)]
print(engl_alphabet, russ_alphabet, sep='\n')
```

###Лабораторные работы 10 и 11:
[Лр10](https://github.com/python-basic/sem3-t3-DenisNyux/tree/master/lab10)

[Лр11](https://github.com/python-basic/sem3-t3-DenisNyux/tree/master/lab11)
