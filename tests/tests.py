import unittest

from cglife.engine import get_neighbours


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
