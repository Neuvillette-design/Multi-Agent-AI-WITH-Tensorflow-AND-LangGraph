from fastapi import APIRouter
from .schemas import AnalyzeResponse, AnalyzeRequest
import uuid

router = APIRouter()

router.post("/analyze", response_model=AnalyzeResponse)
async def analyze(request: AnalyzeRequest):

    return AnalyzeResponse(request_id=str(uuid.uuid4()),
                           message="Request received successfully.",
                           requested_tasks=request.tasks)

@router.get("/agents/status")
async def agents_status():
    return {"message": "This is the agents status endpoint!"}

@router.get("/health")
async def health():
    return {"message": "This is the health endpoint!"}
