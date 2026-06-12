from src.models.classifier import TextClassifier
from src.models.sentiment import SentimentModel
from src.models.summarizer import SummarizerModel

class ModelRegistry:

    def __init__ (self):

        self.classifier = TextClassifier()
        self.sentiment = SentimentModel()
        self.summarizer = SummarizerModel()

registry = ModelRegistry()