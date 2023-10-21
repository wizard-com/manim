import numpy as np

from manim import *


class CameraIssue(MovingCameraScene):
    def construct(self):
        s1 = Square()
        s2 = Square()
        s1.set_fill(RED, opacity=0.5).shift(2 * LEFT)
        s2.set_fill(GREEN, opacity=0.5).shift(2 * RIGHT)
        self.add(s1)
        self.add(s2)
        self.play(self.camera.frame.animate.rotate(PI / 2))


class CameraSolution(MovingCameraScene):
    def construct(self):
        s1 = Square()
        s2 = Square()
        s1.set_fill(RED, opacity=0.5)
        s2.set_fill(GREEN, opacity=0.5)
        group = Group(s1, s2).set_x(0).arrange(buff=1.0)
        self.add(group)
        self.play(group.animate.rotate(PI / 2))
