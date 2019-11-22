import unittest

from cglife.engine import get_neighbours
from cglife.engine import transform_cell
from cglife.engine import transform_matrix


class TestNeighbours(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(get_neighbours([], 1, 1, "0"), 0)

    def test_get_neighbours(self):
        data = (
            {
                "m": [
                    ["", "", "", ""],
                    ["", "", "", ""],
                ],
                "result": 0
            },
            {
                "m": [
                    ["", "0", "", ""],
                    ["", "", "", ""],
                ],
                "result": 1
            },
            {
                "m": [
                    ["", "0", "", ""],
                    ["0", "", "", "0"],
                ],
                "result": 2
            },
            {
                "m": [
                    ["0", "0"],
                    ["0", "0"],
                ],
                "result": 3
            },
        )

        for index, item in enumerate(data):
            with self.subTest(index):
                self.assertEqual(
                    get_neighbours(item["m"], 1, 1, "0"), item["result"])


class TestTransformCell(unittest.TestCase):

    def test_transform_cell(self):
        data = (
            # dead -> dead
            {
                "m": [
                    [".", ".", ".", "."],
                    [".", ".", ".", "."],
                    [".", ".", ".", "."],
                ],
                "result": "."
            },
            {
                "m": [
                    [".", ".", ".", "0"],
                    [".", ".", ".", "0"],
                    [".", ".", ".", "0"],
                ],
                "result": "."
            },
            # dead -> alive
            {
                "m": [
                    [".", "0", ".", "."],
                    ["0", ".", ".", "."],
                    [".", "0", ".", "."],
                ],
                "result": "0"
            },
            # alive -> dead
            {
                "m": [
                    [".", ".", ".", "."],
                    [".", "0", ".", "."],
                    [".", ".", ".", "."],
                ],
                "result": "."
            },
            {
                "m": [
                    [".", ".", ".", "0"],
                    [".", "0", ".", "0"],
                    [".", ".", ".", "0"],
                ],
                "result": "."
            },
            {
                "m": [
                    [".", ".", ".", "."],
                    [".", "0", "0", "."],
                    [".", ".", ".", "."],
                ],
                "result": "."
            },
            {
                "m": [
                    [".", ".", ".", "."],
                    [".", "0", "0", "."],
                    [".", ".", "0", "."],
                ],
                "result": "0"
            },
            {
                "m": [
                    [".", ".", "0", "."],
                    [".", "0", "0", "."],
                    [".", ".", "0", "."],
                ],
                "result": "0"
            },
            {
                "m": [
                    ["0", ".", "0", "."],
                    [".", "0", "0", "."],
                    [".", ".", "0", "."],
                ],
                "result": "."
            },
        )

        for index, item in enumerate(data):
            cell = transform_cell(item["m"], 1, 1, "0", ".")
            with self.subTest(index):
                self.assertEqual(cell, item["result"])


class TestTransformMatrix(unittest.TestCase):

    def test_transform_matrix(self):
        data = (
            {
                "m": [
                    "....",
                    "....",
                    "....",
                ],
                "result": [
                    "....",
                    "....",
                    "....",
                ],
            },
            {
                "m": [
                    "000.",
                    "0...",
                    "0..0",
                ],
                "result": [
                    "00..",
                    "0.0.",
                    "....",
                ],
            },
        )

        for index, item in enumerate(data):
            new = transform_matrix(item["m"], live_cell="0", dead_cell=".")
            with self.subTest(index):
                self.assertEqual(new, item["result"])
