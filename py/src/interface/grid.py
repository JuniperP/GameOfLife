from simul.world import World


class Grid:

    def __init__(self, world: World):
        """
        Creates a new grid as a HTML table representing the world values.

        param: World world: Uses the world to display the grid
        """
        self._world = world

    def repopulate(self):
        """
        Changes the grid to the new world values.
        """
