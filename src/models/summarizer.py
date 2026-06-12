from src.models.base import BaseModel

class SummarizerModel(BaseModel):
    def predict(self, text: str):

        return {
            "This is the summary!"
        }