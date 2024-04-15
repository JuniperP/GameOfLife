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
        
        pass

    @property
    def size(self) -> int:
        """
        Returns the size of the world.
        """
        return 6  # TODO - Replace with actual size

    def __getitem__(self, key: tuple[int, int]) -> int:
        """
        Allows accessing the cell state at the specified (row, column) using array indexing.
        Cells outside of bounds will be wrapped to the other side.

        :param key: a tuple containing the row and column indices
        :return: the state of the cell at the specified row and column
        """
        # row, col = key
        # row = row % self.size
        # col = col % self.size
        # return self.cells[row][col]

        
        return 0  # TODO - Replace with actual cell state

    def __setitem__(self, key: tuple[int, int], value: int) -> None:
        """
        Allows setting the cell state at the specified (row, column) using array indexing.
        Cells outside of bounds will be wrapped to the other side.
        """
        pass

    def is_alive(self, row: int, col: int) -> bool:
    
        """
        Determines if the cell at the specified row and column is alive.
        Cells on borders wrap around to the other side when checking their neighbors.
 
        :return: whether the cell at the specified location is alive
        """
        return True  # TODO - Replace with actual value

    def count_neighbors(self, row: int, col: int) -> int:
        """
        Counts the number of alive neighbors of the cell at the specified row and column.
        Cells on borders wrap around to the other side when counting their neighbors.

        :return: the number of alive neighbors of the cell at the specified location
        """
        return 0  # TODO - Replace with actual value

    


class Random(World):

    def __init__(self):
        pass


class Pulsar(World):

    def __init__(self):
        pass


class Glider(World):

    def __init__(self):
        pass
