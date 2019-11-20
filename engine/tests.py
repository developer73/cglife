import unittest

from engine import get_neighbours


class TestNeighbours(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(get_neighbours([], 1, 1, "0"), 0)

    def test_get_neighbours(self):
        data = (
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
        )

        for data_item in data:
            self.assertEqual(
                get_neighbours(data_item["m"], 1, 1, "0"), data_item["result"])
