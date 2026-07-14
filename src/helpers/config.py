from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str

    FILE_ALLOWED_TYPES: list
    FILE_MAX_SIZE: int
    FILE_DEFAULT_CHUNK_SIZE: int

    MONGODB_URL: str
    MONGODB_DATABASE: str

    class Config:
        env_file =".env"
        # مهمت هذا الكلاس يحمل كل شي موجود في دوت انف ويتحول لكلاس اقدر استخدمو

def get_settings():
    return Settings()
# يرجع اوبجيكتس من كلاس السيتنغز
# singlton