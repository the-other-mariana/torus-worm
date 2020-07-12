#File:      torus-worm.py
#Author:    Mariana Avalos
#Date:      11/07/2020
#Description: Python code that makes an animated torus

import maya.cmds as c
import math as math
import maya.OpenMaya as OM

verts = []
mesh = OM.MFnMesh()
mergeVerts = True
pointTolerance = 0.001

tubes = 5
sections = 5
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

        # save vertices
        temp = OM.MPoint(x, y, z)
        verts.append(temp)

quadArray = OM.MPointArray()
quadArray.setLength(4)
print(len(verts))


for j in range(tubes):
    exception = 0
    print("-----")
    for i in range(sections):
        print("+++++")
        if i == sections - 1:
            exception = sections
        quadArray.set(verts[(i) + (sections)* j], 0)
        print(str((i) + (sections)* j))
        quadArray.set(verts[(i + 1) - exception + (sections)* j], 1)
        print(str((i + 1) - exception + (sections)* j))

        if j == tubes - 1:
            var = 8 + sections
            quadArray.set(verts[((i + sections + 1) - exception + (sections)* j) % len(verts)], 2)
            print(str(((i + sections + 1) - exception + (sections)* j) % len(verts)))
            quadArray.set(verts[((i + sections) + (sections)* j) % len(verts)], 3)
            print(str(((i + sections) + (sections)* j) % len(verts)))
        else:

            quadArray.set(verts[(i + sections + 1) - exception + (sections)* j], 2)
            print(str((i + sections + 1) - exception + (sections)* j))
            quadArray.set(verts[(i + sections) + (sections)* j], 3)
            print(str((i + sections) + (sections)* j))



        mesh.addPolygon(quadArray, mergeVerts, pointTolerance)

'''
for j in range(tubes-1):
    exception = 0
    for i in range(sections):
        if(i == sections -1):
            exception = sections
        quadArray.set(verts[(i + 1) + (sections * j)], 0)
        print(str((i + 1) + (sections * j)))
        quadArray.set(verts[(i + 2 - exception) + (sections * j)], 1)
        print(str((i + 2 - exception) + (sections * j)))
        quadArray.set(verts[(i + (sections + 2) - exception) + (sections * j)], 2)
        print(str((i + (sections + 2) - exception) + (sections * j)))
        quadArray.set(verts[(i + (sections + 1)) + (sections * j)], 3)
        print(str((i + (sections + 1)) + (sections * j)))
        mesh.addPolygon(quadArray, mergeVerts, pointTolerance)
'''
