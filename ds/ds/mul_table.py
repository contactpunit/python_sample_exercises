class MultiplicationTable:

    def __init__(self, length):
        """Create a 2D self._table of (x, y) coordinates and
           their calculations (form of caching)"""
        self.length = length
        self._table = {
            (i, j): i * j
            for i in range(1, length + 1)
            for j in range(1, length + 1)
        }
        print(self._table)

    def __len__(self):
        """Returns the area of the table (len x* len y)"""
        return self.length * self.length

    def __str__(self):
        return '\n'.join(
            [
                ' | '.join(
                    [
                        str(self._table[(i, j)])
                        for j in range(1, self.length + 1)
                    ]
                )
                for i in range(1, self.length + 1)
            ]
        )

    def calc_cell(self, x, y):
        """Takes x and y coords and returns the re-calculated result"""
        try:
            return self._table[(x, y)]
        except KeyError as e:
            raise IndexError()


m = MultiplicationTable(3)
print(m)
