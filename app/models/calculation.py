
# app/models/calculation.py

import uuid
from datetime import datetime

from sqlalchemy import Column, String, Float, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.models.user import Base



class Calculation(Base):
    __tablename__ = "calculations"

    __table_args__ = (
        CheckConstraint(
            "type IN ('Add', 'Subtract', 'Multiply', 'Divide')",
            name="ck_calculations_valid_type",
        ),
        CheckConstraint(
            "NOT (type = 'Divide' AND b = 0)",
            name="ck_calculations_no_zero_division",
        ),
    )

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    a = Column(Float, nullable=False)
    b = Column(Float, nullable=False)

    type = Column(String(20), nullable=False)
    result = Column(Float, nullable=True)

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    user = relationship("User")

    def __repr__(self):
        return (
            f"<Calculation("
            f"type={self.type}, "
            f"a={self.a}, "
            f"b={self.b}, "
            f"result={self.result}"
            f")>"
        )
