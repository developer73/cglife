import time

from .input import get_data
from .engine import transform_matrix


def clear_screen():
    """
    Clears the screen.
    """
    print('\n'*40)


def print_matrix(m):
    """
    Prints the matrix.
    """
    for line in m:
        print(line)


def main():
    live_cell = '0'
    dead_cell = '.'

    sleep_time = 1
    generations = 10

    m = get_data()

    # main loop
    for ii in range(generations):
        clear_screen()
        print_matrix(m)
        print("--- generation %s" % (ii + 1))
        m = transform_matrix(m, live_cell, dead_cell)
        time.sleep(sleep_time)

    print("Application terminated successfully.")


main()
