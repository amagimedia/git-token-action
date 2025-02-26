# Welcome to Amagi Git token Action!

Amagi Git Token Action let's you get github token and set it in the current running environment as masked secret.

# Dependencies

In order to work with this Github Actions, you require Github App to be installed on all the repos including this one.

# Inputs for running
- Github App ID
- Github App Installation ID
- Github App Private Key
- Log Level

# Output of execution
- Returns a Github token which is masked and injected to the current environment.
- It can be referenced as `AMAGI_GITHUB_TOKEN`

