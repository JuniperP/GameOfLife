from enum import Enum
from world import World


class WorldType(Enum):
    RANDOM = 0
    PULSAR = 1
    GLIDER = 2


class Simulation:
    """
    This class represents a simulation of the Conway's Game of Life.
    It provides the ability to step through a generation (iteration)
    of the simulation.
    """

    def __init__(self, world_type: WorldType) -> None:
        """
        Creates a new simulation of the world type specified.

        @param world_type: the type of world to use for the simulation
        """
        pass

    @property
    def world(self) -> World:
        """
        Returns the current world.
        """
        return World(1)  # TODO - Replace with actual world

    def step(self) -> None:
        """
        Steps the simulation forward one generation.
        """
        pass

    def reset(self) -> None:
        """
        Resets the simulation to the initial state.
        """
        pass
