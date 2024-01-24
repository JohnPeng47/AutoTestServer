from pydantic import BaseModel
from dataclasses import dataclass

@dataclass
class GitCredentials:
    """
    Depending on what kind of git operations we want to perform, we need different credentials.
    """
    pass

class GitRepo(BaseModel):
    # check what kind of credentials we need to perform our operaitons
    credentials: GitCredentials 
    url: str
