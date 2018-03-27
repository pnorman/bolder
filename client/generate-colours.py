#!/usr/bin/env python

from colormath.color_objects import sRGBColor, LCHabColor
from colormath.color_conversions import convert_color

greys = [(0, l, 0) for l in range(0, 100+5, 5)] # Greys are hue 0, not hue 360. Also include 100% lightness which is not part of print atlas
pastels = [(h, l, 5) for h in range(30, 360+30, 30) for l in range(5,100,5)]
colours = [(h, l, c) for h in range(10, 360+10, 10) for l in [15, 25, 35, 45, 55, 65, 75, 85, 90] for c in range(10, 100, 10)]


def InGamut(c):
    return not (c.rgb_r <= 0 or c.rgb_r >= 1 or c.rgb_g <= 0 or c.rgb_g >= 1 or c.rgb_b <= 0 or c.rgb_b >= 1)


print('''# This file has the RGB values for HLC colours from the freecolour.org system.
# As an expression of the CIELa*b* and colour coversions, it's a mathematical model, free of copyright.
# Colours are calculated by generate-colours.py
global:
  freecolour:''')
for colour in greys + pastels + colours:
    srgb = convert_color(LCHabColor(colour[1], colour[2], colour[0]), sRGBColor)
    if InGamut(srgb):
        print("    H%03d_L%02d_C%03d: '%s'" % (colour[0], colour[1], colour[2], srgb.get_rgb_hex()))
