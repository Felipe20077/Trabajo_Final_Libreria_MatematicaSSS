"""
Script de validacion para la libreria matematica propia.
Compara las aproximaciones obtenidas frente a los valores reales de math.
"""
import math
import libreria_matematica as lm

def verificar(etiqueta: str, obtenido: float, esperado: float) -> None:
    err_abs = lm.abs_val(obtenido - esperado)
    print(f"- {etiqueta:<22} | Propio: {obtenido:12.8f} | Real: {esperado:12.8f} | Error: {err_abs:.2e}")

print("---------------------------------------------------------------------------")
print("1. EXPONENCIAL Y CONSTANTES FUNDAMENTALES")
print("---------------------------------------------------------------------------")
verificar("e^0", lm.calc_exp(0), math.exp(0))
verificar("Constante e (e^1)", lm.obtener_e(), math.e)
verificar("e^3", lm.calc_exp(3), math.exp(3))
verificar("Constante pi", lm.obtener_pi(), math.pi)

print("\n---------------------------------------------------------------------------")
print("2. FUNCIONES TRIGONOMETRICAS")
print("---------------------------------------------------------------------------")
verificar("sin(pi/6)", lm.calc_seno(math.pi / 6), math.sin(math.pi / 6))
verificar("sin(pi/3)", lm.calc_seno(math.pi / 3), math.sin(math.pi / 3))
verificar("cos(0)", lm.calc_coseno(0), math.cos(0))
verificar("cos(pi/3)", lm.calc_coseno(math.pi / 3), math.cos(math.pi / 3))
verificar("tan(pi/4)", lm.calc_tan(math.pi / 4), math.tan(math.pi / 4))

print("\nValidacion de frontera en tangente:")
print("  tan(pi/2) ->", lm.calc_tan(math.pi / 2))

print("\n---------------------------------------------------------------------------")
print("3. LOGARITMO NATURAL (NEWTON-RAPHSON)")
print("---------------------------------------------------------------------------")
verificar("ln(1.0)", lm.calc_ln(1.0), math.log(1.0))
verificar("ln(1.5)", lm.calc_ln(1.5), math.log(1.5))
verificar("ln(2.0)", lm.calc_ln(2.0), math.log(2.0))

print("\nValidaciones de dominio en logaritmo:")
print("  ln(0)  ->", lm.calc_ln(0))
print("  ln(-3) ->", lm.calc_ln(-3))

print("\n---------------------------------------------------------------------------")
print("4. MAXIMO COMUN DIVISOR (EUCLIDES RECURSIVO)")
print("---------------------------------------------------------------------------")
casos_mcd = [(48, 18), (-15, 0), (-72, 108), (0, 0)]
for num1, num2 in casos_mcd:
    print(f"  MCD({num1}, {num2}) = {lm.hallar_mcd(num1, num2)}")

print("\n---------------------------------------------------------------------------")
print("5. SERIE DE FOURIER (ONDA CUADRADA)")
print("---------------------------------------------------------------------------")
evaluaciones = [
    ("pi/2", math.pi / 2, 1.0),
    ("3pi/2", 3 * math.pi / 2, -1.0),
    ("0.1", 0.1, 1.0)
]

for nombre_x, valor_x, ref in evaluaciones:
    print(f"\nEvaluando en x = {nombre_x} (Referencia ideal: {ref}):")
    for armonicos in [1, 5, 15]:
        res_fourier = lm.serie_fourier(valor_x, armonicos)
        diff = lm.abs_val(res_fourier - ref)
        print(f"  N = {armonicos:2d} terminos -> Aproximacion = {res_fourier:9.6f} | Error abs = {diff:.6f}")
