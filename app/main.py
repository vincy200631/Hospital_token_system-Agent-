from fastapi import FastAPI

from app.database.connection import Base, engine
from app.routes.token_routes import router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Hospital Token AI Agent"
)


app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Hospital Token AI Agent is running"
    }