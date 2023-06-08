# https://github.com/marrlab/SHAPR_torch/blob/master/shapr/scripts/tif_to_x3d.py
# in this script the volumina isn't exported as x3d file because trying it generated error for some reasons
from vedo import Plotter
from vedo import Volume
from shapr.utils import import_image

image_data = import_image("Results/cell_frame004185_x0513_y0217_red.tif").squeeze()

def to_x3d(image_data):
    plt = Plotter(size=(600, 600), bg='white', offscreen=False, interactive=True)
    volume = Volume(image_data).isosurface()

    # Add some nice colours based on the y coordinate. This is just for
    # visualisation purposes.
    coords = volume.points()
    volume.cmap('Reds', coords[:, 1])

    plt.show(volume, axes=0, viewup= "z", interactive = True)

   

to_x3d(image_data) #hi
