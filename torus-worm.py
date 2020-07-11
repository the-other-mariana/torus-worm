#File:      torus-worm.py
#Author:    Mariana Avalos
#Date:      11/07/2020
#Description: Python code that makes an animated torus

import maya.cmds as c
import math as math

sections = 6
inner_radius = 3
distance = 5
PI = 3.1416
z = 0
step_angle = 360.0 / sections

for i in range(sections):
    rads = (step_angle * PI / 180.0)
    x = distance + inner_radius * math.cos(i * rads - (rads / 2.0))
    y = inner_radius * math.sin(i * rads - (rads / 2.0))

    # points as spheres
    c.polySphere(sx = 5, sy = 5, r = 0.5, n = 'point{}'.format(i))
    c.setAttr('point{}.translateX'.format(i), x)
    c.setAttr('point{}.translateZ'.format(i), z)
    c.setAttr('point{}.translateY'.format(i), y)
