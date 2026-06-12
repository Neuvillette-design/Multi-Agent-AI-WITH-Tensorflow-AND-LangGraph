from langgraph.graph import START, END, StateGraph
from langgraph.types import Send
from src.agents.state import AgentState
from src.agents.classifier_agent import ClassifierAgent
from src.agents.sentiment_agent import SentimentAgent
from src.agents.summarizer_agent import SummarizerAgent
from src.models.registry import registry

class orchastrator:
    def __init__(self):
        self.classifier = ClassifierAgent()
        self.summarizer = SummarizerAgent()
        self.sentiment = SentimentAgent()

        self.graph = self.build()

    async def orchastrator_node(self, state: AgentState,) -> AgentState:
        state["status"] = "processing"

        return state
    
    async def classifier_node(state):
        prediction = registry.classifier.predict(state["input_text"])

        return {
            "classification": prediction,
            "completed_tasks": ["classifier"]
        }
    
    async def sentiment_node(state):

        prediction = registry.sentiment.predict(state["input_text"])

        return {
            "Sentiment": prediction,
            "completed_tasks": ["sentiment"]
        }
    
    async def aggregator_node(self, state: AgentState,) -> AgentState:

        state["status"] = "completed"

        return state
    
    def build(self):

        workflow = StateGraph(AgentState)

        workflow.add_node("orchastrator", self.orchastrator_node)
        workflow.add_node("classifier", self.classifier)
        workflow.add_node("sentiment", self.sentiment)
        workflow.add_node("summarizer", self.summarizer)
        workflow.add_node("aggregator", self.aggregator_node)

        workflow.add_edge(START, "orchastrator")
        workflow.add_conditional_edges("orchastrator", self.route_tasks)
        
        workflow.add_edge("classifier", "aggregator")
        workflow.add_edge("sentiment", "aggregator")
        workflow.add_edge("summarizer", "aggregator")
        workflow.add_edge("aggregator", END)

        return workflow.compile()
    
    def route_tasks(self, state: AgentState):

        sends = []

        if "classify" in state["requested_tasks"]:
            sends.append(Send("classifier", state))

        if "sentiment" in state["requested_tasks"]:
            sends.append(Send("sentiment", state))

        if "summarize" in state["requested_tasks"]:
            sends.append(Send("summarizer", state))

        return sends