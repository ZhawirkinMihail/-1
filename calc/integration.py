import math
 
MIN_STEPS = 1
MAX_STEPS = 100_000
 
DIGITS = 4
  
def F_ratio(x):
    """F(x) = x / (x + 1)."""
    return x / (x + 1)
 
 
def F_root(x):
    """F(x) = sqrt(x^2 + 1)."""
    return math.sqrt(x * x + 1)
  
FUNCTIONS = {
    "ratio": (F_ratio, "F(x) = x / (x + 1)",   0, 20, True),
    "root":  (F_root,  "F(x) = sqrt(x^2 + 1)", -5, 5, False),
}
 
  
def check_params(name, start, end, steps):
    if not (math.isfinite(start) and math.isfinite(end)):
        raise ValueError("предел интегрирования не является конечным числом")
    if start >= end:
        raise ValueError("начальный предел не меньше конечного")
 
    _, _, low, high, closed = FUNCTIONS[name]
    for value in (start, end):
        if closed:
            outside = value < low or value > high
        else:
            outside = value <= low or value >= high
        if outside:
            left, right = ("[", "]") if closed else ("(", ")")
            raise ValueError(f"предел вне промежутка {left}{low}; {high}{right}")
 
    if not MIN_STEPS <= steps <= MAX_STEPS:
        raise ValueError("количество шагов вне диапазона")
  
def integral(function, start, end, steps):
    dx = (end - start) / steps
    result = 0
    for i in range(steps):
        x = start + i * dx      
        result += function(x) * dx
    return result
 