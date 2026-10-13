# MAT1188 – Cálculo Intermedio: Proyecto Manim (EID)

## Grupo 9 – Eje 9: Teorema Fundamental del Cálculo (Parte II) y Regla de Barrow
**Pregunta Central:** *¿Por qué una integral definida puede calcularse como $F(b) - F(a)$?*

---

## Contenido del Repositorio

- [Documentacion_matematica.md]: Documento principal con el desarrollo matemático paso a paso (desde las sumas de Riemann hasta la deducción de Barrow), el ejemplo con $f(x)=3x^2$ y las especificaciones técnicas de cada escena para Manim.
- `pyproject.toml`: Configuracion, metadata y dependencias del proyecto.
- `main.py`: Punto de entrada principal para orquestar la renderización de las escenas del proyecto.
- `src/common/`: Estructura para estilos y definiciones matemáticas compartidas.
- `src/scenes/`: Directorio modular donde residen los scripts de animación en Python.

---

## Requisitos Previos 

- **uv** Requerido para ejecutar comodamente el proyecto modularizado, dentro de su entorno virtual adecuado.
- **Python:** 3.10 o superior.
- **FFmpeg:** Requerido por Manim para codificar y renderizar los archivos de video MP4.
- **LaTeX / MiKTeX (Opcional):** Si se desea renderizado tipográfico nativo de fórmulas matemáticas complejas.

---

## Estructura de Escenas y Ejecución

Las animaciones se organizan de manera modular siguiendo los 5 pasos del proyecto:

1. `scene1_riemann_motivation.py` (`Scene1RiemannMotivation`): Motivación mostrando sumas de Riemann ($n=4 \to n=32$) y la necesidad de un método exacto.
2. `scene2_accumulation_tfc1.py` (`Scene2AccumulationTFC1`): Función de acumulación $G(x')$, franja diferencial $\Delta x$ y deducción directa de $\frac{dG}{dx'} = f(x')$.
3. `scene3_antiderivative_theory.py` (`Scene3AntiderivativeTheory`): Definición de antiderivada y familia infinita de primitivas ($F(x') = G(x') + C$).
4. `scene4_barrow_deduction.py` (`Scene4BarrowDeduction`): Deducción analítica de la Regla de Barrow evaluando en $a$ y $b$ con cancelación de $C$.
5. `scene5_example_calculation.py` (`Scene5ExampleCalculation`): Ejemplo práctico con $f(x) = 3x^2$ en $[1, 2]$ y área $= 7$.

### Comandos de Renderizado con `uv`

`uv run` ejecuta los comandos automáticamente dentro del entorno virtual del proyecto sin necesidad de activarlo manualmente:


- **Ejecución vía script principal:**
  ```bash
  uv run python main.py
  ```

- **Previsualización rápida en baja resolución (480p, 15fps):**
  ```bash
  uv run manim -pql src/scenes/scene1_riemann_motivation.py Scene1RiemannMotivation
  ```

- **Renderizado en calidad media (720p, 30fps):**
  ```bash
  uv run manim -pqm src/scenes/scene2_accumulation_tfc1.py Scene2AccumulationTFC1
  ```

- **Renderizado final en alta calidad (1080p, 60fps):**
  ```bash
  uv run manim -pqh src/scenes/scene5_example_calculation.py Scene5ExampleCalculation
  ```




---

## Fuentes y Bibliografía

1. **Documentación Oficial de Manim Community:** [https://docs.manim.community/](https://docs.manim.community/)
2. **Apunte de Cátedra MAT1188:** *Introducción a la integral – Apunte base común*, Facultad de Ingeniería.
3. BlueDot. (2023, 23 de enero). Este TEOREMA lo CAMBIO TODO 🚀| ¿QUÉ es LA INTEGRAL? ▶ El FAMOSO NEXO entre DERIVADAS e INTEGRALES ⌚ [Video]. YouTube. https://www.youtube.com/watch?v=y6YQSUDTzqE
4. 3Blue1Brown. (2017, 5 de mayo). Integration and the fundamental theorem of calculus | Chapter 8, Essence of calculus [Video]. YouTube. https://www.youtube.com/watch?v=rfG8ce4nNh0


---

## Declaración de Uso de Inteligencia Artificial

- **Herramienta:** Antigravity (modelo Gemini 3.8 Flash).
- **Finalidad:** Redacción de documentación (citación en APA, formulas en LaTex), estructuración inicial de parametros guía para implementar las animaciones en manim.
- **Verificación:** Todos los pasos algebraicos, fórmulas de derivación/integración y resultados numéricos fueron comprobados a mano por los integrantes del equipo.
