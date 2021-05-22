class Matrix:
    """
    def __init__(self, matrix_string):
        self.matrix = matrix_string.split(sep='\n') if matrix_string.find('\n') > 0 else [matrix_string]
        self.matrix = [list(map(int, self.matrix[i].split())) for i in range(len(self.matrix))]

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        changed = [[row[i] for row in self.matrix] for i in range(len(self.matrix[0]))]
        return changed[index-1]
    -
    Looking good!

    L3: Python provides a str.splitlines method that you may want to consider using.
    L3: Do you actually need the ternary expression here? str.split() and str.splitlines() should always return a list.
    L4, L10: Whenever you find yourself reaching for for i in range(len(thing)), ask yourself if you can use for t in
    thing instead. Often, that's sufficient. If you absolutely need the index, there is the enumerate() function. If
    you only need the index and not the actual value, only then is range() the right approach. In this case, you
    shouldn't actually need the index at all!
    L4: It's good practice to use a variable for just one purpose. It makes static type checking possible and keeps the
    logic clean since one variable isn't used for unrelated things. self.matrix is used to store two distinct data
    types.
    ------------------------------------------------------------------------------------------------------------------
    def __init__(self, matrix_string):
        self.matrix = [list(map(int, i.split())) for i in matrix_string.splitlines()]

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return list(map(list, zip(*self.matrix)))[index-1]
    -
    L3: This solution combines functions that act on lists (list(map(..))) with list comprehensions. Could you solve
    this with the consistent use of just list comprehensions?
    L9: This transposes the entire matrix then selects just one row, discarding the rest of the data. Do you need to
    actually transpose the matrix?
    -------------------------------------------------------------------------------------------------------------------
    """
    def __init__(self, matrix_string):
        self.matrix = [[int(i) for i in j.split()] for j in matrix_string.splitlines()]

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return [[row[i] for row in self.matrix] for i in self.matrix[index-1]]

# exercism submit Exercism/python/matrix/matrix.py