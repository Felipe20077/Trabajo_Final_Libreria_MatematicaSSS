# Librería Matemática en Python — Trabajo Final

**Asignatura:** Introducción a la Programación / Diseño de Informática 1  
**Profesor:** Joaquín Sánchez  
**Autor:** Daniel Murcia  

---

## 1. Descripción General y Ejecución

Este repositorio contiene una librería matemática implementada en Python puro (`libreria_matematica.py`) sin dependencias externas ni uso del módulo estándar `math` en los cálculos internos, acompañada de su archivo de validación (`pruebas.py`) que verifica los resultados y reporta los errores absolutos.

### Instrucciones de ejecución
1. Descargue `libreria_matematica.py` y `pruebas.py` en la misma carpeta local.
2. Abra una terminal en dicha carpeta y ejecute el comando: `python pruebas.py`

---

## 2. Métodos Numéricos, Intervalos y Tolerancias

* **Exponencial ($e^x$) y constante $e$:** Calculados mediante acumulación iterativa de la serie de Taylor $\sum_{k=0}^{N-1} \frac{x^k}{k!}$ usando $30$ términos ($35$ en llamadas internas de Newton-Raphson), logrando un error absoluto de $4.44 \times 10^{-16}$ en $e^1 \approx 2.71828183$ y $7.11 \times 10^{-15}$ en $e^3$.
* **Constante $\pi$:** Aproximada mediante la serie de Madhava-Leibniz $\pi = \sqrt{12} \sum_{k=0}^{29} \frac{(-1)^k}{(2k+1)3^k}$ con $30$ términos y cálculo propio de raíz cuadrada mediante el método babilónico (tolerancia $10^{-10}$), alcanzando precisión de máquina ($3.14159265$, error de $4.44 \times 10^{-16}$).
* **Funciones Trigonométricas ($\sin$, $\cos$, $\tan$):** Los argumentos en radianes se normalizan al intervalo $[-\pi, \pi]$ mediante aritmética modular. Seno y coseno se evalúan con series de Taylor incrementales de $15$ términos (errores de $1.11 \times 10^{-16}$ en $\sin(\pi/6) = 0.5$ y $0.00 \times 10^0$ en $\cos(0) = 1.0$). La tangente se obtiene como $\sin(x)/\cos(x)$, rechazando ángulos donde $|\cos(x)| < 10^{-6}$ (como $\pi/2$).
* **Logaritmo Natural ($\ln(x)$):** Resuelto mediante el algoritmo iterativo de Newton-Raphson sobre $f(y) = e^y - x = 0$ desde $y_0 = 0$. Se fijó una tolerancia de $|e^y - x| < 10^{-7}$ con un límite de $100$ iteraciones, validado en el rango $[1.0, 2.0]$ (errores de $0.00 \times 10^0$ en $\ln(1)$, $4.38 \times 10^{-11}$ en $\ln(1.5)$ y $8.00 \times 10^{-14}$ en $\ln(2)$) y bloqueando valores $x \le 0$ ($\ln(0)$ y $\ln(-3)$).
* **Máximo Común Divisor ($\text{mcd}$):** Implementado mediante una versión recursiva del algoritmo de Euclides utilizando el operador residuo (`%`), garantizando salida no negativa para entradas negativas ($\text{mcd}(-15, 0) = 15$, $\text{mcd}(-72, 108) = 36$) y retornando $0$ para $(0, 0)$.

---

## 3. Comparación de Sumas Parciales de Fourier

Aproximación de una onda cuadrada de amplitud $1$ y periodo $2\pi$ mediante $S_N(x) = \frac{4}{\pi} \sum_{k=0}^{N-1} \frac{\sin((2k+1)x)}{2k+1}$ para $N \in \{1, 5, 15\}$:

| Punto ($x$) | Valor Ideal | $N = 1$ ($S_1(x)$ / Error) | $N = 5$ ($S_5(x)$ / Error) | $N = 15$ ($S_{15}(x)$ / Error) |
| :--- | :---: | :---: | :---: | :---: |
| **$x = \pi/2$** | $1.0$ | $1.273240$ (Err: $0.273240$) | $1.063467$ (Err: $0.063467$) | $1.021232$ (Err: $0.021232$) |
| **$x = 3\pi/2$** | $-1.0$ | $-1.273240$ (Err: $0.273240$) | $-1.063467$ (Err: $0.063467$) | $-1.021232$ (Err: $0.021232$) |
| **$x = 0.1$** | $1.0$ | $0.127112$ (Err: $0.872888$) | $0.601865$ (Err: $0.398135$) | $1.177965$ (Err: $0.177965$) |

### Observaciones sobre la convergencia
* Incrementar el número de armónicos impares $N$ reduce progresivamente el error de aproximación en todos los puntos evaluados.
* En las zonas continuas ($x = \pi/2$ y $x = 3\pi/2$), el error cae por debajo de $0.022$ al llegar a $N = 15$.
* En las proximidades de la discontinuidad ($x = 0.1$), la serie requiere más armónicos para ajustarse al salto abrupto y presenta una ligera sobreoscilación inicial (fenómeno de Gibbs) con $N = 15$ antes de converger hacia $1.0$.
