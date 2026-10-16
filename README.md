# MAT1188 – Cálculo Intermedio: Proyecto Manim (EID)

**Grupo 9 – Eje 9:** Teorema Fundamental del Cálculo (Parte II) y Regla de Barrow  
**Pregunta Central:** *¿Por qué una integral definida puede calcularse como $F(b) - F(a)$?*

## Estructura del Proyecto

- `Documentacion_matematica.md`: Desarrollo matemático, deducción de la Regla de Barrow a partir de la función de acumulación $G(x')$, justificación de la cancelación de la constante $C$ y guion de las escenas.
- `pyproject.toml`: Configuración del proyecto y dependencias gestionadas con `uv`.
- `main.py`: Script de línea de comandos para renderizar escenas individuales, procesar todas las escenas en lote y concatenar el video final con `ffmpeg`.
- `src/common/`:
  - `style.py`: Paleta de colores, tamaños de fuente y funciones auxiliares de formato.
  - `math_defs.py`: Funciones matemáticas ($f(x)=3x^2$, $F(x)=x^3$, función de acumulación $G(x')$ y sumas de Riemann).
- `src/scenes/`: Implementación de las 5 escenas en Manim Community:
  1. `scene1_riemann_motivation.py`: Sumas de Riemann y refinamiento de la partición ($n=4, 8, 32$).
  2. `scene2_accumulation_tfc1.py`: Función de acumulación $G(x')$, diferencial de área $\Delta x$ y relación $\frac{dG}{dx'} = f(x')$.
  3. `scene3_antiderivative_theory.py`: Definición de antiderivada y familia de primitivas $F(x') = G(x') + C$.
  4. `scene4_barrow_deduction.py`: Deducción de la Regla de Barrow evaluando en $a$ y $b$, y cancelación de la constante $C$.
  5. `scene5_example_calculation.py`: Ejemplo práctico con $f(x) = 3x^2$ en $[1, 2]$ y verificación numérica.

## Requisitos

- **Python:** 3.10 o superior
- **uv:** Gestor de paquetes y entornos virtuales de Python
- **Manim Community:** 0.18.0 o superior
- **FFmpeg:** Para la codificación y unión de los archivos de video
- **LaTeX:** Distribución con soporte para `amsmath`, `mathtools` y `dvisvgm`

## Instalación

1. Instalar dependencias del sistema (`ffmpeg` y `latex`):

   En Debian / Ubuntu:
   ```bash
   sudo apt update
   sudo apt install ffmpeg texlive texlive-latex-extra texlive-fonts-extra texlive-science dvisvgm
   ```

   En Arch Linux:
   ```bash
   sudo pacman -S ffmpeg texlive-basic texlive-latexextra texlive-fontsrecommended
   ```

2. Sincronizar el entorno virtual e instalar paquetes de Python:
   ```bash
   uv sync
   ```

## Uso

El archivo `main.py` centraliza la ejecución de Manim:

```bash
# Renderizar una escena específica (calidad media 720p30 por defecto)
uv run python main.py --scene 1

# Cambiar calidad de renderizado: low (480p15), med (720p30), high (1080p60)
uv run python main.py --scene 2 -q low
uv run python main.py --scene 5 -q high

# Renderizar las 5 escenas en orden
uv run python main.py --all -q med

# Unir las escenas ya renderizadas en un único archivo MP4
uv run python main.py --merge -q med
```

El video compilado se guarda en la raíz del proyecto bajo el nombre `MAT1188_Grupo9_EID_Completo_<calidad>.mp4`.

## Referencias

1. **Documentación Oficial de Manim Community:** [https://docs.manim.community/](https://docs.manim.community/)
2. **Apunte de Cátedra MAT1188:** *Introducción a la integral – Apunte base común*, Facultad de Ingeniería.
3. **Stewart, J.** (2012). *Cálculo de una variable: Trascendentes tempranas* (7.ª ed.). Cengage Learning. (Capítulo 5: Integrales y Teorema Fundamental del Cálculo).
4. **Thomas, G. B., Weir, M. D., & Hass, J.** (2010). *Cálculo: Una variable* (12.ª ed.). Pearson Educación.
5. **BlueDot.** (2023, 23 de enero). *Este TEOREMA lo CAMBIO TODO 🚀| ¿QUÉ es LA INTEGRAL? ▶ El FAMOSO NEXO entre DERIVADAS e INTEGRALES* [Video]. YouTube. https://www.youtube.com/watch?v=y6YQSUDTzqE
6. **3Blue1Brown.** (2017, 5 de mayo). *Integration and the fundamental theorem of calculus | Chapter 8, Essence of calculus* [Video]. YouTube. https://www.youtube.com/watch?v=rfG8ce4nNh0

---

## Declaración de Uso de Inteligencia Artificial

- **Herramienta:** Asistente IA Antigravity (Google DeepMind, Gemini 3.8 Flash).
- **Finalidad:** Apoyo en la estructura del código modular de Manim Community, redacción de documentación y formato en LaTeX / APA.
- **Verificación Humana:** Todos los desarrollos algebraicos, deducciones del Teorema Fundamental del Cálculo, cálculo de áreas e integrales, y relaciones de invariancia ante la constante $C$ fueron verificados y calculados a mano por los integrantes del equipo.
