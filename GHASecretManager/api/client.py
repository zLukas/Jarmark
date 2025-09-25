from github import Github
from github import Auth
import os


def login(token: str) -> Github:
    # using an access token
    if not token:
        raise ValueError("GitHub token must be provided.")
    auth = Auth.Token(token)
    g = Github(auth=auth)
    try:
        g.get_user().login  # Test the authentication
    except Exception as e:
        raise ValueError("Failed to authenticate with GitHub. Check your token.") from e
    return g
