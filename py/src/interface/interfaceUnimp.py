from pyscript import document
from pyodide.ffi.wrappers import add_event_listener
from input import Slider
# from simul.simulation import WorldType, Simulation
# from grid import Grid


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


world_select = document.getElementById("world-select")


def world():
    if world_select.value == "random":
        print("random")
    elif world_select.value == "pulsar":
        print("pulsar")
    elif world_select.value == "glider":
        print("glider")


