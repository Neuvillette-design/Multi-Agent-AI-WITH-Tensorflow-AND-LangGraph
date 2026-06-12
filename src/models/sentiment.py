from src.models.base import BaseModel

class SentimentModel(BaseModel):
    def predict(self, text: str):
        return {
            "label": "Positive",
            "confidence": 0.97
        }