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

    sleep_time = 0.2  # seconds
    generations = 10

    m = get_data()

    # main loop
    for generation in range(generations + 1):
        clear_screen()
        print_matrix(m)
        print("--- generation %s" % generation)
        m = transform_matrix(m, live_cell, dead_cell)
        time.sleep(sleep_time)

    print("Application terminated successfully.")


main()
