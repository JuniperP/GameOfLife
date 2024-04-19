from pyscript import document
from pyodide.ffi.wrappers import add_event_listener

from interface.input import Slider, Button, Dropdown, Numerical
from interface.grid import Grid
from simul.simulation import Simulation, WorldType
from simul.world import World, Random, Pulsar, Glider

def str_to_world_type(str: str) -> WorldType:
    """
    Converts a string to a WorldType enum value.

    :param str str: the string to convert
    :return: the WorldType enum value
    :rtype: WorldType
    """
    match str:
        case "random":
            return WorldType.RANDOM
        case "pulsar":
            return WorldType.PULSAR
        case "glider":
            return WorldType.GLIDER
        case _:
            raise ValueError(f"Invalid world type: {str}")

size_requirements = {
    "random": 5,
    "pulsar": 17,
    "glider": 36,
}

def main():
    global world_sim, grid, size_slider, type_selector

    def generateWorld(event):
        global world_sim, grid, size_slider, type_selector

        world_type = str_to_world_type(type_selector.value)
        world_sim = Simulation(size_slider.value, world_type)
        grid = Grid(world_sim.world, "grid")
        step_button.disabled = False
        play_button.disabled = False

    def simulationStep(event):
        global world_sim, grid
        
        world_sim.step()
        grid.update(world_sim.world)

    def updateNumerical(event):
        myNumerical.value = size_slider.value

    def updateSlider(event):
        size_slider.value = myNumerical.value

    def updateSliderMin(event):
        world_min = size_requirements[type_selector.value]
        size_slider.min = world_min
        updateNumerical(None)

    def start_stop(event):
        pass  # Unimplemented
    
    myNumerical = Numerical("size_num", updateSlider)
    size_slider = Slider("size_slider", updateNumerical)
    gen_button = Button("world_generate", generateWorld)
    step_button = Button("world_step", simulationStep)
    play_button = Button("start_stop", start_stop)
    type_selector = Dropdown("world_select", updateSliderMin)


if __name__ == "__main__":
    main()
