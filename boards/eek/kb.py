# This is for the eek! with silk side down. and the KB2040 from Adafruit

import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.matrix import DiodeOrientation
from kmk.matrix import intify_coordinate as ic

class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.D4,
        board.D5,
        board.D10,
        board.MOSI,
        board.MISO,
        board.SCK,
        board.A0,
        board.A1,
        board.A2,
        board.A3,
    )
    row_pins = (board.D6, board.D7, board.D8, board.D9)

    diode_orientation = DiodeOrientation.COLUMNS
    rgb_pixel_pin = board.D0
    rgb_num_pixels = 36
    i2c = board.I2C

    coord_mapping = []
    coord_mapping.extend(ic(0, x) for x in range(10))
    coord_mapping.extend(ic(1, x) for x in range(10))
    coord_mapping.extend(ic(2, x) for x in range(10))
    #bottom row only has 6 keys total
    coord_mapping.extend(ic(3, x) for x in range(2,7))