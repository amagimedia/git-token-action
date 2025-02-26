import logging
import os

from utilities.ev_validator import EVValidator
from utilities.get_token import GitApis


logger = logging.getLogger(__name__)

if __name__=="__main__":
    ev_configs={}    
    for key, value in os.environ.items():
        if key.startswith("GITHUB_") or key.startswith("LOG_LEVEL"):
            ev_configs[key]=value
    
    ev_values=EVValidator(**ev_configs)

    git = GitApis(
        private_key=ev_values.GITHUB_APP_PRIVATE_KEY, 
        app_id=ev_values.GITHUB_APP_ID, 
        app_installation_id=ev_values.GITHUB_APP_INSTALLATION_ID, 
        token_expiry_seconds=ev_values.GITHUB_TOKEN_EXPIRY_SECONDS
    )

    token = git.get_token()

    if not token:
        print("❌ Failed to retrieve GitHub token")
        exit(1)

    # Ensure GitHub Actions Environment File Exists
    github_env_path = os.getenv("GITHUB_ENV", "/github_env")

    # Inject Token into Runner Environment
    with open(github_env_path, "a") as env_file:
        env_file.write(f"AMAGI_GITHUB_TOKEN={token}\n")

    # Mask Token in Logs
    print(f"::add-mask::{token}")

    print("✅ GitHub Token successfully injected and masked.")