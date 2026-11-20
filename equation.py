import math
MAX_VALUE = 10_000

def check_coefficients(coefficients):

    for name, value in coefficients.items():
        if abs(value) > MAX_VALUE:
            raise ValueError(f"коэффициент {name} вне допустимого диапазона")
    if coefficients["A"] == 0 and coefficients["B"] == 0:
        raise ValueError("это не уравнение: A и B равны нулю")

def solve(a, b, c):     
    if a == 0:
        return "линейное", None, [-c / b + 0.0]

    d = b * b - 4 * a * c
    if d > 0:
        root = math.sqrt(d)
        x1 = (-b + root) / (2 * a) + 0.0
        x2 = (-b - root) / (2 * a) + 0.0
        return "квадратное", d, [x1, x2]
    if d == 0:
        return "квадратное", d, [-b / (2 * a) + 0.0]
    return "квадратное", d, []
