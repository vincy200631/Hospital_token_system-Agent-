from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey

from app.database.connection import Base


class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    specialization = Column(String, nullable=False)

    available_time = Column(String, nullable=False)


class Token(Base):
    __tablename__ = "tokens"

    id = Column(Integer, primary_key=True, index=True)

    patient_name = Column(String, nullable=False)

    doctor_id = Column(Integer, ForeignKey("doctors.id"))

    appointment_date = Column(Date, nullable=False)

    appointment_time = Column(Time, nullable=False)

    token_number = Column(Integer, nullable=False)

    status = Column(String, default="booked")