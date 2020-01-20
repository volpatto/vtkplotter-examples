"""Split a mesh by connectivity and
order the pieces by increasing area.
"""
from vtkplotter import *

em = load(datadir+"embryo.tif", threshold=80)

# return the list of the largest 10 connected meshes:
splitem = splitByConnectivity(em, maxdepth=40)[0:9]

t = Text(__doc__)
show( [(em, t), splitem], N=2, axes=1 )
