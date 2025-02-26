from pydantic import BaseModel
from pydantic import Field
from pydantic import ConfigDict

class EVValidator(BaseModel):    
    LOG_LEVEL: str = Field(default="INFO", pattern=r'^(DEBUG|INFO|WARNING|CRITICAL|ERROR)$')    
    GITHUB_APP_ID: int
    GITHUB_APP_INSTALLATION_ID: int
    GITHUB_PRIVATE_KEY: str = Field(pattern=r'-----BEGIN (RSA|EC|DSA|OPENSSH) PRIVATE KEY-----\n([A-Za-z0-9+/=\n]+)\n-----END (RSA|EC|DSA|OPENSSH) PRIVATE KEY-----')
    GITHUB_TOKEN_EXPIRY_SECONDS: int = Field(default=300)
    
    model_config = ConfigDict(extra="forbid")