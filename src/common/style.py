from manim import *

COLOR_BG = "#14161B"
COLOR_TEXT = WHITE
COLOR_SUBTEXT = LIGHT_GRAY
COLOR_BOX = GRAY

COLOR_CURVE = ORANGE
COLOR_AREA = TEAL_C

COLOR_PRIMARY = TEAL_C
COLOR_SECONDARY = ORANGE
COLOR_DIFF_STRIP = YELLOW_C
COLOR_MATH = WHITE
COLOR_HIGHLIGHT = YELLOW_C
COLOR_ACCENT = YELLOW_C
COLOR_AREA_EXAMPLE = TEAL_C

FONT_TITLE = 32
FONT_SUBTITLE = 24
FONT_BODY = 20
FONT_MATH = 26
FONT_NOTE = 16

DEFAULT_AXIS_CONFIG = {
    "color": LIGHT_GRAY,
    "stroke_width": 2,
    "include_tip": True,
    "tip_length": 0.2,
}

def get_scene_title(title_text: str, subtitle_text: str = "") -> VGroup:
    title = Text(title_text, font_size=FONT_TITLE, weight=BOLD, color=COLOR_PRIMARY)
    if not subtitle_text:
        return VGroup(title).to_edge(UP, buff=0.4).to_edge(LEFT, buff=0.6)

    sub = Text(subtitle_text, font_size=FONT_SUBTITLE, color=COLOR_SUBTEXT)
    group = VGroup(title, sub).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
    return group.to_edge(UP, buff=0.4).to_edge(LEFT, buff=0.6)

def get_boxed_formula(formula_mob: VMobject, color: ManimColor = COLOR_BOX, buff: float = 0.2) -> VGroup:
    box = SurroundingRectangle(formula_mob, color=color, buff=buff, stroke_width=2.5)
    return VGroup(box, formula_mob)

