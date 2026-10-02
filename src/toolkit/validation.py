"""Проверка корректности последовательности токенов.
Реализована функция validate() - проверка корректности выражения.

Правила:
- выражение не пустое;
- два числа, разделённые пробелом запрещены;
- в начале может стоять только унарный + или унарный -;
- оператор не может стоять в конце;
- два бинарных оператора подряд запрещены.
"""

from .constants import BINARY_OPERATORS, MINUS, NUMBER, PLUS
from .errors import EmptyExpression, MissingOperandError


def validate(tokens: list[list[str]]) -> None:
    """Проверка корректности токенов.
    Принимает список токенов [тип, значение].
    :return: Данная фанкция ничего не возвращает.
    Если список токенов пуст, бросает EmptyExpression.
    Если пропущен операнд, бросает MissingOperandError.
    """
    if not tokens:
        raise EmptyExpression()
    previous = None
    for token in tokens:
        t_type = token[0]
        if t_type == NUMBER:
            if previous is not None and previous[0] == NUMBER:
                raise MissingOperandError()
        else:
            if previous is None:
                if t_type != PLUS and t_type != MINUS:
                    raise MissingOperandError()
            elif previous[0] in BINARY_OPERATORS and t_type in BINARY_OPERATORS:
                raise MissingOperandError()
        previous = token
    if previous is not None and previous[0] in BINARY_OPERATORS:
        raise MissingOperandError()
