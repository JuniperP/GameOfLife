from pyscript import document
from simul.world import World


class Grid:

    # Constant for the HTML element of the table data cell
    GRID_TEMPLATE = '<td id="{row},{col}" class="cell {living_dead}"></td>'

    def __init__(self, world: World, grid_id: str = "grid"):
        """
        Creates a new grid as a HTML table representing the world values.
        
        param: World world: the world to display with the grid
        param: str grid_id: the ID of the HTML element of the grid
        """
        self._world: World = world
        self._grid_elem = document.getElementById(grid_id)
        self.create_grid()

    def create_grid(self):
        """
        Creates the grid as a HTML table.
        """
        grid_HTML = "<tbody>"  # Start table body

        # Create the rows
        for row in range(self._world.size):
            grid_HTML += "<tr>"  # Start row

            # Create a cell for every column of the row
            for col in range(self._world.size):
                living_text = "alive" if self._world[row, col] else "dead"
                grid_HTML += self.GRID_TEMPLATE.format(
                    row=row,
                    col=col,
                    living_dead=living_text,
                )

            grid_HTML += "</tr>"  # Close row

        grid_HTML += "</tbody>"  # Close table body

        self._grid_elem.innerHTML = grid_HTML

    def update(self):
        """
        Updates the grid to the current world values.
        """
        for row in range(self._world.size):
            for col in range(self._world.size):
                living_text = "alive" if self._world[row, col] else "dead"
                document.getElementById(
                    f"{row},{col}").className = f"cell {living_text}"
