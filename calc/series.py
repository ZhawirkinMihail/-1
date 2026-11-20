import math
 
MAX_TERMS = 10_000    
MAX_EPS = 0.0001          
MAX_ITERATIONS = 100_000  
DIGITS = math.ceil(-math.log10(MAX_EPS))
   
def sign(n):
    if n % 2 == 0:
        return -1
    return 1 

#(n-3)**3 + 2
def form(n):
    r = ((n-3) ** 3 - 8)
    if r == 0:
        return 0
    return sign(n)/r


def term_third(n):
    return sign(n) / (3 * n)
 
def term_sqplus(n):
    return sign(n) / (n * n + 1)

 
FORMULAS = {
    "third":  (term_third,  "S = 1/3 - 1/6 + 1/9 - ..."),
    "sqplus": (term_sqplus, "S = 1/(1^2+1) - 1/(2^2+1) + 1/(3^2+1) - ..."),
    "form": (form, "s = 1/((1-3)**3 + 2)"),
}
  
def check_terms(terms):
    if not 1 <= terms <= MAX_TERMS:
        raise ValueError("количество слагаемых вне диапазона")
 
def check_eps(eps):
    if not (math.isfinite(eps) and 0 < eps <= MAX_EPS):
        raise ValueError("точность вне диапазона")
def safe_term(term, n):
    try:
        return term(n)
    except ZeroDivisionError:
        return 0
    
def sum_by_count(term, count):
    result = 0
    for n in range(1, count + 1):
        result += safe_term(term, n)
    return result
 
def sum_by_eps(term, eps):
    result = 0
    n = 0
    while True:
        n += 1
        value = safe_term(term, n)
        result += value
        if value != 0 and abs(value) < eps:
            return result, n
        if n >= MAX_ITERATIONS:
            raise ValueError("точность не достигнута")
 