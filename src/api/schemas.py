from pydantic import BaseModel
from typing import List

class AnalyzeRequest(BaseModel):
    texts: str
    tasks: List[str]

class AnalyzeResponse(BaseModel):
    request_id: str
    message: str
    requested_tasks: List[str]