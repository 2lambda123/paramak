# This examples creates Gif animation of 50 reactors by creating individual
# images of reactors and stiching them together using Imagemagick into a Gif
# animation. Two animations are made, of of a 3D render and one of a wireframe
# line drawing.

import math
import os

# to run this example you will need all of the following packages installed
import matplotlib.pyplot as plt
import numpy as np
import paramak
import pyrender
import trimesh
from PIL import Image, ImageFont, ImageDraw


def create_reactor_renders(
    render_number,
    inner_blanket_radius,
    blanket_thickness,
    blanket_height,
    lower_blanket_thickness,
    upper_blanket_thickness,
    blanket_vv_gap,
    upper_vv_thickness,
    vv_thickness,
    lower_vv_thickness,
):

    # creates a blank figure for populating with subplots
    plt.figure()

    # creates a reactor from the input arguments
    my_reactor = paramak.FlfSystemCodeReactor(
        rotation_angle=180,
        inner_blanket_radius=inner_blanket_radius,
        blanket_thickness=blanket_thickness,
        blanket_height=blanket_height,
        lower_blanket_thickness=lower_blanket_thickness,
        upper_blanket_thickness=upper_blanket_thickness,
        blanket_vv_gap=blanket_vv_gap,
        upper_vv_thickness=upper_vv_thickness,
        vv_thickness=vv_thickness,
        lower_vv_thickness=lower_vv_thickness,
    )

    # saves the reactor geometry as separate stl files that are later read in
    # for the rendering
    my_reactor.export_stl()

    # assigns colours to each stl file
    stl_files_with_colors = {
        "blanket.stl": (255, 255, 0),
        "vessel.stl": (128, 128, 128),
        "upper_blanket.stl": (255, 255, 0),
        "lower_blanket.stl": (255, 255, 0),
        "lower_vessel.stl": (128, 128, 128),
        "upper_vessel.stl": (128, 128, 128),
    }

    scene = pyrender.Scene()

    # for each stl file and color combination
    for key, value in stl_files_with_colors.items():
        trimesh_obj = trimesh.load(key)
        trimesh_obj.visual.vertex_colors = value
        trimesh_obj.visual

        render_mesh = pyrender.Mesh.from_trimesh(trimesh_obj, smooth=False)
        scene.add(render_mesh)

    camera = pyrender.camera.PerspectiveCamera(yfov=math.radians(90.0))  # aspectRatio=2.0 could be added here

    # sets the position of the camera using a matrix
    cam = 2**-0.5
    camera_pose = np.array([[1, 0, 0, 0], [0, cam, -cam, -600], [0, cam, cam, 600], [0, 0, 0, 1]])

    # adds a camera and a point light source at the same location
    scene.add(camera, pose=camera_pose)
    light = pyrender.PointLight(color=np.ones(3), intensity=300000.0)
    scene.add(light, pose=camera_pose)

    # renders the scene
    my_render = pyrender.OffscreenRenderer(1000, 1000)
    color, _ = my_render.render(scene)

    # adds the render to the plot as a subplot in the correct location
    plt.plot()
    plt.axis("off")
    plt.imshow(color)
    # plt.show()
    plt.savefig("tempfile.png", dpi=400)

    my_image = Image.open("tempfile.png")
    title_text = f"""
    inner_blanket_radius={round(inner_blanket_radius,1)}
    blanket_thickness={round(blanket_thickness,1)}
    blanket_height={round(blanket_height,1)}
    lower_blanket_thickness={round(lower_blanket_thickness,1)}
    upper_blanket_thickness={round(upper_blanket_thickness,1)}
    blanket_vv_gap={round(blanket_vv_gap,1)}
    upper_vv_thickness={round(upper_vv_thickness,1)}
    vv_thickness={round(vv_thickness,1)}
    lower_vv_thickness={round(lower_vv_thickness,1)}
    """
    image_editable = ImageDraw.Draw(my_image)

    # ttf file from https://fonts.google.com/
    title_font = ImageFont.truetype("EncodeSansSemiExpanded-Medium.ttf", 50)
    xy_location = (1000, 1000)
    rgb = (0, 0, 0)
    image_editable.text(xy_location, title_text, rgb, font=title_font)
    my_image.save(f"render_{str(render_number).zfill(3)}.png")


# loops through adding a random reactor render to the figure with each iteration
for i in range(50):
    create_reactor_renders(
        render_number=i,
        inner_blanket_radius=np.random.uniform(low=50, high=90),
        blanket_thickness=np.random.uniform(low=50, high=140),
        blanket_height=np.random.uniform(low=400, high=550),
        lower_blanket_thickness=np.random.uniform(low=20, high=70),
        upper_blanket_thickness=np.random.uniform(low=20, high=70),
        blanket_vv_gap=np.random.uniform(low=10, high=90),
        upper_vv_thickness=np.random.uniform(low=5, high=15),
        vv_thickness=np.random.uniform(low=5, high=15),
        lower_vv_thickness=np.random.uniform(low=5, high=15),
    )

# The convert comand requires imagemagick
# saves the rendered png files as a gif
os.system("convert -delay 40 -loop 0 render_*.png reactors.gif")
