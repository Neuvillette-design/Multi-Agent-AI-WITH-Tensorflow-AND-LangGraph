from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Multi-Agent ML Platform"

    host: str = "0.0.0.0"
    port: int = 8000

    log_level: str = "INFO"

    openai_api_key: str = ""

    classifier_model_path: str = "models/classifier/saved_model"
    sentiment_model_path: str = "models/sentiment/saved_model"

    model_config = {"env_file": ".env", "extra": "ignore"}


settings = Settings()