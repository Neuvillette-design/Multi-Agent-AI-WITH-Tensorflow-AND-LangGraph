from typing import Optional, TypedDict, Annotated
import operator

class AgentState(TypedDict):
    input_text: str
    requested_tasks: list[str]
    classification: Optional[dict]
    sentiment: Optional[dict]
    summary: Optional[str]
    request_id: str
    status: str
    errors: list[str]
    completed_tasks: Annotated[list[str], operator.add]