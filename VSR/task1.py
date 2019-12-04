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
