#File:      torus-worm.py
#Author:    Mariana Avalos
#Date:      11/07/2020
#Description: Python code that makes an animated torus

import maya.cmds as c
import math as math

tubes = 9
sections = 6
inner_radius = 3
distance = 5
PI = 3.1416
z = 0
step_outer_angle = 360.0 / tubes
step_inner_angle = 360.0 / sections

for j in range(tubes):
    outer_rads = (step_outer_angle * PI / 180.0)
    outer_distance = 0.0
    x = 0.0
    y = 0.0
    z = 0.0
    for i in range(sections):
        inner_rads = (step_inner_angle * PI / 180.0)
        inner_x = distance + inner_radius * math.cos(i * inner_rads - (inner_rads / 2.0))
        inner_y = inner_radius * math.sin(i * inner_rads - (inner_rads / 2.0))

        outer_distance = inner_x
        y = inner_y

        x = outer_distance * math.sin(j * outer_rads - (outer_rads / 2.0))
        z = outer_distance * math.cos(j * outer_rads - (outer_rads / 2.0))

        # points as spheres
        c.polySphere(sx = 5, sy = 5, r = 0.5, n = 'point{}{}'.format(i, j))
        c.setAttr('point{}{}.translateX'.format(i, j), x)
        c.setAttr('point{}{}.translateZ'.format(i, j), z)
        c.setAttr('point{}{}.translateY'.format(i, j), y)
