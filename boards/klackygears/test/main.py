import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide, SplitType

keyboard = KMKKeyboard()



keyboard.col_pins = (board.D2, board.D4, board.D5, board.D6, board.D7, board.D8, board.D9)
keyboard.row_pins = (board.A3, board.A2, board.A1, board.A0, board.SCK)
keyboard.rollover_cols_every_rows = 4
keyboard.diode_orientation = DiodeOrientation.COL2ROW

split_side = SplitSide.LEFT
split = Split(split_type=SplitType.BLE, split_side=split_side)

layers_ext = Layers()

keyboard.modules = [layers_ext, split]

keyboard.keymap = [
    [

        KC.N1, KC.Q,  KC.W,  KC.E,  KC.R,  KC.T,  KC.N1,        KC.N2, KC.Y,   KC.U,   KC.I,   KC.O,   KC.P,   KC.N2,
        KC.N1, KC.A,  KC.S,  KC.D,  KC.F,  KC.G,  KC.N1,        KC.N2, KC.H,   KC.J,   KC.K,   KC.L,   KC.N2,  KC.N2,
        KC.N1, KC.Z,  KC.X,  KC.C,  KC.V,  KC.B,  KC.N1,        KC.N2, KC.N,   KC.M,   KC.N2,  KC.N2,  KC.N2,  KC.N2,
        KC.N1, KC.N1,  KC.N1,  KC.N1,  KC.N1,  KC.N1,  KC.N1,   KC.N2, KC.N2,  KC.N2,  KC.N2,  KC.N2,  KC.N2,  KC.N2, 
        KC.N1, KC.N1,  KC.N1,  KC.N1,  KC.N1,  KC.N1,  KC.N1,   KC.N2, KC.N2,  KC.N2,  KC.N2,  KC.N2,  KC.N2,  KC.N2, 
    ]
]


if __name__ == '__main__':
    keyboard.go()