from fastapi import APIRouter
from src.api.schemas import AnalyzeResponse, AnalyzeRequest
from src.agents.orchastrator import orchastrator
import uuid

router = APIRouter()
graph = orchastrator()

@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze(request: AnalyzeRequest):
    state = {
        "input_text": request.text,
        "requested_tasks": request.tasks,
        "classification": None,
        "sentiment": None,
        "summary": None,
        "request_id": str(uuid.uuid4()),
        "status": "pending",
        "errors": [],
        "completed_tasks": []
    }

    result = await graph.graph.ainvoke(state)
    return AnalyzeResponse(
        request_id=result["request_id"],
                           status=result["status"],
                           classification=result["classification"],
                           sentiment=result["sentiment"],
                           summary=result["summary"],
                           errors=result["errors"],
                           )

@router.get("/agents/status")
async def agents_status():
    return {"message": "This is the agents status endpoint!"}

@router.get("/health")
async def health():
    return {"message": "This is the health endpoint!"}
