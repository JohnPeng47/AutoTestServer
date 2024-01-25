from pydantic import BaseModel
from dataclasses import dataclass
from beanie import Document

@dataclass
class GitCredentials:
    """
    Depending on what kind of git operations we want to perform, we need different credentials.
    """
    pass

class FileRepoModel(Document):
    filepath: str
    credentials: GitCredentials 
    url: str