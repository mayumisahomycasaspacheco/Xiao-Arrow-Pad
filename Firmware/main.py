# Hello, I'm michisistemas, here I'll be making the firmware for Miauyummi's First Project

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC

keyboard = KMKKeyboard()

# EXACT pins according to my KiCad schematic

PINS = [
    board.GP1,  # SW1 → GPIO1 → Izquierda
    board.GP2,  # SW2 → GPIO2 → Abajo
    board.GP4,  # SW3 → GPIO4 → Derecha
    board.GP3,  # SW4 → GPIO3 → Arriba
    board.GP7,  # SW5 → GPIO7 → Espacio
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [[
    KC.LEFT,   # SW1
    KC.DOWN,   # SW2
    KC.RIGHT,  # SW3
    KC.UP,     # SW4
    KC.SPACE,  # SW5
]]

keyboard.go()