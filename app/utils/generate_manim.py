from manim import PINK, Circle, Create, Scene


class CreateCircle(Scene):
    """Generate Manim flow visualizaiton."""

    def construct(self) -> None:
        """Construct scene."""
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen
