from src.agents.state import AgentState

class SummarizerAgent:
    async def __call__ (self, state: AgentState) -> dict:
        # The state is passed in, but we only return the fields we have updated
        # to avoid conflicts during parallel execution.
        # Note: The original code returned a set for summary, which is incorrect.
        # The schema expects a string.
        return {
            "summary": "This is a dummy summary.",
            "completed_tasks": ["summarizer"]
        }