"""Константы."""

DIGITS: str = "1234567890"
EXIT_OK: int = 0
EXIT_ERROR: int = 2
FROM_CELSIUS_TO_KELVIN: float = 273.15
FROM_CELSIUS_TO_FAHRENHEIT: float = 32.0
FROM_FAHRENHEIT_TO_KELVIN: float = 459.67
FROM_FAHRENHEIT_CONSTANT: float = 5.0 / 9.0
CELSIUS: str = "c"
FAHRENHEIT: str = "f"
KELVIN: str = "k"
MASS: str = "mass"
LENGTH: str = "length"
TEMPERATURE: str = "temperature"
NUMBER: str = "number"
PLUS: str = "plus"
MINUS: str = "minus"
STAR: str = "star"
SLASH: str = "slash"
OPERATORS: list[str] = [PLUS, MINUS, STAR, SLASH]
BINARY_OPERATORS: list[str] = [STAR, SLASH]
CHAR: dict = {"+": PLUS, "-": MINUS, "*": STAR, "/": SLASH}
