#!/usr/bin/env python3
""" age.py """
def main():
    """ age.py """
    try:
        age = int(input('Please tell me your age: '))
        print(f'You are currently {age} years old')
        for i in range(1, 4):
            before_age = i*10
            print(f'In {before_age} years, you\'ll be {age+i*10} years old.')
    except:
        print('Mai Aow STR')

main()
