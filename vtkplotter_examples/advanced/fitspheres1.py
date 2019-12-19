"""
In this example we fit spheres to a region of a surface defined by
N points that are closest to a given point of the surface.
For some of these point we show the fitting sphere.
Red lines join the center of the sphere to the surface point.
Blue points are the N points used for fitting.
Fitted radius can be accessed from actor.info['radius'].
"""
from __future__ import division, print_function
from vtkplotter import *

vp = Plotter(verbose=0, axes=0, bg='white')

# load mesh and increase by a lot (N=2) the nr of surface vertices
s = vp.load(datadir+"cow.vtk").alpha(0.3).subdivide(N=2)

for i, p in enumerate(s.getPoints()):
    if i % 1000:
        continue  # skip most points
    pts = s.closestPoint(p, N=16)  # find the N closest points to p
    sph = fitSphere(pts).alpha(0.05)  # find the fitting sphere
    if sph is None:
        continue  # may fail if all points sit on a plane
    vp += sph
    vp += Points(pts)
    vp += Line(sph.info["center"], p, lw=2)

vp += Text(__doc__)
vp.show(viewup="z")