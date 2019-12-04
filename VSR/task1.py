from random import *


def main():
    guess = randint()
    x = None
    print('Угадайте число: ')
    while x != guess:
        x = int(input())
        print('Не угадал')


main()
