import math
 
MAX_COUNT = 20         
MAX_ABS = 10_000        
  
def parse_number(word):
    try:
        return float(word)
    except ValueError:
        raise ValueError(f"{word} не является числом") from None
 
def check_values(values):
    if len(values) == 0:
        raise ValueError("последовательность пуста")
    if len(values) > MAX_COUNT:
        raise ValueError(f"чисел больше {MAX_COUNT}")
    for value in values:
        if not math.isfinite(value):
            raise ValueError(f"значение {value} не является конечным числом")
        if abs(value) > MAX_ABS:
            raise ValueError(f"значение {value} по модулю больше {MAX_ABS}")
  
def count(values):
    return len(values)
 
def total(values):
    result = 0
    for value in values:
        result += value
    return result
 
def mean(values):
    return total(values) / len(values)
 
def sum_squares(values):
    result = 0
    for value in values:
        result += value ** 2
    return result 
 
def root_mean_square(values):
    return math.sqrt(sum_squares(values) / len(values))
 
def sum_squared_deviations(values):
    average = mean(values)
    result = 0
    for value in values:
        result += (value - average) ** 2
    return result
  
def variance(values):
    return sum_squared_deviations(values) / len(values)
 
def sko(values):
    return math.sqrt(variance(values))
 
def std_dev(values):
    if len(values) < 2:
        return None
    return math.sqrt(sum_squared_deviations(values) / (len(values) - 1))
 
def minimum(values):
    result = values[0]
    for value in values:
        if value < result:
            result = value
    return result
 
def maximum(values):
    result = values[0]
    for value in values:
        if value > result:
            result = value
    return result
 
def count_positive(values):
    result = 0
    for value in values:
        if value > 0:
            result += 1
    return result 

def count_negative(values):
    result = 0
    for value in values:
        if value < 0:
            result += 1
    return result
 
REPORT = [
    ("Количество",    count,             "d"),
    ("Сумма",         total,             ".3f"),
    ("Ср. арифм.",    mean,              ".3f"),
    ("Сумма кв.",     sum_squares,       ".3f"),
    ("Ср. кв.",       root_mean_square,  ".3f"),
    ("Дисперсия",     variance,          ".3f"),
    ("СКО",           sko,               ".3f"),
    ("Станд. откл.",  std_dev,           ".3f"),
    ("Наименьшее",    minimum,           ".3f"),
    ("Наибольшее",    maximum,           ".3f"),
    ("Положительных", count_positive,    "d"),
    ("Отрицательных", count_negative,    "d"),
]
 