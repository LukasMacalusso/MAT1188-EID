from manim import *

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
    FONT_NOTE,
    get_scene_title,
    get_boxed_formula,
)
from src.common.math_defs import (
    func_main,
    DEFAULT_A,
    DEFAULT_B,
    DEFAULT_EXACT_AREA,
)

class Scene5ExampleCalculation(Scene):
    def construct(self):
        header = get_scene_title(
            "Paso 5: Ejemplo Propio y Verificación Numérica",
            "Cálculo exacto con f(x) = 3x² en [1, 2] e invariancia ante la constante C"
        )
        self.play(FadeIn(header, shift=UP * 0.3), run_time=1.2)
        self.wait(3.5)

        axes = Axes(
            x_range=[0, 2.6, 0.5],
            y_range=[0, 14, 2],
            x_length=4.8,
            y_length=4.2,
            axis_config={
                "color": LIGHT_GRAY,
                "stroke_width": 2,
                "include_tip": True,
                "tip_length": 0.2,
            },
        ).to_edge(LEFT, buff=0.5).shift(DOWN * 0.4)

        x_axis_tag = axes.get_x_axis_label(Tex("x", font_size=FONT_BODY), edge=RIGHT, direction=RIGHT)
        y_axis_tag = axes.get_y_axis_label(Tex("y", font_size=FONT_BODY), edge=UP, direction=UP)
        axes_labels = VGroup(x_axis_tag, y_axis_tag)

        curve = axes.plot(
            func_main,
            x_range=[0.0, 2.15],
            color=COLOR_CURVE,
            stroke_width=3.5,
        )
        curve_label = MathTex(r"f(x) = 3x^2", color=COLOR_CURVE, font_size=FONT_MATH - 2)
        curve_label.next_to(axes.c2p(2.0, 12.0), LEFT, buff=0.25).shift(UP * 0.2)

        a_line = axes.get_vertical_line(axes.c2p(DEFAULT_A, func_main(DEFAULT_A)), color=COLOR_ACCENT, stroke_width=2)
        b_line = axes.get_vertical_line(axes.c2p(DEFAULT_B, func_main(DEFAULT_B)), color=COLOR_ACCENT, stroke_width=2)
        a_label = MathTex("a = 1", font_size=FONT_BODY, color=COLOR_ACCENT).next_to(axes.c2p(DEFAULT_A, 0), DOWN, buff=0.25)
        b_label = MathTex("b = 2", font_size=FONT_BODY, color=COLOR_ACCENT).next_to(axes.c2p(DEFAULT_B, 0), DOWN, buff=0.25)

        shaded_area = axes.get_area(
            curve,
            x_range=[DEFAULT_A, DEFAULT_B],
            color=COLOR_AREA,
            opacity=0.65
        )
        area_number = MathTex(r"\text{Área} = 7", font_size=FONT_MATH, color=WHITE).move_to(
            axes.c2p(1.5, 3.5)
        )

        self.play(Create(axes), Write(axes_labels), Create(curve), Write(curve_label), run_time=1.5)
        self.play(Create(a_line), Create(b_line), Write(a_label), Write(b_label), run_time=1.0)
        self.play(FadeIn(shaded_area), Write(area_number), run_time=1.2)
        self.wait(4.5)

        panel_x = 3.0
        calc_title = Text("1. Cálculo Analítico:", font_size=FONT_SUBTITLE, color=COLOR_PRIMARY)
        calc_title.move_to(RIGHT * panel_x + UP * 1.85)

        step_f = MathTex(r"\text{Antiderivada: } F(x) = x^3", font_size=FONT_BODY - 2, color=COLOR_SECONDARY)
        step_f.next_to(calc_title, DOWN, buff=0.25, aligned_edge=LEFT)

        step_eval = MathTex(
            r"\int_1^2 3x^2\,dx = \big[x^3\big]_1^2 = F(2) - F(1)",
            font_size=FONT_BODY - 3
        ).next_to(step_f, DOWN, buff=0.18, aligned_edge=LEFT)

        step_calc = MathTex(
            r"= 2^3 - 1^3 = 8 - 1 = \mathbf{7}",
            font_size=FONT_MATH - 2,
            color=COLOR_MATH
        ).next_to(step_eval, DOWN, buff=0.18, aligned_edge=LEFT)

        boxed_res = get_boxed_formula(step_calc, color=COLOR_BOX, buff=0.18)

        self.play(FadeIn(calc_title), Write(step_f), run_time=1.2)
        self.wait(2.5)
        self.play(Write(step_eval), run_time=1.2)
        self.wait(2.5)
        self.play(FadeIn(boxed_res, shift=UP * 0.15), run_time=1.2)
        self.wait(4.0)

        verif_title = Text("2. Verificación de Invarianza ante C:", font_size=FONT_BODY, color=COLOR_ACCENT)
        verif_title.next_to(boxed_res, DOWN, buff=0.3, aligned_edge=LEFT)

        verif_f2 = MathTex(r"\text{Elegimos: } F_2(x) = x^3 + 5", font_size=FONT_BODY - 3, color=LIGHT_GRAY)
        verif_f2.next_to(verif_title, DOWN, buff=0.15, aligned_edge=LEFT)

        verif_calc = MathTex(
            r"F_2(2) - F_2(1) = (2^3 + 5) - (1^3 + 5)",
            font_size=FONT_BODY - 3
        ).next_to(verif_f2, DOWN, buff=0.15, aligned_edge=LEFT)

        verif_calc2 = MathTex(
            r"= 13 - 6 = \mathbf{7}",
            font_size=FONT_MATH - 3,
            color=COLOR_HIGHLIGHT
        ).next_to(verif_calc, DOWN, buff=0.15, aligned_edge=LEFT)

        self.play(FadeIn(verif_title), Write(verif_f2), run_time=1.0)
        self.wait(2.0)
        self.play(Write(verif_calc), run_time=1.0)
        self.wait(2.0)
        self.play(Write(verif_calc2), run_time=1.2)
        self.wait(4.0)

        closing_box = VGroup(
            Text(
                "¡Coincidencia exacta con el límite de Riemann!",
                font_size=FONT_NOTE,
                color=COLOR_PRIMARY,
                weight=BOLD
            ),
            Text(
                "Paso 1: S₃₂ ≈ 7.14 → 7.00 con límite.",
                font_size=FONT_NOTE - 2,
                color=WHITE
            ),
            Text(
                "Regla de Barrow: valor exacto 7 mediante resta.",
                font_size=FONT_NOTE - 2,
                color=COLOR_SECONDARY,
                weight=BOLD
            ),
        ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        closing_box.next_to(verif_calc2, DOWN, buff=0.22, aligned_edge=LEFT)

        self.play(FadeIn(closing_box, shift=UP * 0.2), run_time=1.5)
        self.wait(8.0)

        self.play(FadeOut(Group(*self.mobjects)), run_time=1.2)

