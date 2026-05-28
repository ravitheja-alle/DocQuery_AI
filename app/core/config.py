from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "Headless Document Intelligence API"
    VERSION: str = "1.0.0"
    
    # Database configuration
    DATABASE_URL: str
    
    # OpenAI configuration
    OPENAI_API_KEY: str
    
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()