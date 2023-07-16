from fastapi import FastAPI
from pydantic import BaseModel
from loguru import logger


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


class JobPayload(BaseModel):
    job_name: str
    job_start_time: str


@app.post("/monitor/job")
async def root(job_payload:JobPayload) -> JobPayload:
    logger.info(job_payload.dict())
    return job_payload.dict()