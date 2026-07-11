from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from .env"""

    APP_NAME: str = "KAIA - Koha AI Assistant"
    APP_VERSION: str = "0.1.0"
    APP_DESCRIPTION: str = "AI-powered assistant for the Koha Library Management System"

    DEBUG: bool = True

    HOST: str = "127.0.0.1"
    PORT: int = 8000

    # AI Provider
    OPENAI_API_KEY: str = ""
    OPENAI_MODEL: str = "gpt-4o-mini"

    # Koha
    KOHA_BASE_URL: str = ""
    KOHA_USERNAME: str = ""
    KOHA_PASSWORD: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )


settings = Settings()
