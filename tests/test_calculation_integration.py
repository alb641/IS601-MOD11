
import pytest

from app.models.calculation import Calculation
from app.calculation_factory import CalculationFactory
from app.schemas.calculation import CalculationCreate
from sqlalchemy.exc import IntegrityError


def test_save_and_retrieve_calculation(db_session):
    # Arrange: validate input and calculate the result
    data = CalculationCreate(a=10, b=2, type="Divide")
    result = CalculationFactory.calculate(data)

    # Act: save the calculation to PostgreSQL
    calculation = Calculation(
        a=data.a,
        b=data.b,
        type=data.type.value,
        result=result,
    )

    db_session.add(calculation)
    db_session.commit()

    calculation_id = calculation.id

    # Clear cached objects so the next query reads from the DB
    db_session.expunge_all()

    # Retrieve the saved calculation
    saved_calculation = db_session.get(Calculation, calculation_id)

    # Assert: verify the stored data
    assert saved_calculation is not None
    assert saved_calculation.a == 10.0
    assert saved_calculation.b == 2.0
    assert saved_calculation.type == "Divide"
    assert saved_calculation.result == 5.0


@pytest.mark.parametrize(
    "operation, expected",
    [
        ("Add", 12.0),
        ("Subtract", 8.0),
        ("Multiply", 20.0),
        ("Divide", 5.0),
    ],
)
def test_persist_all_operations(db_session, operation, expected):
    data = CalculationCreate(a=10, b=2, type=operation)

    calculation = Calculation(
        a=data.a,
        b=data.b,
        type=data.type.value,
        result=CalculationFactory.calculate(data),
    )

    db_session.add(calculation)
    db_session.commit()

    calculation_id = calculation.id
    db_session.expunge_all()

    saved = db_session.get(Calculation, calculation_id)

    assert saved is not None
    assert saved.type == operation
    assert saved.result == expected


def test_calculation_belongs_to_user(db_session, test_user):
    calculation = Calculation(
        a=15,
        b=5,
        type="Subtract",
        result=10,
        user_id=test_user.id,
    )

    db_session.add(calculation)
    db_session.commit()
    db_session.refresh(calculation)

    assert calculation.user_id == test_user.id
    assert calculation.user is not None
    assert calculation.user.id == test_user.id


@pytest.mark.parametrize(
    "operation, a, b",
    [
        ("Power", 10, 2),
        ("Divide", 10, 0),
    ],
)
def test_database_rejects_invalid_calculations(
    db_session, operation, a, b
):
    calculation = Calculation(
        a=a,
        b=b,
        type=operation,
        result=0,
    )

    db_session.add(calculation)

    with pytest.raises(IntegrityError):
        db_session.commit()

    # Restore the session after the expected database error
    db_session.rollback()