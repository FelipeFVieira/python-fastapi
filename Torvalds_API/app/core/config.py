from pydantic import BaseSettings

class Settings(BaseSettings):
    sender_email: str
    sender_password: str
    debug: bool = False
    
    class Config:
        env_file = None

settings = Settings()       
