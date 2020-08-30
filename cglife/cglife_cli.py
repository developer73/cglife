import argparse
import time

from .input import get_data
from .engine import transform_matrix


def clear_screen():
    print('\n'*40)


def print_matrix(m):
    for line in m:
        print(line)


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--input",
                        help="Path to input file",
                        default="data/rectangle.txt")

    parser.add_argument("-g", "--generations",
                        help="Number of generations to run",
                        default=10,
                        type=int)

    return parser.parse_args()


def main():
    live_cell = '0'
    dead_cell = '.'
    sleep_time = 0.2  # seconds

    args = get_args()
    generations_total = args.generations
    m = get_data(args.input)

    for generation in range(generations_total + 1):
        if generation < generations_total:
            status = "Running."
        else:
            status = "Stopped."

        clear_screen()
        print_matrix(m)
        print(f"{status} Generation {generation}.")
        m = transform_matrix(m, live_cell, dead_cell)
        time.sleep(sleep_time)


main()
