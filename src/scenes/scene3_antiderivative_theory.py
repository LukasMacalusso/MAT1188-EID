from manim import *

from src.common.style import (
    COLOR_PRIMARY,
    COLOR_SECONDARY,
    COLOR_ACCENT,
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

class Scene3AntiderivativeTheory(Scene):
    def construct(self):
        header = get_scene_title(
            "Paso 3: Definición de Antiderivada y Familia de Primitivas",
            "Cualquier antiderivada difiere de la acumulación únicamente por una constante C"
        )
        self.play(FadeIn(header, shift=UP * 0.3), run_time=1.2)
        self.wait(3.5)

        card_title = Text("1. Definición Formal de Antiderivada", font_size=FONT_SUBTITLE, color=COLOR_PRIMARY)
        card_text = Text(
            "Una función F se denomina antiderivada o primitiva de f en un intervalo si:",
            font_size=FONT_BODY,
            color=COLOR_TEXT
        )
        def_formula = MathTex(
            r"F'(x) = f(x)",
            font_size=FONT_MATH + 4,
            color=COLOR_MATH
        )
        boxed_def = get_boxed_formula(def_formula, color=COLOR_SECONDARY)

        def_group = VGroup(card_title, card_text, boxed_def).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        def_group.to_edge(LEFT, buff=1.2).shift(UP * 0.9)

        self.play(Write(card_title), FadeIn(card_text), run_time=1.5)
        self.play(FadeIn(boxed_def, shift=UP * 0.2), run_time=1.2)
        self.wait(4.0)

        conn_title = Text("2. El rol de la Función de Acumulación", font_size=FONT_SUBTITLE, color=COLOR_PRIMARY)
        conn_text = MathTex(
            r"\text{En el Paso 2 demostramos que: } G(x') = \int_a^{x'} f(t)\,dt \implies G'(x') = f(x')",
            font_size=FONT_BODY,
            color=COLOR_ACCENT
        )
        conn_note = Text(
            "Por lo tanto, G(x') es una antiderivada particular (donde G(a) = 0).",
            font_size=FONT_BODY - 2,
            color=LIGHT_GRAY
        )
        conn_group = VGroup(conn_title, conn_text, conn_note).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        conn_group.next_to(def_group, DOWN, buff=0.6, aligned_edge=LEFT)

        self.play(Write(conn_title), FadeIn(conn_text), FadeIn(conn_note), run_time=1.8)
        self.wait(4.5)

        self.play(FadeOut(def_group), FadeOut(conn_group), run_time=1.0)

        fam_title = Text("3. La Familia Infinita de Antiderivadas", font_size=FONT_SUBTITLE + 2, color=COLOR_PRIMARY)
        fam_title.to_edge(UP, buff=1.6).to_edge(LEFT, buff=1.2)

        const_rule = MathTex(
            r"\text{Dado que la derivada de una constante es cero: } \frac{d}{dx}(C) = 0",
            font_size=FONT_BODY,
            color=COLOR_TEXT
        ).next_to(fam_title, DOWN, buff=0.35, aligned_edge=LEFT)

        deriv_sum = MathTex(
            r"\big(G(x') + C\big)' = G'(x') + \frac{d}{dx'}(C) = f(x') + 0 = f(x')",
            font_size=FONT_MATH,
            color=COLOR_SECONDARY
        ).next_to(const_rule, DOWN, buff=0.35, aligned_edge=LEFT)

        self.play(Write(fam_title), FadeIn(const_rule), run_time=1.5)
        self.play(Write(deriv_sum), run_time=1.8)
        self.wait(4.0)

        fam_result = MathTex(
            r"F(x') = G(x') + C \quad \text{para alguna constante } C \in \mathbb{R}",
            font_size=FONT_MATH + 2,
            color=COLOR_MATH
        )
        boxed_fam = get_boxed_formula(fam_result, color=COLOR_BOX)
        boxed_fam.next_to(deriv_sum, DOWN, buff=0.45, aligned_edge=LEFT)

        question_prompt = VGroup(
            Text(
                "Pregunta Clave para la Regla de Barrow:",
                font_size=FONT_SUBTITLE,
                color=COLOR_PRIMARY,
                weight=BOLD
            ),
            Text(
                "Si existen infinitas antiderivadas con diferentes valores de C...",
                font_size=FONT_BODY,
                color=LIGHT_GRAY
            ),
            Text(
                "¿Por qué el cálculo del área no depende de la constante que elijamos?",
                font_size=FONT_BODY,
                color=COLOR_HIGHLIGHT,
                weight=BOLD
            )
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        question_prompt.next_to(boxed_fam, DOWN, buff=0.5, aligned_edge=LEFT)

        self.play(FadeIn(boxed_fam, shift=UP * 0.2), run_time=1.5)
        self.wait(3.5)
        self.play(FadeIn(question_prompt, shift=UP * 0.2), run_time=1.8)
        self.wait(8.0)

        self.play(FadeOut(Group(*self.mobjects)), run_time=1.2)

