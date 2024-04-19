import numpy as np
import json
import os


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

        # Create a new numpy array with the specified size filled with zeros
        self._array: np.ndarray = np.zeros((size, size), dtype=bool)

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
        Cells outside of bounds ARE ASSUMED DEAD.

        :param tuple[int, int] key: a tuple containing the row and column indices
        :return: the state of the cell at the specified row and column
        :rtype: bool
        """
        row, col = key

        # If outside of bounds, assume dead
        if row < 0 or row >= self._size or col < 0 or col >= self._size:
            return False

        return self._array[row][col]

    def __setitem__(self, key: tuple[int, int], value: bool) -> None:
        """
        Allows setting the cell state at the specified (row, column) using array indexing.
        This method does nothing when the indicies are outside of bounds.

        :param tuple[int, int] key: a tuple containing the row and column indices
        :param bool value: the new state of the cell at the specified row and column
        """
        row, col = key

        # If outside of bounds, return
        if row < 0 or row >= self._size or col < 0 or col >= self._size:
            return

        self._array[row][col] = value

    def will_live(self, row: int, col: int) -> bool:
        """
        Determines if the cell at the specified row and column SHOULD be alive.
        For example, an alive cell surrounded by 9 dead cells will die.
        Cells on borders are considered dead.

        :param int row: the row index of the cell
        :param int col: the column index of the cell
        :return: whether the cell at the specified location is alive
        :rtype: bool
        """
        neighbors = self._count_neighbors(row, col)

        if self[row, col]:  # Living cases
            return neighbors in (2, 3)  # Keep alive if 2 or 3 neighbors
        else:  # Dead cases
            return neighbors == 3  # Reproduce with exactly 3 neighbors

    def _count_neighbors(self, row: int, col: int) -> int:
        """
        Counts the number of alive neighbors of the cell at the specified row and column.
        Cells on borders are considered dead.

        :param int row: the row index of the cell
        :param int col: the column index of the cell
        :return: the number of alive neighbors of the cell at the specified location
        :rtype: int
        """

        neighbors = 0

        # Check the 3x3 surrounding the provided cell location
        # Check row above through below
        for row_check in range(row - 1, row + 2):
            # Check column left through right
            for col_check in range(col - 1, col + 2):
                if self[row_check, col_check]:
                    neighbors += 1

        # Subtract out if the middle cell itself is alive
        if self[row, col]:
            neighbors -= 1

        return neighbors


class Random(World):
    """
    This class represents a random world. 
    Each cell is either alive or dead based on the life probability value. 
    """

    def __init__(self, size: int, probability: float) -> None:
        """
        Creates a new random world.

        :param float probability: the probability of a cell being alive
        """
        self._size = size

        # Set each cell to either alive or dead based on the probability
        self._array: np.ndarray = np.random.choice(
            [True, False], size=(size, size), p=[probability, 1 - probability])


PRESET_FILE_NAME = os.path.join("simul", "world_templates.json")


class Pulsar(World):
    """
    This class represents a pulsar world.
    The grid starts with cyclical pattern and alternates between three different patterns.

    Note: The pulsar requires a minimum size of 17 x 17 (size = 17).
    """

    def __init__(self, size: int) -> None:
        """
        Creates a new pulsar world.
        """
        self._size = size

        # Read the 2D JSON array from the file
        with open(PRESET_FILE_NAME, "r") as file:
            json_array = json.load(file)["pulsar"]

        # Create a new numpy array with the specified size filled with zeros
        self._array: np.ndarray = np.zeros((size, size), dtype=bool)

        # Get the dimensions of the JSON array
        json_rows = len(json_array)
        json_cols = len(json_array[0])

        # Calculate how many times the pattern can repeat
        n_rows = size // json_rows
        n_cols = size // json_cols

        # Fill the array with the pattern
        for row in range(n_rows * json_rows):
            for col in range(n_cols * json_cols):
                self._array[row][col] = json_array[row % json_rows][col % json_cols]


class Glider(World):
    """
    This class represents a pulsar world.
    The grid starts with cyclical pattern and alternates between three different patterns.

    Note: The glider requires a minimum size of 9 x 36 (size = 38).
    """

    def __init__(self, size: int) -> None:
        """
        Creates a new glider world.
        """
        self._size = size

        # Read the 2D JSON array from the file
        with open(PRESET_FILE_NAME, "r") as file:
            json_array = json.load(file)["glider"]

        # Create a new numpy array with the specified size filled with zeros
        self._array: np.ndarray = np.zeros((size, size), dtype=bool)

        # Get the dimensions of the JSON array
        json_rows = len(json_array)
        json_cols = len(json_array[0])

        # Fill the array with the pattern
        for row in range(min(size, json_rows)):
            for col in range(min(size, json_cols)):
                self._array[row][col] = json_array[row % json_rows][col % json_cols]
