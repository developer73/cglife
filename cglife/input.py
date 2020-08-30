def read_from_file(filename):
    """
    Reads text file <filename> and returns it's content.

    content of the file:
        test 123
        abc 456
        end
    output:
        ['test 123\n', 'abc 456\n', 'end\n']
    """
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    return lines


def get_data(path="data/rectangle.txt"):
    m = read_from_file(path)
    # remove new line characters
    m = [item.rstrip('\n') for item in m]
    return m
