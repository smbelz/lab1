"""Токенизация.
Реализована функция tokenize() - разбитие выражения на токены."""

from .constants import CHAR, DIGITS, NUMBER
from .errors import InvalidCharacterError


def tokenize(expression: str) -> list[list[str]]:
    """Токенизация.
    Принимает исходное выражение.
    Выражение разбивается на токены, пробелы игнорируются.
    :return: Список токенов вида [тип, значение].
    Если есть недопустимый символ, бросает InvalidCharacterError.
    """
    tokens = []
    i = 0
    while i < len(expression):
        if expression[i] == " ":
            i += 1
        elif expression[i] in DIGITS or (
            expression[i] == "."
            and i < len(expression) - 1
            and expression[i + 1] in DIGITS
        ):
            start = i
            flag_dot = False
            while i < len(expression) and (
                expression[i] == "." or expression[i] in DIGITS
            ):
                if expression[i] == ".":
                    if flag_dot:
                        raise InvalidCharacterError()
                    flag_dot = True
                i += 1
            tokens.append([NUMBER, expression[start:i]])
        elif expression[i] in CHAR:
            tokens.append([CHAR[expression[i]], expression[i]])
            i += 1
        else:
            raise InvalidCharacterError()
    return tokens
