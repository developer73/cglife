from engine import get_neighbours


def test_get_neighbours_empty():
    assert get_neighbours([], 1, 1, '0') == 0


def test_get_neighbours():
    data = [
        {
            'm': [
                ['', '0', '', ''],
                ['', '', '', ''],
            ],
            'result': 1
        },
        {
            'm': [
                ['', '0', '', ''],
                ['0', '', '', '0'],
            ],
            'result': 2
        },
    ]

    for data_item in data:
        yield check_neighbours, data_item['m'], 1, 1, '0', data_item['result']


def check_neighbours(m, i, j, live_cell, result):
    assert get_neighbours(m, i, j, live_cell) == result
