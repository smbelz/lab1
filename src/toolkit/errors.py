"""Ошибки калькулятора и конвертера."""


class ToolkitError(Exception):
    """Для всех ошибок toolkit."""

    exit_code = 2


class EmptyExpression(ToolkitError):
    """Ошибка пустого выражения."""

    def __init__(self) -> None:
        """Создаёт ошибку - пустое выражение."""

        super().__init__("Ошибка. Введено пустое выражение.")


class InvalidCharacterError(ToolkitError):
    """Ошибка - недопустимый символ."""

    def __init__(self)  -> None:
        """Создаёт ошибку - недопустимый символ."""

        super().__init__("Ошибка. Введён недопустимый символ.")


class MissingOperandError(ToolkitError):
    """Ошибка пропущенного операнда."""

    def __init__(self) -> None:
        """Создаёт ошибку - пропущенный операнд."""

        super().__init__("Ошибка. В выражении пропущен операнд.")


class DivisionByZeroError(ToolkitError):
    """Ошибка деления на 0."""

    def __init__(self) -> None:
        """Создаёт ошибку - деление на 0."""

        super().__init__("Ошибка. Вы пытаетесь разделить на 0.")


class UnknownOperatorError(ToolkitError):
    """Ошибка неизвестного оператора."""

    def __init__(self) -> None:
        """Создаёт ошибку - неизвестный оператор."""

        super().__init__("Ошибка. Был введён неизвестный оператор.")


class UnknownUnitError(ToolkitError):
    """Ошибка - неизвестная единица измерения."""

    def __init__(self) -> None:
        """Создаёт ошибку - неизвестная единица."""

        super().__init__("Ошибка. Была введена неизвестная единица.")


class IncompatibleUnitsError(ToolkitError):
    """Ошибка - несовместимые единицы."""

    def __init__(self, unit_1, unit_2: str) -> None:
        """Создаёт ошибку - несовместимые единицы."""

        super().__init__(f"Ошибка. Нельзя перевести {unit_1} в {unit_2}.")


class InvalidValueError(ToolkitError):
    """Неверное значение."""

    def __init__(self) -> None:
        """Создаёт ошибку - неверное значение."""
        super().__init__("Ошибка. Введено неверное значение.")


class BelowAbsoluteZeroError(ToolkitError):
    """Температура ниже абсолютного 0."""

    def __init__(self) -> None:
        """Создаёт ошибку - температура ниже абсолютного 0."""

        super().__init__("Ошибка. Температура не должна быть ниже абсолютого 0.")
