from enum import Enum
from simul.world import World, Random, Pulsar, Glider


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

    def __init__(self,
                 world_size: int,
                 world_type: WorldType,
                 rand_chance: float = 0.5) -> None:
        """
        Creates a new simulation of the world type specified.

        :param int world_size: the size of the world
        :param WorldType world_type: the type of world to create
        :param float rand_chance: the probability of a cell being alive for random worlds
        """
        self._world_type = world_type

        match self._world_type:
            case WorldType.RANDOM:
                self._world = Random(world_size, rand_chance)
            case WorldType.PULSAR:
                self._world = Pulsar(world_size)
            case WorldType.GLIDER:
                self._world = Glider(world_size)

    @property
    def world(self) -> World:
        """
        Returns the current world.

        :return: the current world being stored in the simulation
        :rtype: World
        """
        return self._world

    def step(self) -> None:
        """
        Steps the simulation forward one generation.
        """
        futureWorld = World(self.world.size)

        for row in range(self.world.size):
            for col in range(self.world.size):
                futureWorld[row, col] = self.world.will_live(row, col)

        self._world = futureWorld
