from manim import *
import numpy as np

from src.common.style import (
    COLOR_PRIMARY,
    COLOR_SECONDARY,
    COLOR_ACCENT,
    COLOR_CURVE,
    COLOR_AREA,
    COLOR_DIFF_STRIP,
    COLOR_TEXT,
    COLOR_SUBTEXT,
    COLOR_MATH,
    COLOR_HIGHLIGHT,
    COLOR_BOX,
    FONT_TITLE,
    FONT_SUBTITLE,
    FONT_BODY,
    FONT_MATH,
    FONT_NOTE,
    get_scene_title,
    get_boxed_formula,
)
from src.common.math_defs import (
    func_main,
    DEFAULT_A,
    DEFAULT_B,
)

class Scene2AccumulationTFC1(Scene):
    def construct(self):
        header = get_scene_title(
            "Paso 2: Función de Acumulación y Derivación",
            "La tasa a la que se acumula área es la altura de la curva: G'(x') = f(x')"
        )
        self.play(FadeIn(header, shift=UP * 0.3), run_time=1.2)
        self.wait(3.5)

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

        t_label = axes.get_x_axis_label(Tex("t", font_size=FONT_BODY), edge=RIGHT, direction=RIGHT)
        y_label = axes.get_y_axis_label(Tex("y", font_size=FONT_BODY), edge=UP, direction=UP)
        axes_labels = VGroup(t_label, y_label)

        curve = axes.plot(
            func_main,
            x_range=[0.0, 2.15],
            color=COLOR_CURVE,
            stroke_width=3.5,
        )
        curve_label = MathTex(r"f(t) = 3t^2", color=COLOR_CURVE, font_size=FONT_MATH)
        curve_label.next_to(axes.c2p(2.0, 12.0), LEFT, buff=0.25).shift(UP * 0.2)

        self.play(Create(axes), Write(axes_labels), run_time=1.5)
        self.play(Create(curve), Write(curve_label), run_time=1.5)
        self.wait(3.5)

        x_val = 1.6
        dx_val = 0.25

        a_line = axes.get_vertical_line(axes.c2p(DEFAULT_A, func_main(DEFAULT_A)), color=COLOR_ACCENT, stroke_width=2)
        a_label = MathTex("a = 1", font_size=FONT_BODY, color=COLOR_ACCENT).next_to(axes.c2p(DEFAULT_A, 0), DOWN, buff=0.25)

        x_line = axes.get_vertical_line(axes.c2p(x_val, func_main(x_val)), color=COLOR_SECONDARY, stroke_width=2.5)
        x_label = MathTex("x'", font_size=FONT_BODY, color=COLOR_SECONDARY).next_to(axes.c2p(x_val, 0), DOWN, buff=0.25)

        accum_area = axes.get_area(
            curve,
            x_range=[DEFAULT_A, x_val],
            color=COLOR_AREA,
            opacity=0.55
        )
        g_area_tag = MathTex(r"G(x')", font_size=FONT_MATH, color=WHITE).move_to(
            axes.c2p((DEFAULT_A + x_val) / 2, 2.0)
        )

        self.play(Create(a_line), Write(a_label), run_time=1.0)
        self.play(Create(x_line), Write(x_label), run_time=1.0)
        self.play(FadeIn(accum_area), Write(g_area_tag), run_time=1.5)
        self.wait(4.0)

        panel_x = 3.6
        g_def_title = Text("Función de Acumulación", font_size=FONT_SUBTITLE, color=COLOR_PRIMARY)
        g_def_title.move_to(RIGHT * panel_x + UP * 1.8)

        g_def_formula = MathTex(
            r"G(x') = \int_a^{x'} f(t)\,dt",
            font_size=FONT_MATH,
            color=COLOR_SECONDARY
        ).next_to(g_def_title, DOWN, buff=0.35)

        g_prop = MathTex(
            r"\text{Condición inicial: } G(a) = \int_a^a f(t)\,dt = 0",
            font_size=FONT_BODY - 2,
            color=LIGHT_GRAY
        ).next_to(g_def_formula, DOWN, buff=0.3)

        self.play(FadeIn(g_def_title), Write(g_def_formula), FadeIn(g_prop), run_time=1.8)
        self.wait(5.0)

        x_plus_dx = x_val + dx_val
        diff_strip = axes.get_riemann_rectangles(
            curve,
            x_range=[x_val, x_plus_dx],
            dx=dx_val,
            input_sample_type="left",
            stroke_width=2.0,
            stroke_color=YELLOW_A,
            fill_opacity=0.75,
            color=COLOR_DIFF_STRIP,
        )

        dx_bracket = BraceBetweenPoints(
            axes.c2p(x_val, 0),
            axes.c2p(x_plus_dx, 0),
            direction=DOWN,
            buff=0.1
        )
        dx_brace_text = MathTex(r"\Delta x", font_size=FONT_NOTE, color=COLOR_ACCENT).next_to(dx_bracket, DOWN, buff=0.1)

        delta_g_label = MathTex(r"\Delta G", font_size=FONT_BODY, color=YELLOW_A).move_to(
            axes.c2p(x_val + dx_val / 2, func_main(x_val) / 2)
        )

        height_line = DashedLine(
            axes.c2p(x_val, 0),
            axes.c2p(x_val, func_main(x_val)),
            color=YELLOW_A,
            stroke_width=2
        )
        height_label = MathTex(r"f(x')", font_size=FONT_NOTE, color=YELLOW_A).next_to(height_line, LEFT, buff=0.15)

        self.play(
            Create(diff_strip),
            Create(dx_bracket),
            Write(dx_brace_text),
            FadeIn(delta_g_label),
            run_time=1.5
        )
        self.play(Create(height_line), Write(height_label), run_time=1.0)
        self.wait(4.5)

        diff_title = Text("Razón de Cambio del Área:", font_size=FONT_SUBTITLE - 2, color=COLOR_ACCENT)
        diff_title.next_to(g_prop, DOWN, buff=0.45)

        step1 = MathTex(r"\Delta G \approx f(x') \cdot \Delta x", font_size=FONT_BODY)
        step1.next_to(diff_title, DOWN, buff=0.25)

        step2 = MathTex(r"\frac{\Delta G}{\Delta x} \approx f(x')", font_size=FONT_BODY)
        step2.next_to(step1, DOWN, buff=0.25)

        step3 = MathTex(
            r"\frac{dG}{dx'} = \lim_{\Delta x \to 0} \frac{\Delta G}{\Delta x} = f(x')",
            font_size=FONT_MATH,
            color=COLOR_MATH
        )
        boxed_tfc1 = get_boxed_formula(step3, color=COLOR_BOX)
        boxed_tfc1.next_to(step2, DOWN, buff=0.35)

        conclusion_note = Text(
            "Conclusión: G(x') es una antiderivada de f(x')",
            font_size=15,
            color=COLOR_HIGHLIGHT,
            weight=BOLD
        ).next_to(boxed_tfc1, DOWN, buff=0.25)

        self.play(FadeIn(diff_title), Write(step1), run_time=1.2)
        self.wait(2.5)
        self.play(Write(step2), run_time=1.2)
        self.wait(2.5)
        self.play(FadeIn(boxed_tfc1, shift=UP * 0.2), FadeIn(conclusion_note), run_time=1.8)
        self.wait(7.5)

        self.play(FadeOut(Group(*self.mobjects)), run_time=1.2)

