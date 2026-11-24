"""
Modulo de funciones matematicas basicas y aproximaciones numericas.
Desarrollado sin dependencias de la libreria math.
"""

def abs_val(numero: float) -> float:
    """Devuelve la magnitud positiva de un numero real."""
    return -numero if numero < 0 else numero

def raiz_cuadrada(n: float, tol: float = 1e-10) -> float:
    """Calcula la raiz cuadrada positiva mediante el metodo babilonico."""
    if n == 0:
        return 0.0
    estimacion = n / 2.0
    while abs_val(estimacion * estimacion - n) > tol:
        estimacion = 0.5 * (estimacion + n / estimacion)
    return estimacion

# ---------------------------------------------------------
# 1. EXPONENCIAL Y CONSTANTES MATEMATICAS
# ---------------------------------------------------------

def calc_exp(x: float, n_terminos: int = 30) -> float:
    """
    Aproxima e^x mediante serie de Taylor acumulando terminos de forma iterativa.
    """
    total = 1.0
    termino_actual = 1.0
    for k in range(1, n_terminos):
        termino_actual = termino_actual * (x / k)
        total += termino_actual
    return total

def obtener_e(n_terminos: int = 30) -> float:
    """Retorna la aproximacion de Euler evaluando calc_exp(1)."""
    return calc_exp(1.0, n_terminos)

def obtener_pi(n_terminos: int = 30) -> float:
    """
    Aproxima pi usando la serie de Madhava-Leibniz:
    pi = sqrt(12) * sum((-1)^k / ((2k + 1) * 3^k))
    """
    suma = 0.0
    potencia_tres = 1.0
    signo = 1.0
    for k in range(n_terminos):
        suma += signo / ((2 * k + 1) * potencia_tres)
        signo = -signo
        potencia_tres *= 3.0
    return raiz_cuadrada(12.0) * suma

# ---------------------------------------------------------
# 2. TRIGONOMETRIA EN RADIANES
# ---------------------------------------------------------

def ajustar_rango(rad: float) -> float:
    """Lleva cualquier angulo en radianes al rango [-pi, pi] usando modulo."""
    pi = obtener_pi()
    dos_pi = 2.0 * pi
    return ((rad + pi) % dos_pi) - pi

def calc_seno(rad: float, n_terminos: int = 15) -> float:
    """Calcula sin(rad) con serie de Taylor incremental."""
    x = ajustar_rango(rad)
    termino = x
    suma = x
    for k in range(1, n_terminos):
        termino = -termino * x * x / ((2 * k) * (2 * k + 1))
        suma += termino
    return suma

def calc_coseno(rad: float, n_terminos: int = 15) -> float:
    """Calcula cos(rad) con serie de Taylor incremental."""
    x = ajustar_rango(rad)
    termino = 1.0
    suma = 1.0
    for k in range(1, n_terminos):
        termino = -termino * x * x / ((2 * k - 1) * (2 * k))
        suma += termino
    return suma

def calc_tan(rad: float) -> float:
    """Calcula tan(rad) verificando que el coseno no sea cercano a cero."""
    val_cos = calc_coseno(rad)
    if abs_val(val_cos) < 1e-6:
        print("Aviso: Tangente indefinida para el angulo ingresado (coseno ~ 0).")
        return None
    return calc_seno(rad) / val_cos

# ---------------------------------------------------------
# 3. LOGARITMO NATURAL (NEWTON-RAPHSON)
# ---------------------------------------------------------

def calc_ln(x: float, tol: float = 1e-7, limite_iter: int = 100) -> float:
    """
    Aproxima ln(x) para x > 0 resolviendo e^y - x = 0 mediante Newton-Raphson.
    """
    if x <= 0:
        print("Aviso: El logaritmo natural no existe para valores menores o iguales a 0.")
        return None

    y = 0.0
    for _ in range(limite_iter):
        exp_y = calc_exp(y, 35)
        diferencia = exp_y - x
        if abs_val(diferencia) < tol:
            return y
        y = y - (diferencia / exp_y)

    print("Aviso: No se alcanzo convergencia dentro del limite de iteraciones.")
    return y

# ---------------------------------------------------------
# 4. MAXIMO COMUN DIVISOR (EUCLIDES RECURSIVO)
# ---------------------------------------------------------

def hallar_mcd(a: int, b: int) -> int:
    """
    Calcula el MCD de dos enteros usando recursion y el operador residuo (%).
    """
    a = -a if a < 0 else a
    b = -b if b < 0 else b
    if b == 0:
        return a
    return hallar_mcd(b, a % b)

# ---------------------------------------------------------
# 5. SERIE DE FOURIER PARA ONDA CUADRADA
# ---------------------------------------------------------

def serie_fourier(x: float, N: int) -> float:
    """
    Calcula la suma parcial de N armonicos impares para una onda cuadrada
    de amplitud 1 y periodo 2*pi.
    """
    if N <= 0:
        print("Aviso: El numero de armonicos N debe ser mayor que cero.")
        return None

    pi = obtener_pi()
    acumulado = 0.0
    for k in range(N):
        armonico = 2 * k + 1
        acumulado += calc_seno(armonico * x) / armonico

    return (4.0 / pi) * acumulado
