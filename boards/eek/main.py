from kb import KMKKeyboard
from kmk.extensions.RGB import RGB, AnimationModes
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap

keyboard = KMKKeyboard()
keyboard.tap_time = 200

#Uncomment this next line if you want the bat silk facing up
#keyboard.col_pins = tuple(reversed(keyboard.col_pins))

# Adding extensions
rgb = RGB(pixel_pin=keyboard.rgb_pixel_pin, num_pixels=keyboard.rgb_num_pixels)


layers_ext = Layers()
modtap_ext = ModTap()


keyboard.modules = [layers_ext, modtap_ext]
keyboard.extensions = [rgb]

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

#LOWER = KC.MO(1)
#RAISE = KC.MO(2)
#ADJUST = KC.LT(3, KC.SPC)

SYMENT = KC.LT(1, KC.ENT)
NUMBS = KC.LT(2, KC.BSPC)
FNENT = KC.LT(3, KC.ENT)
MEDAZ = KC.LT(3, KC.Z)

#ModTap keys row below home row
MT_JCTL = KC.MT(KC.J, KC.LCTRL)
MT_QALT = KC.MT(KC.Q, KC.LALT)
MT_SCGUI = KC.MT(KC.SCLN, KC.LGUI)
MT_WCTL = KC.MT(KC.W, KC.RCTRL)
MT_VALT = KC.MT(KC.V, KC.RALT)
#MT_ZGUI = KC.MT(KC.Z, KC.RGUI)
#ModTap keys row below home row numbers
MTTWCTL = KC.MT(KC.N2, KC.RCTRL)
MTTHALT = KC.MT(KC.N3, KC.RALT)
MTZEGUI = KC.MT(KC.N0, KC.RGUI)

MT_SPSFT = KC.MT(KC.SPC, KC.LSFT)


keyboard.keymap = [
    [  #DVORAK
        KC.QUOT,  KC.COMM, KC.DOT,   KC.P,    KC.Y,       KC.F,    KC.G,   KC.C,    KC.R,    KC.L,\
        KC.A,     KC.O,    KC.E,     KC.U,    KC.I,       KC.D,    KC.H,   KC.T,    KC.N,    KC.S,\
        MT_SCGUI, MT_QALT, MT_JCTL,  KC.K,    KC.X,       KC.B,    KC.M,   MT_WCTL, MT_VALT, MEDAZ,\
                           FNENT,  NUMBS,   MT_SPSFT,     KC.TAB, SYMENT, KC.N2,
    ],
    [  #SYMBOL
        KC.DQT,  KC.AT,   KC.HASH, KC.DLR,  KC.PERC,     KC.MINS, KC.UNDS, KC.PIPE, XXXXXXX,  XXXXXXX,\
        KC.LBRC, KC.RBRC, KC.LPRN, KC.RPRN, KC.AMPR,     KC.DQT,  XXXXXXX, KC.ASTR, XXXXXXX,  XXXXXXX,\
        KC.LCBR, KC.RCBR, KC.TILD, KC.CIRC, KC.GRV,      XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,  XXXXXXX,\
                          KC.NLCK, KC.DEL,  KC.SLCK,     XXXXXXX, XXXXXXX, XXXXXXX,
    ],
    [  #NUMBERS, ARROWS, & Excel Shortcuts 
        KC.HOME, KC.END,  KC.PGUP, KC.PGDN, KC.TRNS,    KC.TRNS, KC.N7,   KC.N8,    KC.N9,   KC.COLN,\
        KC.LEFT, KC.UP,   KC.DOWN, KC.RGHT, KC.AMPR,    XXXXXXX, KC.N4,   KC.N5,    KC.N6,   KC.SCLN,\
        XXXXXXX, XXXXXXX, KC.TILD, KC.CIRC, KC.GRV,     KC.UNDS, KC.N1,   MTTWCTL,  MTTHALT, MTZEGUI,\
                          XXXXXXX, XXXXXXX, XXXXXXX,    XXXXXXX, KC.LSFT, KC.N0,
    ],
    [  #FUNCTION
        KC.RGB_M_P, KC.RGB_HUI,  KC.RGB_SAI, KC.RGB_VAI, KC.RGB_ANI,     KC.RGB_TOG, KC.F9,   KC.F10,  KC.F11, KC.F12,\
        KC.RGB_M_B, KC.RGB_HUD,  KC.RGB_SAD, KC.RGB_VAD, KC.RGB_AND,     XXXXXXX,    KC.F5,   KC.F6,   KC.F7,  KC.F8,\
        KC.RGB_M_R, KC.RGB_M_BR, KC.RGB_M_K, KC.RGB_M_S, XXXXXXX,        XXXXXXX,    KC.F1,   KC.F2,   KC.F3,  KC.F4,\
                                 KC.LCTL,    XXXXXXX,    KC.LSFT,        KC.ENT,     XXXXXXX,   KC.CAPS,
    ],
    [  #MEDIA
        KC.RGB_M_P, KC.RGB_HUI,  KC.RGB_SAI, KC.RGB_VAI, KC.RGB_ANI,     KC.RGB_TOG, KC.F9,   KC.F10,  KC.F11, KC.F12,\
        KC.RGB_M_B, KC.RGB_HUD,  KC.RGB_SAD, KC.RGB_VAD, KC.RGB_AND,     XXXXXXX,    KC.F5,   KC.F6,   KC.F7,  KC.F8,\
        KC.RGB_M_R, KC.RGB_M_BR, KC.RGB_M_K, KC.RGB_M_S, XXXXXXX,        XXXXXXX,    KC.F1,   KC.F2,   KC.F3,  KC.F4,\
                                 XXXXXXX,    XXXXXXX,    KC.LSFT,        KC.ENT,     XXXXXXX, XXXXXXX,
    ]
]

if __name__ == '__main__':
    keyboard.go()
