from pyscript import document

def main():
    print("Main function")

def change_button(event):
    button_text = "Click Me More!"
    document.getElementById("click_me").innerText = button_text
