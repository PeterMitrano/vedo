"""Add a square button with N possible internal states
to a rendering window that calls an external function"""
from vedo import *

vp = Plotter()

mesh = vp.load(datadir+"magnolia.vtk").c("v").flat()

# add a button to the current renderer (e.i. nr1)
def buttonfunc():
    mesh.alpha(1 - mesh.alpha())  # toggle mesh transparency
    bu.switch()                 # change to next status
    printc(bu.status(), box="_", dim=True)

bu = vp.addButton(
    buttonfunc,
    pos=(0.7, 0.05),  # x,y fraction from bottom left corner
    states=["click to hide", "click to show"],
    c=["w", "w"],
    bc=["dg", "dv"],  # colors of states
    font="courier",   # arial, courier, times
    size=25,
    bold=True,
    italic=False,
)

vp.show(mesh, __doc__, axes=11)
