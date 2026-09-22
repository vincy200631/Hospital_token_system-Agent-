from datetime import datetime

from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.agent.tools import book_token

from app.schemas.token_schema import TokenRequest


router = APIRouter(
    prefix="/tokens",
    tags=["Tokens"]
)


@router.post("/book")
def create_token(
    request: TokenRequest,
    db: Session = Depends(get_db)
):

    appointment_date = datetime.strptime(
        request.appointment_date,
        "%Y-%m-%d"
    ).date()

    appointment_time = datetime.strptime(
        request.appointment_time,
        "%H:%M"
    ).time()

    token = book_token(
        db=db,
        patient_name=request.patient_name,
        doctor_id=request.doctor_id,
        appointment_date=appointment_date,
        appointment_time=appointment_time
    )

    return {
        "message": "Token booked successfully",
        "token_number": token.token_number,
        "patient": token.patient_name,
        "date": str(token.appointment_date),
        "time": str(token.appointment_time)
    }