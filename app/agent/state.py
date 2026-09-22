from typing import TypedDict


class AgentState(TypedDict, total=False):

    user_message: str

    patient_name: str

    doctor_name: str

    specialization: str

    appointment_date: str

    appointment_time: str

    token_number: int

    response: str