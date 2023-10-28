import json
import threading
from pynput.mouse import Listener

# List to store recorded clicks
clicks = []

# Function to handle mouse clicks and add them to the list
def on_click(x, y, button, pressed):
    if pressed:
        clicks.append({"x": int(x), "y": int(y)})
        with open("record.json", "w") as json_file:
            json.dump(clicks, json_file, indent=4)


with Listener(
        on_click=on_click) as listener:
    listener.join()