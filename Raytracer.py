from gl import Raytracer, V3
from texture import *
from figures import *
from lights import *


width = 1024
height = 1024

centrox = 0
centroy = -1
centroz = 0

# Materiales

brick = Material(diffuse=(0.8, 0.3, 0.3), spec=16)
stone = Material(diffuse=(0.4, 0.4, 0.4), spec=8)
grass = Material(diffuse=(0.3, 1.0, 0.3), spec=64)


marble = Material(spec=64, texture=Texture("marble.bmp"), matType=REFLECTIVE)

mirror = Material(diffuse=(0.9, 0.9, 0.9), spec=64, matType=REFLECTIVE)
glass = Material(diffuse=(0.9, 0.9, 0.9), spec=64,
                 ior=1.5, matType=TRANSPARENT)

rtx = Raytracer(width, height)

rtx.envMap = Texture("Galaxia.bmp")

rtx.lights.append(AmbientLight(intensity=0.1))
#rtx.lights.append( DirectionalLight(direction = (0,0,-1), intensity = 0.5 ))
rtx.lights.append(PointLight(point=(-1, -1, 0)))


# rtx.scene.append( Plane(position = (0,-10,0), normal = (0,1,0), material = brick ))
# rtx.scene.append( Plane(position = (0,10,0), normal = (0,-1,0), material = brick ))
# rtx.scene.append( Plane(position = (-10,0,0), normal = (1,0,0), material = stone ))
# rtx.scene.append( Plane(position = (10,0,0), normal = (-1,0,0), material = stone ))
# rtx.scene.append( Plane(position = (0,0,-40), normal = (0,0,1), material = stone ))

# rtx.scene.append( Disk(position = (0,-3,-7), radius = 2, normal = (0,1,0), material = mirror ))

# rtx.scene.append( AABB(position = (-2,1,-10), size = (2,2,2), material = glass))
# rtx.scene.append( AABB(position = (2,1,-10), size = (2,2,2), material = marble))

# rtx.scene.append(Cilinder(position=(centrox, 3+centroy, -10),
#                  radio=2, height=2, material=brick))

rtx.scene.append(Sphere(V3(0, -0.5, -5), 1, glass))
rtx.scene.append(Torus(position=(0, -0.5, -5), radius=2,
                 normal=(0, 1, 0), material=stone))

rtx.glRender()

rtx.glFinish("output.bmp")
