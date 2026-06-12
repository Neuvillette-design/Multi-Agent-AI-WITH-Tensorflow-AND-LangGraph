from src.models.registry import registry

class SentimentAgent:
    async def execute(self, text: str):
        prediction = registry.sentiment.predict(text)

        return prediction