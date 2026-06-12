from pydantic import BaseModel
from typing import List

class AnalyzeRequest(BaseModel):
    text: str
    tasks: List[str]

class AnalyzeResponse(BaseModel):
    request_id: str
    status: str
    classification: dict | None = None
    sentiment: dict | None = None
    summary: str | None = None
    errors: list[str] = []