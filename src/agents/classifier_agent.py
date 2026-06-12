from src.models.registry import registry

class ClassifierAgent:
    async def execute(self, text: str):
        
        prediction = registry.classifier.predict(text)
        return prediction