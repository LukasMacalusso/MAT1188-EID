# Fundamentación Matemática y Guion Técnico: Teorema Fundamental del Cálculo (Parte II)

**Asignatura:** MAT1188 – Cálculo Intermedio  
**Eje 9 / Grupo 9:** Calcular una integral mediante antiderivadas  
**Pregunta Central:** *¿Por qué una integral definida puede calcularse como $F(b) - F(a)$?*

## 1. Fundamento Matemático

El cálculo de áreas mediante el límite formal de sumas de Riemann requiere evaluar sumatorias y límites que resultan extensos incluso para funciones elementales. El Teorema Fundamental del Cálculo (TFC) relaciona la acumulación de área bajo una curva con el concepto de antiderivada.

- **Condición necesaria:** La función $f(x)$ debe ser continua en el intervalo cerrado $[a, b]$.
- **Síntesis de la respuesta:** La función de acumulación $G(x') = \int_a^{x'} f(t)\,dt$ mide el área acumulada desde $a$ hasta $x'$ y cumple que $G'(x') = f(x')$, siendo una antiderivada particular con $G(a) = 0$. Cualquier otra antiderivada $F(x)$ difiere de $G(x)$ en una constante aditiva ($F(x) = G(x) + C$). Al calcular la diferencia $F(b) - F(a)$, la constante $C$ se cancela y se obtiene exactamente $\int_a^b f(x)\,dx$.

## 2. Estructura de Escenas

### Paso 1: Motivación mediante Sumas de Riemann (`scene1_riemann_motivation.py`)
- **Definición:** La integral definida se expresa como el límite de sumas de Riemann:
  $$\int_a^b f(x)\,dx = \lim_{n \to \infty} \sum_{i=1}^n f(x_i^*)\,\Delta x, \quad \Delta x = \frac{b - a}{n}$$
- **Desarrollo en escena:**
  - Trazado de $f(x) = 3x^2$ en el intervalo $[1, 2]$.
  - Aproximación mediante rectángulos con $n = 4$, $n = 8$ y $n = 32$, mostrando la convergencia numérica hacia el área exacta ($7.00$) y la necesidad de contar con un método analítico directo.

### Paso 2: Función de Acumulación y TFC Parte I (`scene2_accumulation_tfc1.py`)
- **Definición:** Se define la función de acumulación con extremo superior variable $x' \in [a, b]$:
  $$G(x') = \int_a^{x'} f(t)\,dt$$
- **Diferencial de área:**
  - Al incrementar $x'$ en una cantidad $\Delta x$, la variación de área $\Delta G$ se aproxima por un rectángulo de base $\Delta x$ y altura $f(x')$:
    $$\Delta G \approx f(x') \cdot \Delta x \implies \frac{\Delta G}{\Delta x} \approx f(x')$$
  - En el límite cuando $\Delta x \to 0$:
    $$\frac{dG}{dx'} = f(x')$$
- **Conclusión:** La derivada de la función de acumulación es la función original $f(x')$; por lo tanto, $G(x')$ es una antiderivada de $f$.

### Paso 3: Familia de Antiderivadas (`scene3_antiderivative_theory.py`)
- **Definición:** Una función $F(x)$ es antiderivada de $f(x)$ si $F'(x) = f(x)$.
- **Propiedad de la constante:**
  - Dado que $\frac{d}{dx}(C) = 0$, al sumar una constante arbitraria $C$ a $G(x')$ la derivada se mantiene invariante:
    $$(G(x') + C)' = G'(x') + 0 = f(x')$$
  - Toda antiderivada general se expresa como:
    $$F(x') = G(x') + C$$

### Paso 4: Deducción de la Regla de Barrow (`scene4_barrow_deduction.py`)
- **Deducción algebraica:**
  1. Relación entre primitivas:
     $$F(x') = G(x') + C$$
  2. Evaluación en el límite inferior ($x' = a$):
     $$G(a) = \int_a^a f(t)\,dt = 0 \implies F(a) = C$$
  3. Evaluación en el límite superior ($x' = b$):
     $$G(b) = \int_a^b f(t)\,dt \implies F(b) = G(b) + C$$
  4. Diferencia entre ambos extremos:
     $$F(b) - F(a) = [G(b) + C] - [G(a) + C] = G(b) - 0$$
  5. Resultado (Regla de Barrow):
     $$\int_a^b f(x)\,dx = F(b) - F(a)$$
- **Observación:** La constante $C$ se anula en la sustracción ($C - C = 0$), por lo que el resultado es independiente de la antiderivada elegida.

### Paso 5: Ejemplo Resuelto y Verificación (`scene5_example_calculation.py`)
- **Planteamiento:** Evaluar $\int_1^2 3x^2\,dx$.
- **Resolución mediante Regla de Barrow:**
  - Antiderivada: $F(x) = x^3$.
  - Evaluación en los extremos:
    $$\int_1^2 3x^2\,dx = \Big[ x^3 \Big]_1^2 = 2^3 - 1^3 = 8 - 1 = 7$$
- **Verificación con constante $C \neq 0$:**
  - Tomando $F_2(x) = x^3 + 5$:
    $$F_2(2) - F_2(1) = (2^3 + 5) - (1^3 + 5) = 13 - 6 = 7$$
