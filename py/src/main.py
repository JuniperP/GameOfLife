from pyscript import document
from pyodide.ffi.wrappers import add_event_listener

from interface.input import Slider, Button, Dropdown, Numerical
from interface.grid import Grid
from simul.simulation import Simulation, WorldType
from simul.world import World, Random, Pulsar, Glider


def main():
    global world_sim, grid, size_slider, type_selector

    def generateWorld(event):
        global world_sim, grid, size_slider, type_selector
        world_sim = Simulation(size_slider.value, WorldType.PULSAR)
        grid = Grid(world_sim.world, "grid")
        stepButton.disabled = False
        startStopButton.disabled = False

    def simulationStep(event):
        global world_sim, grid
        world_sim.step()
        grid.update(world_sim.world)

    def updateNumerical(event):
        myNumerical.value = size_slider.value

    def updateSlider(event):
        size_slider.value = myNumerical.value

    def updateSliderMin(event):
        pass

    def startStop(event):
        pass
    
    myNumerical = Numerical("size_num", updateSlider)
    size_slider = Slider("size_slider", updateNumerical)
    gen_button = Button("world_generate", generateWorld)
    stepButton = Button("world_step", simulationStep)
    startStopButton = Button("start_stop", startStop)
    type_selector = Dropdown("world_select")



if __name__ == "__main__":
    main()
