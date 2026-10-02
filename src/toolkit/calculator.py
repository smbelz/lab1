"""Калькулятор.

Реализованы функции:
1) tokenize() - разбитие выражения на токены;
2) validate() - проверка корректности выражения;
3) calculate() - вычисление.

Поддержаны:
1) целые и вещественные числа;
2) +, -, *, /;
3) унарные - и +;
4) приоритет * и / над + и -;
5) целые результаты возвращаются как int, дробные как float;
6) запрещены 2 бинарных оператора подряд.
"""


from .constants import MINUS, NUMBER, PLUS, SLASH, STAR
from .errors import DivisionByZeroError, MissingOperandError, UnknownOperatorError
from .tokenization import tokenize
from .validation import validate


def apply_operator(operator: str, a: float, b: float) -> float:
    """Применяет бинарный оператор к числам.
    Принимает тип оператора, левый и правый операнды.
    :return: Результат операции.
    Если есть деление на 0, бросает DivisionByZeroError.
    Если есть неизвестный оператор, бросает UnknownOperatorError.
    """
    if operator == PLUS:
        return a + b
    if operator == MINUS:
        return a - b
    if operator == STAR:
        return a * b
    if operator == SLASH:
        if b != 0:
            return a / b
        raise DivisionByZeroError()
    raise UnknownOperatorError()


class Parser:
    """Реализация рекурсивного спуска."""

    def __init__(self, tokens: list[list[str]]) -> None:
        """Создаёт парсер.
        Принимает список токенов [тип, значение].
        :return: Данная функция ничего не возвращает.
        """
        self.tokens = tokens
        self.pos = 0

    def parse(self) -> float:
        """Точка входа парсера.
        :return: Результат вычисления выражения.
        Если остались непрочитанные токены, бросает MissingOperandError.
        """
        result = self.expr()
        if self.pos != len(self.tokens):
            raise MissingOperandError()
        return result

    def current(self) -> list[str] | None:
        """Возвращает текущий токен и не сдвигает позицию.
        :return: Текущий токен. Если токены закончились, то None.
        """
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def next(self) -> list[str]:
        """Возвращает текущий токен и сдвигает позицию.
        :return: Текущий токен.
        """
        token = self.tokens[self.pos]
        self.pos += 1
        return token

    def expr(self) -> float:
        """Операции с низким приоритетом.
        :return: Значение подвыражения после обработки + и -.
        """
        left = self.term()
        while True:
            token = self.current()
            if token is None or token[0] != PLUS and token[0] != MINUS:
                break
            self.next()
            right = self.term()
            left = apply_operator(token[0], left, right)
        return left

    def term(self) -> float:
        """Операции с высоким приоритетом.
        :return: Значение подвыражения после обработки * и /.
        """
        left = self.unary()
        while True:
            token = self.current()
            if token is None or token[0] != STAR and token[0] != SLASH:
                break
            self.next()
            right = self.unary()
            left = apply_operator(token[0], left, right)
        return left

    def unary(self) -> float:
        """Унарные операторы.
        :return: Значение подвыражения с унарными + и -.
        """
        token = self.current()
        if token is not None and (token[0] == MINUS or token[0] == PLUS):
            self.next()
            value = self.unary()
            if token[0] == PLUS:
                return value
            else:
                return -value
        return self.primary()

    def primary(self) -> float:
        """Числа.
        :return: Числовое значение токена.
        Если токен не число, бросает MissingOperandError.
        """
        token = self.next()
        if token[0] == NUMBER:
            return float(token[1])
        raise MissingOperandError()


def float_to_int(value: float) -> int | float:
    """Приводит float к int.
    Принимает число с плавающей точкой.
    :return: int если число целое, иначе - float.
    """
    if value == int(value):
        return int(value)
    return value


def calculate(expression: str) -> int | float:
    """Точка входа.
    Принимает выражение и выполняет токенизацию -> валидацию -> парсинг -> приведение к нужному типу.
    :return: Результат вычисления.
    """
    tokens = tokenize(expression)
    validate(tokens)
    result = Parser(tokens).parse()
    return float_to_int(result)
