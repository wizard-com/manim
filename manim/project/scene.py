import numpy as np

from manim import *


class CameraIssue(MovingCameraScene):
    def construct(self):
        square = Square()
        triangle = Triangle()
        square.set_fill(RED, opacity=0.5)
        self.camera.frame.height = 4
        self.camera.frame.aspect_ratio = 1
        self.add(square)
        self.play(self.camera.frame.animate.rotate(PI / 2, axis=[1.0, 3.0, 1.0]))
