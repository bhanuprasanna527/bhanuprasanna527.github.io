from manim import *

class DS(Scene):
    def construct(self):
        head = Tex("90 Days DSA Challenge", font_size=120, color=BLUE)
        under = Tex("Day 3", font_size=80, color=GRAY)

        self.play(Write(head), head.animate.shift(UP*1), run_time = 3)
        self.play(Write(under), under.animate.shift(DOWN*1), run_time=3)
        self.wait(3)

class t(Scene):
    def construct(self):
        cpp = Tex("NeetCode", font_size=300, color=BLUE)

        self.play(Write(cpp), run_time=2)
        self.wait(3)

class DC(Scene):
    def construct(self):
        head = Tex("90 Days DSA Challenge", font_size=120, color=BLUE)
        under = Tex("Day 10", font_size=80, color=GRAY)
        com = Tex("Completed", font_size=80, color=ORANGE)

        self.play(Write(head), head.animate.shift(UP*1), run_time = 3)
        self.play(Write(under), under.animate.shift(DOWN*1), run_time=3)
        self.play(Write(com), under.animate.shift(DOWN*1), run_time=3)
        self.wait(3)