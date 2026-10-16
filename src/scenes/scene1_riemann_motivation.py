from manim import *
import numpy as np

from src.common.style import (
    COLOR_PRIMARY,
    COLOR_SECONDARY,
    COLOR_ACCENT,
    COLOR_CURVE,
    COLOR_AREA,
    COLOR_TEXT,
    COLOR_SUBTEXT,
    COLOR_MATH,
    COLOR_HIGHLIGHT,
    COLOR_BOX,
    FONT_TITLE,
    FONT_SUBTITLE,
    FONT_BODY,
    FONT_MATH,
    get_scene_title,
    get_boxed_formula,
)
from src.common.math_defs import (
    func_main,
    DEFAULT_A,
    DEFAULT_B,
    riemann_sum_right,
)

class Scene1RiemannMotivation(Scene):
    def construct(self):
        header = get_scene_title(
            "Paso 1: Del Área a las Sumas de Riemann",
            "Aproximación geométrica y necesidad de un método exacto"
        )
        self.play(FadeIn(header, shift=UP * 0.3), run_time=1.2)
        self.wait(4.0)

        axes = Axes(
            x_range=[0, 2.6, 0.5],
            y_range=[0, 14, 2],
            x_length=6.0,
            y_length=4.5,
            axis_config={
                "color": LIGHT_GRAY,
                "stroke_width": 2,
                "include_tip": True,
                "tip_length": 0.2,
            },
        ).to_edge(LEFT, buff=0.8).shift(DOWN * 0.4)

        x_label = axes.get_x_axis_label(Tex("x", font_size=FONT_BODY), edge=RIGHT, direction=RIGHT)
        y_label = axes.get_y_axis_label(Tex("y", font_size=FONT_BODY), edge=UP, direction=UP)
        axes_labels = VGroup(x_label, y_label)

        curve = axes.plot(
            func_main,
            x_range=[0.0, 2.15],
            color=COLOR_CURVE,
            stroke_width=3.5,
        )
        curve_label = MathTex(r"f(x) = 3x^2", color=COLOR_CURVE, font_size=FONT_MATH)
        curve_label.next_to(axes.c2p(2.0, 12.0), LEFT, buff=0.25).shift(UP * 0.2)

        self.play(Create(axes), Write(axes_labels), run_time=1.5)
        self.play(Create(curve), Write(curve_label), run_time=1.5)
        self.wait(4.0)

        a_line = axes.get_vertical_line(axes.c2p(DEFAULT_A, func_main(DEFAULT_A)), color=COLOR_ACCENT, stroke_width=2)
        b_line = axes.get_vertical_line(axes.c2p(DEFAULT_B, func_main(DEFAULT_B)), color=COLOR_ACCENT, stroke_width=2)
        a_text = MathTex("a = 1", font_size=FONT_BODY, color=COLOR_ACCENT).next_to(axes.c2p(DEFAULT_A, 0), DOWN, buff=0.25)
        b_text = MathTex("b = 2", font_size=FONT_BODY, color=COLOR_ACCENT).next_to(axes.c2p(DEFAULT_B, 0), DOWN, buff=0.25)
        interval_group = VGroup(a_line, b_line, a_text, b_text)

        self.play(Create(interval_group), run_time=1.2)
        self.wait(4.5)

        panel_x = 3.6
        riemann_title = Text("Suma de Riemann", font_size=FONT_SUBTITLE, color=COLOR_PRIMARY)
        riemann_title.move_to(RIGHT * panel_x + UP * 1.8)

        dx_formula = MathTex(r"\Delta x = \frac{b - a}{n}", font_size=FONT_BODY)
        dx_formula.next_to(riemann_title, DOWN, buff=0.35)

        sum_formula = MathTex(
            r"S_n = \sum_{i=1}^n f(x_i^*) \Delta x",
            font_size=FONT_MATH,
            color=COLOR_MATH
        )
        sum_formula.next_to(dx_formula, DOWN, buff=0.35)

        info_box = VGroup(riemann_title, dx_formula, sum_formula)
        self.play(FadeIn(info_box, shift=LEFT * 0.4), run_time=1.5)
        self.wait(5.5)

        n_label = MathTex(r"n = 4 \text{ rectángulos}", font_size=FONT_BODY, color=COLOR_ACCENT)
        n_label.next_to(sum_formula, DOWN, buff=0.6)

        rects_n4 = axes.get_riemann_rectangles(
            curve,
            x_range=[DEFAULT_A, DEFAULT_B],
            dx=(DEFAULT_B - DEFAULT_A) / 4,
            input_sample_type="right",
            stroke_width=1.5,
            stroke_color=WHITE,
            fill_opacity=0.6,
            color=(COLOR_AREA, COLOR_PRIMARY),
        )

        val_n4 = riemann_sum_right(func_main, DEFAULT_A, DEFAULT_B, 4)
        val_label = MathTex(rf"S_{{4}} \approx {val_n4:.2f}", font_size=FONT_BODY, color=WHITE)
        val_label.next_to(n_label, DOWN, buff=0.25)

        self.play(Create(rects_n4), FadeIn(n_label), FadeIn(val_label), run_time=1.8)
        self.wait(5.5)

        rects_n8 = axes.get_riemann_rectangles(
            curve,
            x_range=[DEFAULT_A, DEFAULT_B],
            dx=(DEFAULT_B - DEFAULT_A) / 8,
            input_sample_type="right",
            stroke_width=1.0,
            stroke_color=WHITE,
            fill_opacity=0.6,
            color=(COLOR_AREA, COLOR_PRIMARY),
        )
        n8_label = MathTex(r"n = 8 \text{ rectángulos}", font_size=FONT_BODY, color=COLOR_ACCENT).move_to(n_label)
        val_n8 = riemann_sum_right(func_main, DEFAULT_A, DEFAULT_B, 8)
        val8_label = MathTex(rf"S_{{8}} \approx {val_n8:.2f}", font_size=FONT_BODY, color=WHITE).move_to(val_label)

        self.play(
            Transform(rects_n4, rects_n8),
            Transform(n_label, n8_label),
            Transform(val_label, val8_label),
            run_time=1.8
        )
        self.wait(5.5)

        rects_n32 = axes.get_riemann_rectangles(
            curve,
            x_range=[DEFAULT_A, DEFAULT_B],
            dx=(DEFAULT_B - DEFAULT_A) / 32,
            input_sample_type="right",
            stroke_width=0.4,
            stroke_color=WHITE,
            fill_opacity=0.65,
            color=(COLOR_AREA, COLOR_PRIMARY),
        )
        n32_label = MathTex(r"n = 32 \text{ rectángulos}", font_size=FONT_BODY, color=COLOR_ACCENT).move_to(n_label)
        val_n32 = riemann_sum_right(func_main, DEFAULT_A, DEFAULT_B, 32)
        val32_label = MathTex(rf"S_{{32}} \approx {val_n32:.2f} \to 7.00", font_size=FONT_BODY, color=WHITE).move_to(val_label)

        self.play(
            Transform(rects_n4, rects_n32),
            Transform(n_label, n32_label),
            Transform(val_label, val32_label),
            run_time=1.8
        )
        self.wait(6.0)

        limit_formula = MathTex(
            r"\int_a^b f(x)\,dx = \lim_{n \to \infty} \sum_{i=1}^n f(x_i^*)\,\Delta x",
            font_size=FONT_MATH,
            color=COLOR_MATH
        )
        boxed_limit = get_boxed_formula(limit_formula, color=COLOR_BOX)
        boxed_limit.next_to(val_label, DOWN, buff=0.55)

        limit_note = Text(
            "Cálculo algebraico complejo e impracticable en general",
            font_size=15,
            color=COLOR_HIGHLIGHT
        ).next_to(boxed_limit, DOWN, buff=0.3)

        self.play(FadeIn(boxed_limit, shift=UP * 0.2), FadeIn(limit_note), run_time=1.5)
        self.wait(7.0)

        self.play(FadeOut(Group(*self.mobjects)), run_time=1.2)

