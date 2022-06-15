import sys
import napari
import numpy as np

from pathlib import Path
from skimage.measure import regionprops
from brainglobe_napari_io.cellfinder.reader_dir import reader_function

image_path = Path(sys.argv[1])
cellfinder_output = Path(sys.argv[2])

region = sys.argv[3]

registration_data = reader_function(cellfinder_output)[0]
registered_atlas_stack = registration_data[0]
scale = registration_data[1]["scale"]
atlas = registration_data[1]["metadata"]["atlas_class"]

descendants = atlas.get_structure_descendants(region)

mask_stack = np.zeros_like(registered_atlas_stack)
bounding_box_stack = np.zeros_like(registered_atlas_stack)

for descendant in descendants:
    descendant_id = atlas.structures[descendant]["id"]
    mask_stack[registered_atlas_stack == descendant_id] = 1

bounds = regionprops(mask_stack)[0]["bbox"]
bounding_box_stack[
    bounds[0] : bounds[3], bounds[1] : bounds[4], bounds[2] : bounds[5]
] = 1
viewer = napari.Viewer()
viewer.open(image_path)

del registered_atlas_stack
del registration_data
viewer.add_image(
    mask_stack,
    scale=scale,
    blending="additive",
    colormap="gray_r",
    name=f"Region: {region}",
)
viewer.add_image(
    bounding_box_stack,
    scale=scale,
    blending="additive",
    colormap="gray_r",
    name=f"Region: {region} (bounding box)",
)

napari.run()
