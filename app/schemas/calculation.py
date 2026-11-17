
# app/schemas/calculation.py

import uuid
from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, model_validator


class CalculationType(str, Enum):
    Add = "Add"
    Subtract = "Subtract"
    Multiply = "Multiply"
    Divide = "Divide"


class CalculationCreate(BaseModel):
    a: float = Field(allow_inf_nan=False)
    b: float = Field(allow_inf_nan=False)
    type: CalculationType

    @model_validator(mode="after")
    def validate_calculation(self):
        if self.type == CalculationType.Divide and self.b == 0:
            raise ValueError("Cannot divide by zero")
        return self


class CalculationRead(CalculationCreate):
    id: uuid.UUID
    result: Optional[float] = None

    model_config = ConfigDict(from_attributes=True)
