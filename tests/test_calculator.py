"""Тесты для калькулятора.

15 хороших тестов и 5 плохих."""

import pytest

from src.toolkit.calculator import calculate
from src.toolkit.errors import (
    DivisionByZeroError,
    EmptyExpression,
    InvalidCharacterError,
    MissingOperandError,
)


def test_single_number() -> None:
    """Проверка вычислений вида '1'."""
    assert calculate("1") == pytest.approx(1)


def test_negative_number() -> None:
    """Проверка вычислений вида '-1'."""
    assert calculate("-1") == pytest.approx(-1)


def test_double_negative() -> None:
    """Проверка вычислений вида '--1'."""
    assert calculate("--1") == pytest.approx(1)


def test_minus_minus() -> None:
    """Проверка вычислений вида '1--1'."""
    assert calculate("1--1") == pytest.approx(2)


def test_plus_plus() -> None:
    """Проверка вычислений вида '1++1'."""
    assert calculate("1++1") == pytest.approx(2)


def test_plus_minus() -> None:
    """Проверка вычислений вида '1+-1'."""
    assert calculate("1+-1") == pytest.approx(0)


def test_multiply_negative() -> None:
    """Проверка вычислений вида '2*-2'."""
    assert calculate("2*-2") == pytest.approx(-4)


def test_divide_negative() -> None:
    """Проверка вычислений вида '2/-2'."""
    assert calculate("2/-2") == pytest.approx(-1)


def test_multiply_and_add() -> None:
    """Проверка вычислений с приоритетом операций, например '2 + 2 * 5'."""
    assert calculate("2 + 2 * 5") == pytest.approx(12)


def test_whitespace_handling() -> None:
    """Проверка вычислений, где между операндами стоит несколько пробелов, например '   2     *    9'."""
    assert calculate("   2     *    9") == pytest.approx(18)


def test_division_int() -> None:
    """Проверка вычислений, где в итоге должно получиться целое число, например '4 / 2'."""
    assert calculate("4 / 2") == pytest.approx(2)


def test_division_float() -> None:
    """Проверка вычислений, где в итоге должно получиться число с плавающей точкой, например '10 / 4'."""
    assert calculate("10 / 4") == pytest.approx(2.5)


def test_unary_plus() -> None:
    """Проверка вычислений с унарным плюсом, например '+1 + 10'."""
    assert calculate("+1 + 10") == pytest.approx(11)


def test_float_multiplication() -> None:
    """Проверка вычислений, где целое число умножается на число с плавающей точкой. Если возможно, результат целый,
    например '4 * 2.5'."""
    assert calculate("4 * 2.5") == pytest.approx(10)


def test_all_operators() -> None:
    """Проверка вычислений, где используются все операции, например '1 + 4 * 10 / 5 - 8'."""
    assert calculate("1 + 4 * 10 / 5 - 8") == pytest.approx(1)


def test_calculate_empty_expression() -> None:
    """Проверка вычисления пустого выражения. Бросает EmptyExpression."""
    with pytest.raises(EmptyExpression):
        calculate(" ")


def test_calculate_invalid_character() -> None:
    """Проверка вычисления выражения с недопустимым символом. Бросает EmptyExpression."""
    with pytest.raises(InvalidCharacterError):
        calculate("a + 2")


def test_calculate_division_by_zero() -> None:
    """Проверка вычисления выражения с делением на 0. Бросает DivisionByZeroError."""
    with pytest.raises(DivisionByZeroError):
        calculate("1 / 0")

def test_calculate_missing_operand() -> None:
    """Проверка вычисления выражения с пропущенным операндом. Бросает MissingOperandError."""
    with pytest.raises(MissingOperandError):
        calculate("* 10")


def test_calculate_two_operand() -> None:
    """Проверка вычисления выражения с двумя операндами без оператора. Бросает MissingOperandError."""
    with pytest.raises(MissingOperandError):
        calculate("1 1")
