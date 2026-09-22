from datetime import datetime

from sqlalchemy.orm import Session

from app.database.models import Doctor, Token


def get_doctors(
    db: Session,
    specialization: str | None = None
):
    query = db.query(Doctor)

    if specialization:
        query = query.filter(
            Doctor.specialization.ilike(
                f"%{specialization}%"
            )
        )

    return query.all()


def get_next_token(
    db: Session,
    doctor_id: int,
    appointment_date
):

    last_token = (
        db.query(Token)
        .filter(
            Token.doctor_id == doctor_id,
            Token.appointment_date == appointment_date
        )
        .order_by(Token.token_number.desc())
        .first()
    )

    if last_token:
        return last_token.token_number + 1

    return 1


def book_token(
    db: Session,
    patient_name: str,
    doctor_id: int,
    appointment_date,
    appointment_time
):

    token_number = get_next_token(
        db,
        doctor_id,
        appointment_date
    )

    token = Token(
        patient_name=patient_name,
        doctor_id=doctor_id,
        appointment_date=appointment_date,
        appointment_time=appointment_time,
        token_number=token_number,
        status="booked"
    )

    db.add(token)

    db.commit()

    db.refresh(token)

    return token


def get_patient_token(
    db: Session,
    patient_name: str
):

    return (
        db.query(Token)
        .filter(
            Token.patient_name == patient_name,
            Token.status == "booked"
        )
        .order_by(Token.id.desc())
        .first()
    )


def cancel_token(
    db: Session,
    patient_name: str
):

    token = get_patient_token(
        db,
        patient_name
    )

    if not token:
        return None

    token.status = "cancelled"

    db.commit()

    return token