"""Конвертер.

Поддерживает группы:
* длина: mm, cm, m, km;
* масса: g, kg;
* температура: c, f, k.
Правила:
- регистр единиц не учитывается;
- конвертация между разными группами запрещена;
- температура ниже абсолютного 0 запрещена;
- результат возвращается как float.
"""

from .constants import (
    CELSIUS,
    FAHRENHEIT,
    FROM_CELSIUS_TO_KELVIN,
    FROM_FAHRENHEIT_CONSTANT,
    FROM_FAHRENHEIT_TO_KELVIN,
    KELVIN,
    LENGTH,
    MASS,
    TEMPERATURE,
)
from .errors import (
    BelowAbsoluteZeroError,
    IncompatibleUnitsError,
    InvalidValueError,
    UnknownUnitError,
)

LENGTH_FACTOR = {"mm": 0.001, "cm": 0.01, "m": 1.0, "km": 1000.0}
MASS_FACTOR = {"g": 0.001, "kg": 1.0}
TEMPERATURE_NAMES = [CELSIUS, FAHRENHEIT, KELVIN]


def find_unit(unit: str) -> tuple[str, float | None]:
    """Ищет величину.
    Принимает название единицы.
    :return: Кортеж (имя_группы, коэффициент). Для температуры коэффициент = None.
    Если единица не найдена, бросает UnknownUnitError.
    """
    name = unit.strip().lower()
    if name in LENGTH_FACTOR:
        return LENGTH, LENGTH_FACTOR[name]
    if name in MASS_FACTOR:
        return MASS, MASS_FACTOR[name]
    if name in TEMPERATURE_NAMES:
        return TEMPERATURE, None
    raise UnknownUnitError()


def convert(value: float | str, from_unit: str, to_unit: str) -> float:
    """Переводит значения. Температура переводится через Кельвины.
    Принимает value - значение, from_unit - исходная единица, to_unit - финальная единица.
    :return: Результат как float.
    Если value не число, бросает InvalidValueError.
    Если есть неизвестная единица, бросает UnknownUnitError.
    Если единицы из разных групп, бросает IncompatibleUnitsError.
    Если температура ниже абсолютного 0, бросает BelowAbsoluteZeroError.
    """
    try:
        val = float(value)
    except (TypeError, ValueError) as exc:
        raise InvalidValueError() from exc
    from_group, from_factor = find_unit(from_unit)
    to_group, to_factor = find_unit(to_unit)
    if to_group != from_group:
        raise IncompatibleUnitsError(from_unit, to_unit)
    if from_group == TEMPERATURE:
        v1, v2 = from_unit.strip().lower(), to_unit.strip().lower()
        val_input = temperature_to_kelvin(val, v1)
        if val_input < 0:
            raise BelowAbsoluteZeroError()
        val_output = temperature_from_kelvin(val_input, v2)
        if temperature_to_kelvin(val_output, v2) < 0:
            raise BelowAbsoluteZeroError()
        return round(float(val_output), 12)
    else:
        assert from_factor is not None
        assert to_factor is not None
        return float(val * from_factor / to_factor)


def temperature_to_kelvin(value: float, unit: str) -> float:
    """Переводит температуру в Кельвины.
    Принимает значение температуры и единицу измерения(c, f, k).
    :return: Значение в Кельвинах.
    Если единица неизвестная, бросает UnknownUnitError.
    """
    if unit == KELVIN:
        return value
    if unit == CELSIUS:
        return value + FROM_CELSIUS_TO_KELVIN
    if unit == FAHRENHEIT:
        return (value + FROM_FAHRENHEIT_TO_KELVIN) * FROM_FAHRENHEIT_CONSTANT
    raise UnknownUnitError()


def temperature_from_kelvin(value: float, unit: str) -> float:
    """Переводит температуру из Кельвинов.
    Принимает значение температуры в Кельвинах и единицу, в которую надо перевести.
    :return: Значение в нужной единице.
    Если единица неизвестная, бросает UnknownUnitError.
    """
    if unit == KELVIN:
        return value
    if unit == CELSIUS:
        return value - FROM_CELSIUS_TO_KELVIN
    if unit == FAHRENHEIT:
        return value * (1 / FROM_FAHRENHEIT_CONSTANT) - FROM_FAHRENHEIT_TO_KELVIN
    raise UnknownUnitError()
