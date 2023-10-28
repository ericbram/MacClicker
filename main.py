import pyautogui
import time
import json

coordinates_file = "coordinates.json"

def click_at_coordinates(x, y, interval=0.0):
    pyautogui.click(x=x, y=y, clicks=1, interval=interval)
    time.sleep(interval)

if __name__ == "__main__":
    with open(coordinates_file, 'r') as file:
        data = json.load(file)
        repeat = data['repeat']
        coordinates = data['coordinates']
        for i in range(repeat):
            for coordinate in coordinates:
                x = coordinate['x']
                y = coordinate['y']
                try:
                    click_at_coordinates(x, y, 2)
                except Exception as e:
                    print(f"Error: {e}")
