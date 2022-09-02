class GriddlerModel:
    grid: [[str]] = None
    column_numbers: [int] = None
    row_numbers: [int] = None
    height: int = None
    width: int = None

    def _transpose_matrix_string(self, s: [str]) -> [str]:
        """
        Transpose a string in a rectangular matrix shape.
        The operation is a regular matrix transposition.
        E.g.

        abc     ae
        efg --> bf
                cg
        :param s: string (which is in a rectangular shape of M x N)
        :return: transposed string (N x M)
        """
        if not s:
            return
        s_transposed = []
        number_of_columns = len(s[0])

        for i in range(number_of_columns):
            transposed_row = ""
            for row in s:
                transposed_row += row[i]
            s_transposed.append(transposed_row)
        return s_transposed

    def from_string(self, s: str):
        rows = s.splitlines()
        # TODO translate s --> [[char]] IDEA??

        # TODO validate?? symbols, ...


        # validate same length
        if not rows:
            return
        row_length = len(rows[0])
        for row in rows:
            if row_length != len(row):
                raise ValueError("Different length") #TODO better error msg
            row_length = len(row)

        split_row_i = [pair[0] for pair in enumerate(rows) if "/" in pair[1]][0]
        split_column_i = [pair[0] for pair in enumerate(rows[split_row_i]) if "/" == pair[1]][0]

        self.height = len(rows) - split_row_i - 1
        self.width = len(rows[0]) - split_column_i - 1


        # [split_row_i, split_column_i] split point
        # Grid is on dimensions
        #   -->
        # |
        # V
        self.grid = []
        for row in rows[split_row_i + 1:]:
            self.grid.append(row[split_column_i + 1:])

        # Column numbers are on dimensions
        # A
        # |
        #   -->
        self.column_numbers = []
        for row in self._transpose_matrix_string(rows[:split_row_i])[split_column_i + 1:]:
            column_number_seq = []
            for character in reversed(row):
                column_number_seq.append(int(character))
            self.column_numbers.append(column_number_seq)

        # Row numbers are on dimensions
        # <--
        #    |
        #    V
        self.row_numbers = []
        for row in rows[split_row_i + 1:]:
            row_number_seq = []
            for character in row[:split_column_i]:
                row_number_seq.append(int(character))
            self.row_numbers.append(row_number_seq)

        # Filler symbols are on dimensions
        #    A
        #    |
        # <--
        print("INPUT STRING:")
        for row in rows:
            print(f"  -> {row}")

        print("HEIGHT:")
        print(f"  -> {self.height}")

        print("WIDTH:")
        print(f"  -> {self.width}")

        print("GRID:")
        for row in self.grid:
            print(f"  -> {row}")

        print("COLUMN_NUMBERS")
        for row in self.column_numbers:
            print(f"  -> {row}")

        print("ROW_NUMBERS")
        for row in self.row_numbers:
            print(f"  -> {row}")

    def to_string(self) -> str:
        pass

    def __repr__(self):
        pass