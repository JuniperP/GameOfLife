class World:
    """
    This class represents a world of cells.
    It uses a 2D array of 1's and 0's to represent the cells.
    """

    def __init__(self, size: int) -> None:
        """
        Creates a new world of the specified size.
        This will be a square world with sidelength size.

        :param size: the size of the world
        """
        self._size = size
        # self._array = np.zeros((size, size), dtype=np.int8)

    @property
    def size(self) -> int:
        """
        Returns the size of the world.

        :return: the size of the world
        :rtype: int
        """
        return self._size

    def __getitem__(self, key: tuple[int, int]) -> bool:
        """
        Allows accessing the cell state at the specified (row, column) using array indexing.
        Cells outside of bounds will be wrapped to the other side.

        :param tuple[int, int] key: a tuple containing the row and column indices
        :return: the state of the cell at the specified row and column
        :rtype: bool
        """
        # row, col = key
        # row = row % self.size
        # col = col % self.size
        # return self.cells[row][col]

        return False  # TODO - Replace with actual cell state

    def __setitem__(self, key: tuple[int, int], value: bool) -> None:
        """
        Allows setting the cell state at the specified (row, column) using array indexing.
        Cells outside of bounds will be wrapped to the other side.

        :param tuple[int, int] key: a tuple containing the row and column indices
        :param bool value: the new state of the cell at the specified row and column
        """
        pass

    def _is_alive(self, row: int, col: int) -> bool:
        """
        Determines if the cell at the specified row and column SHOULD be alive.
        For example, an alive cell surrounded by 9 dead cells will die.
        Cells on borders wrap around to the other side when checking their neighbors.

        :param int row: the row index of the cell
        :param int col: the column index of the cell
        :return: whether the cell at the specified location is alive
        :rtype: bool
        """

        return True  # TODO - Replace with actual value

    def _count_neighbors(self, row: int, col: int) -> int:
        """
        Counts the number of alive neighbors of the cell at the specified row and column.
        Cells on borders wrap around to the other side when counting their neighbors.

        :param int row: the row index of the cell
        :param int col: the column index of the cell
        :return: the number of alive neighbors of the cell at the specified location
        :rtype: int
        """
        return 0  # TODO - Replace with actual value


class Random(World):
    """
    This class represents a random world. 
    Each cell is either alive or dead based on the life probability value. 
    """

    def __init__(self, probability: float) -> None:
        """
        Creates a new random world.

        :param float probability: the probability of a cell being alive
        """
        pass

    def randomize(self) -> None:
        """
        Randomizes the world by setting each cell to either alive or dead based
        on the probability value.
        """
        pass


class Pulsar(World):
    """
    This class represents a pulsar world.
    Grid starts with cyclical pattern alternates between three different patterns   
    """

    def __init__(self) -> None:
        """
        Creates a new pulsar world.
        """
        pass


class Glider(World):
    """
    This class represents a glider world.
    The glider moves across the grid by moving the cells.
    """

    def __init__(self) -> None:
        """
        Creates a new glider world.
        """
        pass
