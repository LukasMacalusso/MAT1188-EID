# MAT1188 – Cálculo Intermedio: Proyecto Manim (EID)

## Grupo 9 – Eje 9: Teorema Fundamental del Cálculo (Parte II) y Regla de Barrow
**Pregunta Central:** *¿Por qué una integral definida puede calcularse como $F(b) - F(a)$?*

---

## Contenido del Repositorio

- `Documentacion_matematica.md`: Fundamentación matemática rigurosa, deducción paso a paso de la Regla de Barrow a partir de la función de acumulación $G(x')$, justificación de la cancelación de la constante $C$ y especificaciones técnicas de animación.
- `pyproject.toml`: Configuración, metadatos y dependencias gestionadas mediante `uv`.
- `main.py`: CLI orquestador integral para renderizar escenas individuales, compilar todas las escenas y ensamblar el video final unificado (`ffmpeg`).
- `src/common/`: 
  - `style.py`: Paleta cromática estandarizada, tamaños tipográficos y funciones auxiliares de diseño.
  - `math_defs.py`: Definiciones analíticas de $f(x)=3x^2$, primitiva $F(x)=x^3$, función de acumulación $G(x')$ y sumas de Riemann.
- `src/scenes/`: Código modular de las 5 escenas de animación en Manim Community:
  1. `scene1_riemann_motivation.py`: Motivación geométrica y refinamiento de sumas de Riemann ($n=4 \to 8 \to 32$).
  2. `scene2_accumulation_tfc1.py`: Función de acumulación $G(x')$, franja diferencial $\Delta x$ y deducción de $\frac{dG}{dx'} = f(x')$.
  3. `scene3_antiderivative_theory.py`: Definición formal de antiderivada, rol de la constante $C$ y familia de primitivas $F(x') = G(x') + C$.
  4. `scene4_barrow_deduction.py`: Deducción analítica de Barrow evaluando en $a$ y $b$, cancelación algebraica de $C$ y respuesta explícita a la pregunta central.
  5. `scene5_example_calculation.py`: Ejemplo resuelto con $f(x) = 3x^2$ en $[1, 2]$, área $= 7$, verificación de invariancia ante $C$ y síntesis.

---

## Requisitos y Entorno de Ejecución

- **uv:** Gestor de paquetes y entornos de Python ultrarrápido.
- **Python:** 3.10 o superior (el entorno virtual gestionado por `uv` utiliza CPython 3.13 / 3.14).
- **Manim Community:** Versión 0.18.0 o superior (instalado Manim CE 0.22.0).
- **FFmpeg:** Requerido para la codificación y ensamblado final de los videos MP4.
- **LaTeX / TinyTeX:** Motor tipográfico con soporte de `amsmath`, `mathtools` y `dvisvgm` para el renderizado vectorial de fórmulas matemáticas.

---

## Comandos de Ejecución y Renderizado

El script `main.py` permite orquestar de forma sencilla todo el ciclo de renderizado:

### 1. Renderizado individual de escenas
```bash
# Renderizar escena específica en calidad media (720p, 30fps por defecto)
uv run python main.py --scene 1
uv run python main.py --scene 4

# Renderizar en baja resolución para previsualización rápida (480p, 15fps)
uv run python main.py --scene 2 -q low

# Renderizar en alta definición (1080p, 60fps)
uv run python main.py --scene 5 -q high
```

### 2. Renderizado de todas las escenas en lote
```bash
# Renderiza secuencialmente las 5 escenas del proyecto en 720p
uv run python main.py --all -q med
```

### 3. Compilación del video final unificado
```bash
# Concatena automáticamente los 5 clips generados en un único archivo MP4
uv run python main.py --merge -q med
```
El archivo resultante se generará en la raíz del proyecto como `MAT1188_Grupo9_EID_Completo_med.mp4`.

---

## Fuentes y Bibliografía

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
