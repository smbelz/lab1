"""CLI toolkit."""

import argparse
import sys

from .calculator import calculate
from .constants import EXIT_ERROR, EXIT_OK
from .converter import convert
from .errors import ToolkitError


def build_parser() -> argparse.ArgumentParser:
    """Собирает парсер.
    :return: ArgumentParser с подкомандами calc и convert.
    """
    parser = argparse.ArgumentParser(prog="toolkit", description="Консольный набор утилит: калькулятор и конвертер величин.")
    sub = parser.add_subparsers(dest="command", required=True)
    p_calc = sub.add_parser("calc", help="Вычисляет арифметическое выражение.")
    p_calc.add_argument("expression", help="Выражение, например '2 + 2 * 2'")
    p_conv = sub.add_parser("convert", help="Конвертирует величину.")
    p_conv.add_argument("value", help="Значение.")
    p_conv.add_argument("--from", dest="from_unit", required=True, help="Конвертирует из ...")
    p_conv.add_argument("--to", dest="to_unit", required=True,help="Конвертирует в ...")
    return parser


def command_calc(args: argparse.Namespace) -> int:
    """Обработка команды калькулятора.
    Принимает разобранные аргументы CLI с полем expression.
    :return: Код возврата процесса.
    """
    result = calculate(args.expression)
    print(result)
    return EXIT_OK


def command_convert(args: argparse.Namespace) -> int:
    """Обработка команды конвертера.
    Принимает разобранные аргументы CLI с полями value, from_unit, to_unit.
    :return: Код возврата процесса.
    """
    result = convert(args.value, args.from_unit, args.to_unit)
    print(result)
    return EXIT_OK


def main(arguments: list[str] | None = None) -> int:
    """Точка входа CLI.
    Принимает аргументы командной строки.
    :return: Код возврата процесса (0 — успешно, 2 — ошибка).
    """
    parser = build_parser()
    args = parser.parse_args(arguments)
    processing = {"calc": command_calc, "convert": command_convert}
    try:
        return processing[args.command](args)
    except ToolkitError as exc:
        print(exc, file=sys.stderr)
        return EXIT_ERROR


if __name__ == "__main__":
    main()
