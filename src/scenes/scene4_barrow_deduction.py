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
)

class Scene4BarrowDeduction(Scene):
    def construct(self):
        header = get_scene_title(
            "Paso 4: Deducción de la Regla de Barrow (TFC II)",
            "¿Por qué la integral se calcula como F(b) - F(a)? Cancelación de la constante C"
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

        a_line = axes.get_vertical_line(axes.c2p(DEFAULT_A, func_main(DEFAULT_A)), color=COLOR_ACCENT, stroke_width=2)
        b_line = axes.get_vertical_line(axes.c2p(DEFAULT_B, func_main(DEFAULT_B)), color=COLOR_ACCENT, stroke_width=2)
        a_label = MathTex("a", font_size=FONT_BODY, color=COLOR_ACCENT).next_to(axes.c2p(DEFAULT_A, 0), DOWN, buff=0.25)
        b_label = MathTex("b", font_size=FONT_BODY, color=COLOR_ACCENT).next_to(axes.c2p(DEFAULT_B, 0), DOWN, buff=0.25)

        total_area = axes.get_area(
            curve,
            x_range=[DEFAULT_A, DEFAULT_B],
            color=COLOR_AREA,
            opacity=0.6
        )
        integral_tag = MathTex(r"\int_a^b f(x)\,dx", font_size=FONT_MATH - 2, color=WHITE).move_to(
            axes.c2p(1.5, 3.5)
        )

        self.play(Create(axes), Write(axes_labels), Create(curve), run_time=1.5)
        self.play(Create(a_line), Create(b_line), Write(a_label), Write(b_label), run_time=1.0)
        self.play(FadeIn(total_area), Write(integral_tag), run_time=1.2)
        self.wait(4.5)

        panel_x = 3.0
        deduct_title = Text("Deducción Analítica:", font_size=FONT_SUBTITLE, color=COLOR_PRIMARY)
        deduct_title.move_to(RIGHT * panel_x + UP * 1.85)

        l1 = MathTex(r"\text{1. } F(x') = G(x') + C", font_size=FONT_BODY - 2)
        l1.next_to(deduct_title, DOWN, buff=0.25, aligned_edge=LEFT)

        l2 = MathTex(r"\text{2. } F(a) = G(a) + C = 0 + C = C", font_size=FONT_BODY - 2)
        l2.next_to(l1, DOWN, buff=0.18, aligned_edge=LEFT)

        l3 = MathTex(r"\text{3. } F(b) = G(b) + C = \int_a^b f(t)\,dt + C", font_size=FONT_BODY - 2)
        l3.next_to(l2, DOWN, buff=0.18, aligned_edge=LEFT)

        self.play(FadeIn(deduct_title), Write(l1), run_time=1.2)
        self.wait(2.5)
        self.play(Write(l2), run_time=1.2)
        self.wait(2.5)
        self.play(Write(l3), run_time=1.2)
        self.wait(3.0)

        l4_title = Text("4. Resta de ambos extremos:", font_size=FONT_BODY - 3, color=COLOR_ACCENT)
        l4_title.next_to(l3, DOWN, buff=0.22, aligned_edge=LEFT)

        l4 = MathTex(
            r"F(b) - F(a) = \big(G(b) + C\big) - \big(G(a) + C\big)",
            font_size=FONT_BODY - 3
        ).next_to(l4_title, DOWN, buff=0.15, aligned_edge=LEFT)

        l5 = MathTex(
            r"= G(b) - G(a) + (C - C)",
            font_size=FONT_BODY - 3,
            color=COLOR_HIGHLIGHT
        ).next_to(l4, DOWN, buff=0.15, aligned_edge=LEFT)

        cancel_text = Text("(C se anula)", font_size=FONT_NOTE - 2, color=COLOR_HIGHLIGHT)
        cancel_text.next_to(l5, RIGHT, buff=0.15)

        self.play(FadeIn(l4_title), Write(l4), run_time=1.2)
        self.wait(2.5)
        self.play(Write(l5), FadeIn(cancel_text), run_time=1.5)
        self.wait(4.0)

        barrow_formula = MathTex(
            r"\int_a^b f(x)\,dx = F(b) - F(a)",
            font_size=FONT_MATH,
            color=COLOR_MATH
        )
        boxed_barrow = get_boxed_formula(barrow_formula, color=COLOR_BOX, buff=0.2)
        boxed_barrow.next_to(l5, DOWN, buff=0.35, aligned_edge=LEFT)

        answer_box = VGroup(
            Text(
                "Respuesta a la Pregunta Central:",
                font_size=FONT_NOTE,
                color=COLOR_HIGHLIGHT,
                weight=BOLD
            ),
            Text(
                "No importa la constante elegida: C - C = 0 siempre.",
                font_size=FONT_NOTE - 2,
                color=WHITE
            ),
            Text(
                "F(b) - F(a) entrega exactamente la acumulación neta.",
                font_size=FONT_NOTE - 2,
                color=COLOR_SECONDARY,
                weight=BOLD
            ),
        ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        answer_box.next_to(boxed_barrow, DOWN, buff=0.2, aligned_edge=LEFT)

        self.play(FadeIn(boxed_barrow, shift=UP * 0.2), run_time=1.5)
        self.wait(3.5)
        self.play(FadeIn(answer_box, shift=UP * 0.2), run_time=1.5)
        self.wait(8.0)

        self.play(FadeOut(Group(*self.mobjects)), run_time=1.2)

