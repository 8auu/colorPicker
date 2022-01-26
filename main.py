import clipboard
import keyboard
import pyautogui
from infi.systray import SysTrayIcon
from pynput.mouse import Controller

systray = SysTrayIcon("logo.ico",
                      "8au's colorPicker\nShortcuts:\nRGB color = ctrl + shift + L\nHex color: ctrl + shift + k")
systray.start()

mouse = Controller()


def from_rgb(rgb):
    return "#%02x%02x%02x" % rgb


def get_rgb_color(is_rgb: bool):
    current_mouse_position = mouse.position
    if is_rgb:
        rgb = pyautogui.pixel(current_mouse_position[0], current_mouse_position[1])
        return rgb
    elif not is_rgb:
        rgb_to_convert = pyautogui.pixel(current_mouse_position[0],
                                         current_mouse_position[1])
        hex_code = from_rgb(rgb_to_convert)
        return hex_code


def main():
    while True:
        if keyboard.is_pressed('shift') and keyboard.is_pressed("ctrl") and keyboard.is_pressed("l"):
            rgb = get_rgb_color(True)
            clipboard.copy(str(rgb))
            clipboard.paste()
        if keyboard.is_pressed('shift') and keyboard.is_pressed("ctrl") and keyboard.is_pressed("k"):
            hex_code = get_rgb_color(False)
            clipboard.copy(str(hex_code))
            clipboard.paste()


main()
