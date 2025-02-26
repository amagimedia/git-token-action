from pydantic import BaseModel
from pydantic import Field

class EVValidator(BaseModel):    
    LOG_LEVEL: str = Field(default="INFO", pattern=r'^(DEBUG|INFO|WARNING|CRITICAL|ERROR)$')    
    GITHUB_APP_ID: int
    GITHUB_APP_INSTALLATION_ID: int
    GITHUB_APP_PRIVATE_KEY: str
    GITHUB_TOKEN_EXPIRY_SECONDS: int = Field(default=300)