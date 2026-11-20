import argparse
 
from calc import integration, series
 
 
def build_parser():
    parser = argparse.ArgumentParser(
        prog="mathtool",
        description="mathtool — расчёты над уравнениями и числовыми последовательностями",
        allow_abbrev=False,
    )
    commands = parser.add_subparsers(dest="command", title="команды")
 
    solve = commands.add_parser(
        "solve", help="решение уравнения A*x^2 + B*x + C = 0",
        description="Решение уравнения A*x^2 + B*x + C = 0. "
                    "Без параметров коэффициенты запрашиваются с клавиатуры.",
        allow_abbrev=False)
    solve.add_argument("-a", type=int, help="коэффициент A: целое, по модулю не более 10000")
    solve.add_argument("-b", type=int, help="коэффициент B: целое, по модулю не более 10000")
    solve.add_argument("-c", type=int, help="коэффициент C: целое, по модулю не более 10000")
 
    stats = commands.add_parser(
        "stats", help="показатели числовой последовательности",
        description="Чтение чисел (не более 20) и вывод показателей последовательности.",
        allow_abbrev=False)
    stats.add_argument("--input", help="файл с числами; без него числа читаются "
                                       "со стандартного ввода")
 
    ser = commands.add_parser(
        "series", help="сумма знакочередующегося ряда",
        description="Сумма ряда: остановка по количеству слагаемых или по точности.",
        allow_abbrev=False)
    ser.add_argument("--func", required=True, choices=sorted(series.FORMULAS),
                     help="какой ряд суммировать")
    group = ser.add_mutually_exclusive_group(required=True)
    group.add_argument("--terms", type=int,
                       help="сколько слагаемых сложить: целое от 1 до 10000")
    group.add_argument("--eps", type=float,
                       help="считать, пока слагаемое по модулю не станет меньше eps; "
                            "0 < eps <= 0.0001")
 
    integ = commands.add_parser(
        "integrate", help="численное интегрирование (левые прямоугольники)",
        description="Значение интеграла методом левых прямоугольников.",
        allow_abbrev=False)
    integ.add_argument("--func", required=True, choices=sorted(integration.FUNCTIONS),
                       help="какую функцию интегрировать")
    integ.add_argument("--from", dest="start", type=float, required=True,
                       help="нижний предел интегрирования")
    integ.add_argument("--to", dest="end", type=float, required=True,
                       help="верхний предел интегрирования, больше нижнего")
    integ.add_argument("--steps", type=int, required=True,
                       help="число прямоугольников: целое от 1 до 100000")
 
    return parser
 