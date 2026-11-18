import pytest
from pydantic import ValidationError
from app.schemas.base import UserCreate


def test_missing_password_is_rejected():
    data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@example.com",
        "username": "johndoe",
    }

    with pytest.raises(ValidationError, match="Password is required"):
        UserCreate.model_validate(data)