"""
File: DoubleBeepers.py
Name:
-------------------------------
TODO:
"""


from karel.stanfordkarel import *


def main():
    """
    Karel will double the beepers
    """
    move()
    double_beepers()
    turn_back()
    move()
    turn_back()


def turn_back():
    turn_left()
    turn_left()


def double_beepers():
    k = 0
    while on_beeper():
        pick_beeper()
        k = k+1
    else:
        for i in range(k):
            put_beeper()
            put_beeper()


####### DO NOT EDIT CODE BELOW THIS LINE ########


if __name__ == '__main__':
    execute_karel_task(main)