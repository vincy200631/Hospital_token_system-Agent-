from pydantic import BaseModel


class TokenRequest(BaseModel):

    patient_name: str

    doctor_id: int

    appointment_date: str

    appointment_time: str