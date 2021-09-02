def print_matrix(matrix, fmt="g"):
    """Pretty prints a 2d matrix
    Parameters:
        matrix: `np.array`
            a 2D numpy array
    """
    col_maxes = [max([len(("{:"+fmt+"}").format(x)) for x in col]) for col in matrix.T]
    for x in matrix:
        for i, y in enumerate(x):
            print(("{:"+str(col_maxes[i])+fmt+"}").format(y), end="  ")
        print("")



def get_column(data, index=0):
    """Get a column from a dataset
    Parameters:
        data: Could be a list of list or a list of dict, etc
            Given a = [{"k1":1, "k2":5},{"k1":3, "k2":5},{"k1":2, "k2":5}]
            get_column(a, "k1") will get the values of k1
    Returns:
        list: of values that belong to the column
    """
    result = []
    for row in data:
        result.append(row[index])
    return result
