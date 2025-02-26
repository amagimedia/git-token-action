from typing import Dict
import requests, logging, jwt, time
from utilities.datetimeutility import get_current_timestamp, add_time_to_timestamp

logger = logging.getLogger(__name__)

class GitApis:
    def __init__(self, private_key, app_id, app_installation_id, token_expiry_seconds=300) -> None:
        self.private_key=private_key
        self.app_id=app_id
        self.app_installation_id=app_installation_id
        self.token_expiry_seconds=token_expiry_seconds
        self.TOKEN_EXPIRY=None
        self.GIT_TOKEN=None

    
    def generate_jwt_token(self, token_expiry_seconds) -> str:
        """Generate a JWT token using the private key.

        Args:
            token_expiry_seconds (int): JWT Token expiry time in seconds
            
        Returns:
            (str) encoded jwt token
        """
        logger.debug("Generating JWT Token ...")
        private_key = self.private_key.replace("\\n", "\n")
        signing_key: jwt.AbstractJWKBase = jwt.jwk_from_pem(
            private_key.encode("utf-8")
        )

        payload: Dict = {
            "iat": int(time.time()),
            "exp": int(time.time()) + token_expiry_seconds,
            "iss": self.app_id,
        }
        jwt_instance: jwt.JWT = jwt.JWT()
        
        return jwt_instance.encode(payload, signing_key, alg="RS256")


    def generate_access_token(self, jwt_token: str) -> str:
        """Generate a installation access token.

        Args:
            jwt_token (str) : JWT token generated using the private key            

        Returns:
            (str) installation access token
        """
        response = requests.post(
            f"https://api.github.com/app/installations/{self.app_installation_id}/access_tokens",
            headers={
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {jwt_token}",
                "X-Github-Api-Version": "2022-11-28",
            },
            timeout=10,
        )

        return response.json()['token']
    

    def get_token(self):
        current_timestamp=get_current_timestamp()
        if self.TOKEN_EXPIRY==None or self.TOKEN_EXPIRY<current_timestamp:
            jwt_token = self.generate_jwt_token(token_expiry_seconds=self.token_expiry_seconds)            
            self.TOKEN_EXPIRY = add_time_to_timestamp(current_timestamp=current_timestamp, time_to_add=self.token_expiry_seconds)
            self.GIT_TOKEN = self.generate_access_token(jwt_token=jwt_token)

        return self.GIT_TOKEN