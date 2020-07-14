#File:      torus-worm.py
#Author:    Mariana Avalos
#Date:      11/07/2020
#Description: Python code that makes a torus with flower or worm-like figure

import maya.cmds as c
import math as math
import maya.OpenMaya as OM


# modifiable parameters
tubes = 60
sections = 20
inner_radius = 3
distance = 5
spikey = False
flower = True
n_modifs = 6
strength_modif = 0.5


# constants, not for modification
PI = 3.1416
z = 0
step_outer_angle = 360.0 / tubes
step_inner_angle = 360.0 / sections
verts = []
mesh = OM.MFnMesh()
mergeVerts = True
pointTolerance = 0.001
radius_modif = 1
spikey_modif = 1
flower_modif = 1

# creating the points
for j in range(tubes):
    outer_rads = (step_outer_angle * PI / 180.0)
    outer_distance = 0.0
    x = 0.0
    y = 0.0
    z = 0.0
    for i in range(sections):
        if spikey != False or flower != False:
            radius_modif = abs(strength_modif * math.sin((n_modifs/2.0) * j * outer_rads - (outer_rads / 2.0))) + strength_modif
        if spikey == True:
            spikey_modif = radius_modif
        elif flower == True:
            flower_modif = radius_modif
        inner_rads = (step_inner_angle * PI / 180.0)
        inner_x = distance + spikey_modif * inner_radius * math.cos(i * inner_rads - (inner_rads / 2.0))
        inner_y = inner_radius * math.sin(i * inner_rads - (inner_rads / 2.0))


        outer_distance = inner_x * flower_modif
        y = radius_modif * inner_y
        x = outer_distance * math.sin(j * outer_rads - (outer_rads / 2.0))
        z = outer_distance * math.cos(j * outer_rads - (outer_rads / 2.0))

        # points as spheres
        #c.polySphere(sx = 5, sy = 5, r = 0.5, n = 'point{}{}'.format(i, j))
        #c.setAttr('point{}{}.translateX'.format(i, j), x)
        #c.setAttr('point{}{}.translateZ'.format(i, j), z)
        #c.setAttr('point{}{}.translateY'.format(i, j), y)

        # save vertices
        temp = OM.MPoint(x, y, z)
        verts.append(temp)

# joining the points through quads
quadArray = OM.MPointArray()
quadArray.setLength(4)
print(len(verts))

for j in range(tubes):
    exception = 0
    for i in range(sections):
        if i == sections - 1:
            exception = sections

        # counter clock wise faces
        if j == tubes - 1:
            quadArray.set(verts[((i + sections) + (sections)* j) % len(verts)], 0)
            quadArray.set(verts[((i + sections + 1) - exception + (sections)* j) % len(verts)], 1)

        else:
            quadArray.set(verts[(i + sections) + (sections)* j], 0)
            quadArray.set(verts[(i + sections + 1) - exception + (sections)* j], 1)


        quadArray.set(verts[(i + 1) - exception + (sections)* j], 2)
        quadArray.set(verts[(i) + (sections)* j], 3)

        mesh.addPolygon(quadArray, mergeVerts, pointTolerance)
