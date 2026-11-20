import sys
import cli
from calc import equation, integration, series, stats
EXIT_OK = 0
EXIT_DATA_ERROR = 1

def ask_coefficient(name):
    text = input(f"Введите {name}: ")
    try:
        return int(text)
    except ValueError:
        raise ValueError(f"коэффициент {name} не является целым числом") from None


def handle_solve(args):
    given = [args.a, args.b, args.c]
    if all(value is None for value in given):
        a, b, c = ask_coefficient("A"), ask_coefficient("B"), ask_coefficient("C")
    elif any(value is None for value in given):
        raise ValueError("укажите все три коэффициента либо ни одного")
    else:
        a, b, c = given

    equation.check_coefficients({"A": a, "B": b, "C": c})
    kind, discriminant, roots = equation.solve(a, b, c)

    print(f"Уравнение {kind}")
    
    if discriminant is not None:
        print(f"Дискриминант: {discriminant}")
    if len(roots) == 2:
        print(f"x1 = {roots[0]:.3f}")
        print(f"x2 = {roots[1]:.3f}")
    elif len(roots) == 1:
        print(f"x = {roots[0]:.3f}")
    else:
        print("Действительных корней нет")
    return EXIT_OK

def read_numbers(lines):
    values = []
    for line in lines:
        for word in line.split():
            values.append(stats.parse_number(word))
    return values

def handle_stats(args):
    if args.input is not None:
        with open(args.input, encoding="utf-8-sig") as handle:
            values = read_numbers(handle)
    else:
        numbers = []
        if sys.stdin.isatty():
            print('Введите числа: ')
        while True:
            try:
                text = input()
            except EOFError:        
                break
            if text == '':
                break
            numbers.extend(text.split())
        values = read_numbers(numbers)
    stats.check_values(values)

    for label, function, form in stats.REPORT:
        value = function(values)
        if value is None:
            print(f"{label}: НЕ СУЩЕСТВУЕТ")
        else:
            print(f"{label}: {value:{form}}")
    return EXIT_OK


def handle_series(args):
    if args.terms is not None:
        series.check_terms(args.terms)
    else:
        series.check_eps(args.eps)

    term, formula = series.FORMULAS[args.func]
    if args.terms is not None:
        count = args.terms
        result = series.sum_by_count(term, count)
    else:
        result, count = series.sum_by_eps(term, args.eps)

    print(formula)
    print(f"Слагаемых: {count}")
    print(f"Сумма ряда: {result:.{series.DIGITS}f}")
    return EXIT_OK


def handle_integrate(args):
    integration.check_params(args.func, args.start, args.end, args.steps)
    function, formula, _, _, _ = integration.FUNCTIONS[args.func]
    result = integration.integral(function, args.start, args.end, args.steps)
    print(formula)
    print(f"Значение интеграла: {result:.{integration.DIGITS}f}")
    return EXIT_OK

HANDLERS = {
    "solve": handle_solve,
    "stats": handle_stats,
    "series": handle_series,
    "integrate": handle_integrate,
}


def describe_error(error):
    if isinstance(error, OSError) and error.filename is not None:
        return f"файл не открывается: {error.filename}"
    return str(error)

def main(argv):
    parser = cli.build_parser()
    args = parser.parse_args(argv)
    if args.command is None:
        parser.print_help()
        return EXIT_OK
    try:
        return HANDLERS[args.command](args)
    except (ValueError, OSError) as error:
        print(f"ОШИБКА: {describe_error(error)}", file=sys.stderr)
        return EXIT_DATA_ERROR
    except EOFError:
        print("ОШИБКА: ввод прерван", file=sys.stderr)
        return EXIT_DATA_ERROR

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
    print("hi")
