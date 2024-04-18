from pyscript import document
from pyodide.ffi.wrappers import add_event_listener

from interface.input import Slider, Button, Dropdown, Numerical
from interface.grid import Grid
from simul.simulation import Simulation, WorldType
from simul.world import World, Random, Pulsar, Glider


def main():
    global mySim, myGrid, myWorld, myWorldType, mySlider, myButton, myDropdown

    def generateWorld(event):
        global mySim, myGrid, mySlider
        mySim = Simulation(mySlider.value, WorldType.RANDOM)
        myGrid = Grid(mySim.world, "grid")

    def simulationStep(event):
        global mySim, myGrid
        mySim.step()
        myGrid.update(mySim.world)

    def updateNumerical(event):
        myNumerical.value = mySlider.value

    def updateSlider(event):
        mySlider.value = myNumerical.value

    def updateSliderMin(event):
        pass

    def startStop(event):
        pass

    myNumerical = Numerical("size_num", updateSlider)
    mySlider = Slider("size_slider", updateNumerical)
    generate_world_btn = Button("world_generate", generateWorld)
    stepButton = Button("world_step", simulationStep)
    startStopButton = Button("start_stop", startStop)
    myDropDown = Dropdown("world_select")


if __name__ == "__main__":
    main()
