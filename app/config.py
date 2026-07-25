from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application Settings
    """

    # ============================
    # OpenAI
    # ============================

    OPENAI_API_KEY: str
    OPENAI_MODEL: str = "gpt-4.1"
    OPENAI_TEMPERATURE: float = 0

    # ============================
    # NestJS Backend
    # ============================

    NESTJS_API_URL: str = "http://localhost:5000"

    # ============================
    # MongoDB
    # ============================

    MONGODB_URI: str = "mongodb://admin:NewStrongPassword123@157.180.53.175:27017/admin?authSource=admin&replicaSet=rs0&directConnection=true"

    # ============================
    # Vector Database
    # ============================

    VECTOR_DB_URL: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()