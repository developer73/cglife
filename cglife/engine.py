def get_neighbours(m, i, j, live_cell):
    """
    Get number of live cells neighbouring given cell in given matrix.
    """
    n = 0
    for ii in [i-1, i, i+1]:
        for jj in [j-1, j, j+1]:
            if ii > -1 and ii < len(m) and jj > -1 and jj < len(m[1]) and \
                    (i, j) != (ii, jj) and m[ii][jj] == live_cell:
                n += 1
    return n


def transform_cell(m, i, j, live_cell, dead_cell):
    """
    Determines whether cell will be live or dead in the next generation.
    """
    n = get_neighbours(m, i, j, live_cell)
    cell = dead_cell
    if n == 3 or (n == 2 and m[i][j] == live_cell):
        cell = live_cell
    return cell


def transform_matrix(m, live_cell, dead_cell):
    """
    Transforms the matrix to the next generation.
    """
    m_transformed = []
    for row_index, row in enumerate(m):
        row_transformed = ''
        for cell_index, cell in enumerate(row):
            row_transformed = '%s%s' % \
                (row_transformed, transform_cell(
                    m, row_index, cell_index, live_cell, dead_cell))
        m_transformed.append(row_transformed)
    return m_transformed
