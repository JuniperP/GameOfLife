from py.src.interface.input import Dropdown
from pyscript import document
from pyodide.ffi.wrappers import add_event_listener
from input import Slider, Button
from grid import Grid
from world import World
# from simul.simulation import WorldType, Simulation


def change_button(event):
    button_text = "Click Me More!"
    document.getElementById("click_me").innerText = button_text

print("Hello World")

# def init_slider():
#     size_slider = document.getElementById("size_slider")
#     size_display = document.getElementById("size_value")

#     def update_slider(event):
#         size_display.innerText = size_slider.value
#         print(type(event))

#     update_slider(None)
#     add_event_listener(size_slider, "input", update_slider)

mySlider = Slider("size_slider", "size_value")
myDropDown = Dropdown("world_select", ")

myGrid = Grid(World(6))

world_select = document.getElementById("world-select")
