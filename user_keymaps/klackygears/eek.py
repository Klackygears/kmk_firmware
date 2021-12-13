from kb import KMKKeyboard
from kmk.extensions.RGB import RGB, AnimationModes
#from kb import rgb_pixel_pin
from kmk.keys import KC
from kmk.modules.layers import Layers


keyboard = KMKKeyboard()

#Uncomment this next line if you want the bat silk facing up
#keyboard.col_pins = tuple(reversed(keyboard.col_pins))

# Adding extensions
rgb = RGB(pixel_pin=keyboard.rgb_pixel_pin, num_pixels=keyboard.rgb_num_pixels)
#keyboard.extensions.append(rgb_ext)

layers_ext = Layers()

keyboard.modules = [layers_ext]

keyboard.extensions = [rgb]

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

LOWER = KC.MO(1)
RAISE = KC.MO(2)
ADJUST = KC.LT(3, KC.SPC)


keyboard.keymap = [
    # Qwerty
    # ,----------------------------------.           ,----------------------------------.
    # |   Q  |   W  |   E  |   R  |   T  |           |   Y  |   U  |   I  |   O  |   P  |
    # |------+------+------+------+------|           |------+------+------+------+------|
    # |   A  |   S  |   D  |   F  |   G  |           |   H  |   J  |   K  |   L  |   ;  |
    # |------+------+------+------+------|           |------+------+------+------+------|
    # |   Z  |   X  |   C  |   V  |   B  |           |   N  |   M  |   ,  |   .  |   /  |
    # `-------------+------+------+------|           |------+------+------+-------------'
    #               | Ctrl | LOWER| Space|           |BckSpc| RAISE| Shift|
    #               `--------------------'           `--------------------'
    #/
    [  #QWERTY
        KC.Q,    KC.W,    KC.E,     KC.R,    KC.T,       KC.Y,      KC.U,    KC.I,      KC.O,    KC.P,\
        KC.A,    KC.S,    KC.D,     KC.F,    KC.G,       KC.H,      KC.J,    KC.K,      KC.L,    KC.SCLN,\
        KC.Z,    KC.X,    KC.C,     KC.V,    KC.B,       KC.N,      KC.M,    KC.COMM,   KC.DOT,  KC.SLSH,\
                          KC.LCTL,  LOWER,   ADJUST,     KC.BSPC, RAISE,   KC.LSHIFT,
    ],
    [  #LOWER
        KC.EXLM, KC.AT,   KC.HASH,  KC.DLR, KC.PERC,     KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN,  KC.RPRN,\
        KC.ESC,  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,     XXXXXXX, KC.UNDS, KC.PLUS, KC.LCBR,  KC.RCBR,\
        KC.CAPS, KC.TILD, XXXXXXX, XXXXXXX, XXXXXXX,     XXXXXXX, XXXXXXX, XXXXXXX, KC.PIPE,  KC.DQT,\
                          KC.LCTL, LOWER,   ADJUST,      KC.ENT,  RAISE,   KC.DEL,
    ],
    [  #RAISE
        
        KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,       KC.N6,   KC.N7,   KC.N8,   KC.N9,    KC.N0,\
        KC.TAB,  KC.LEFT, KC.DOWN, KC.UP,   KC.RIGHT,    XXXXXXX, KC.MINS,  KC.EQL, KC.LBRC,  KC.RBRC,\
        KC.LCTL, KC.GRV,  KC.LGUI, KC.LALT, XXXXXXX,     KC.UNDS, KC.PLUS, KC.LBRC, KC.RBRC,  KC.BSLS,\
                          KC.LCTL, LOWER,   ADJUST,      KC.ENT,   RAISE,  KC.RALT,
    ],
    [  #ADJUST
         KC.RGB_M_P, KC.RGB_HUI,  KC.RGB_SAI, KC.RGB_VAI, KC.RGB_ANI,     KC.RGB_TOG, KC.F9,   KC.F10,  KC.F11, KC.F12,\
         KC.RGB_M_B, KC.RGB_HUD,  KC.RGB_SAD, KC.RGB_VAD, KC.RGB_AND,     XXXXXXX,    KC.F5,   KC.F6,   KC.F7,  KC.F8,\
         KC.RGB_M_R, KC.RGB_M_BR, KC.RGB_M_K, KC.RGB_M_S, XXXXXXX,        XXXXXXX,    KC.F1,   KC.F2,   KC.F3,  KC.F4,\
                                  KC.LCTL,    LOWER,      ADJUST,         KC.ENT,     RAISE,   KC.RALT,
    ]
]

if __name__ == '__main__': 
    keyboard.go()
