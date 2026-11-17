
import pytest
from pydantic import ValidationError

from app.calculation_factory import CalculationFactory
from app.schemas.calculation import CalculationCreate


@pytest.mark.parametrize(
    "operation, expected",
    [
        ("Add", 12.0),
        ("Subtract", 8.0),
        ("Multiply", 20.0),
        ("Divide", 5.0),
    ],
)
def test_calculation_operations(operation, expected):
    data = CalculationCreate(a=10, b=2, type=operation)
    result = CalculationFactory.calculate(data)
    assert result == expected


def test_division_by_zero():
    with pytest.raises(ValidationError):
        CalculationCreate(a=10, b=0, type="Divide")


def test_invalid_operation():
    with pytest.raises(ValidationError):
        CalculationCreate(a=10, b=2, type="Power")


def test_missing_input():
    with pytest.raises(ValidationError):
        CalculationCreate(a=10, type="Add")


@pytest.mark.parametrize(
    "invalid_value",
    [
        float("nan"),
        float("inf"),
        float("-inf"),
    ],
)
def test_invalid_numeric_values(invalid_value):
    with pytest.raises(ValidationError):
        CalculationCreate(
            a=invalid_value,
            b=2,
            type="Add"
        )


def test_zero_divisor_with_float():
    with pytest.raises(ValidationError):
        CalculationCreate(
            a=10,
            b=0.0,
            type="Divide"
        )
