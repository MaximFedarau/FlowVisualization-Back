import json
import os

from manim import *


class CreateFlow(Scene):
    data = dict()

    def read_data(self, path: str):
        with open(path) as f:
            self.data = json.load(f)
        return self.data

    def construct(self):
        self.read_data(os.environ.get("VISUALIZATION_DATA_PATH", ""))
        self.camera.frame_width = 42.25
        self.camera.frame_height = 22.5
        self.camera.aspect_ratio = 16 / 9
        group = VGroup()
        dots = []
        for coord in self.data["coordinates"]:
            new_dot = Dot((coord[0], coord[1], 0), color=WHITE, radius=0.3)
            dots.append(new_dot)
            group.add(new_dot)

        self.play(Create(group))  # show the circle on screen

        edge_group1 = VGroup()
        for edge in self.data["edges"]:
            start_dot = dots[edge["from_"]]
            end_dot = dots[edge["to"]]
            line = DashedLine(
                start_dot.get_center(),
                end_dot.get_center(),
                stroke_width=3,
                color=ManimColor.from_rgb(tuple(edge["color"])),
            )
            edge_group1.add(line)
        self.play(ChangeSpeed(Create(edge_group1), speedinfo={1: -0.3}))

        edge_group = VGroup()
        for action in self.data["visualization"]:
            edge_group = VGroup()
            for edge in action["way"]:
                start_dot = dots[edge["from_"]]
                end_dot = dots[edge["to"]]
                line = Line(
                    start_dot.get_center(),
                    end_dot.get_center(),
                    stroke_width=5,
                    color=ManimColor.from_rgb(tuple(edge["color"])),
                )
                capacity_text = Text(
                    f"Capacity: {edge['capacity']}",
                    font_size=36,
                ).next_to(line, UP, buff=0.3)
                flow_text = Text(f"Flow: {edge['flow']}", font_size=36).next_to(
                    line,
                    DOWN,
                    buff=0.3,
                )
                edge_group.add(line)
                edge_group.add(capacity_text)
                edge_group.add(flow_text)
            self.play(ChangeSpeed(Create(edge_group), speedinfo={1: -0.3}))
            self.wait(0.5)
            self.remove(edge_group)
