from manim import *


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(Create(circle))
        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))


class CameraIssue(MovingCameraScene):
    def construct(self):
        self.add(Square())
        # To do - Fix the camera not rotating
        self.play(self.camera.frame.animate.rotate(PI / 2))
