"""Тесты для конвертера величин.

Для результатов конвертации температур используется rel=1e-6, т.к. иначе из-за чисел с плавающей точкой получается
некорректный результат.
10 хороших тестов и 5 плохих."""

import pytest

from src.toolkit.converter import convert
from src.toolkit.errors import (
    BelowAbsoluteZeroError,
    IncompatibleUnitsError,
    InvalidValueError,
    UnknownUnitError,
)


def test_from_km_to_m() -> None:
    """Проверка конвертации из километров в метры."""
    assert convert(1, "km", "m") == pytest.approx(1000.0)


def test_from_km_to_m_uppercase() -> None:
    """Проверка конвертации из километров в метры с обработкой заглавных букв."""
    assert convert(10, "KM", "M") == pytest.approx(10000.0)


def test_from_m_to_cm() -> None:
    """Проверка конвертации из метров в сантиметры."""
    assert convert(1, "m", "cm") == pytest.approx(100.0)


def test_from_cm_to_m() -> None:
    """Проверка конвертации из сантиметров в метры."""
    assert convert(1000, "cm", "m") == pytest.approx(10.0)


def test_from_kg_to_g() -> None:
    """Проверка конвертации из килограммов в граммы."""
    assert convert(1, "kg", "g") == pytest.approx(1000.0)


def test_from_g_to_kg() -> None:
    """Проверка конвертации из граммов в килограммы."""
    assert convert(500, "g", "kg") == pytest.approx(0.5)


def test_from_celsius_to_kelvin() -> None:
    """Проверка конвертации из Цельсия в Кельвины."""
    assert convert(0, "c", "k") == pytest.approx(273.15, rel=1e-6)


def test_from_celsius_to_fahrenheit() -> None:
    """Проверка конвертации из Цельсия в Фаренгейты."""
    assert convert(100, "c", "f") == pytest.approx(212.0, rel=1e-6)


def test_from_fahrenheit_to_celsius() -> None:
    """Проверка конвертации из Фаренгейт в Цельсия."""
    assert convert(50, "f", "c") == pytest.approx(10.0, rel=1e-6)


def test_from_kelvin_to_celsius() -> None:
    """Проверка конвертации из Кельвинов в Цельсия."""
    assert convert(273.15, "k", "c") == pytest.approx(0.0, rel=1e-6)


def test_convert_unknown_unit() -> None:
    """Проверка конвертации выражения с неизвестной величиной. Бросает UnknownUnitError."""
    with pytest.raises(UnknownUnitError):
        convert(1, "m", "kilometers")


def test_convert_incompatible_units() -> None:
    """Проверка конвертации выражения, где использованы величины из разных групп, например граммы и сантиметры.
    Бросает IncompatibleUnitsError."""
    with pytest.raises(IncompatibleUnitsError):
        convert(1, "g", "cm")


def test_convert_incompatible_units2() -> None:
    """Проверка конвертации выражения, где использованы величины из разных групп, например метры и Фаренгейты.
    Бросает IncompatibleUnitsError."""
    with pytest.raises(IncompatibleUnitsError):
        convert(1, "m", "f")


def test_convert_below_absolute_zero() -> None:
    """Проверка конвертации выражения с температурой ниже абсолютного 0. Бросает BelowAbsoluteZeroError."""
    with pytest.raises(BelowAbsoluteZeroError):
        convert(-300, "c", "k")


def test_convert_invalid_value() -> None:
    """Проверка конвертации выражения, где использовано нечисловое значение. Бросает InvalidValueError."""
    with pytest.raises(InvalidValueError):
        convert("a", "m", "cm")
