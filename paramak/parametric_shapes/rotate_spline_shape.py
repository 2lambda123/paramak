
import cadquery as cq

from paramak import RotateMixedShape


class RotateSplineShape(RotateMixedShape):
    """Rotates a 3d CadQuery solid from points connected with splines.

    Args:
        points (list): list of (float, float) containing each point
            coordinates.
        rotation_angle (float, optional): The rotation_angle to use when
            revolving the solid (degrees). Defaults to 360.0.
        stp_filename (str, optional): Defaults to "RotateSplineShape.stp".
        stl_filename (str, optional): Defaults to "RotateSplineShape.stl".
    """

    def __init__(
        self,
        points,
        rotation_angle=360,
        stp_filename="RotateSplineShape.stp",
        stl_filename="RotateSplineShape.stl",
        **kwargs
    ):

        super().__init__(
            points=[(*p, "spline") for p in points],
            rotation_angle=rotation_angle,
            stp_filename=stp_filename,
            stl_filename=stl_filename,
            **kwargs
        )
