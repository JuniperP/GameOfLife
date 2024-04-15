from world import World
from pyscript import document


class Grid:

    GRID_TEMPLATE = '<td id="{row},{col}" class="cell_{living_dead}"></td>'
    
    def __init__(self, world: World, grid_id: str = "grid"):
        """
        Creates a new grid as a HTML table representing the world values.
        
        param: World world: Uses the world to display the grid
        """
        self._world: World = world
        self._grid_elem = document.getElementById(grid_id)
        self.create_grid()

    def create_grid(self):
        """
        Creates the grid as a HTML table.
        """
        grid_HTML = "<tbody>"
        
        for row in range(self._world.size):
            grid_HTML += "<tr>"

            for col in range(self._world.size):
                living_text: str = "alive" if self._world[row, col] else "dead"
                grid_HTML += self.GRID_TEMPLATE.format(
                    row=row,
                    col=col,
                    living_dead=living_text,
                )

            grid_HTML += "</tr>"

        grid_HTML += "</tbody>"

        self._grid_elem.innerHTML = grid_HTML

    def repopulate(self):
        """
        Changes the grid to the current world values.
        """
