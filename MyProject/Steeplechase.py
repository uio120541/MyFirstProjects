"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()


def jump():
    up()
    cross()
    down()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def up():
    turn_left()
    #karel is facing North
    while not right_is_clear():
        move()


def cross():
    turn_right()
    move()
    turn_right()


def down():
    move()
    while front_is_clear():
        move()
    else:
        turn_left()


####### DO NOT EDIT CODE BELOW THIS LINE ########


if __name__ == '__main__':
    execute_karel_task(main)
