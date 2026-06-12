from src.agents.state import AgentState

class ClassifierAgent:
    async def __call__ (self, state: AgentState) -> dict:
        # The state is passed in, but we only return the fields we have updated
        # to avoid conflicts during parallel execution.
        return {
            "classification": {
                "label": "Technology",
                "confidence": 0.99
            },
            "completed_tasks": ["classifier"]
        }