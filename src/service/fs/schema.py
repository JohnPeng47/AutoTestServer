from pydantic import BaseModel

class SyncRepoRequest(BaseModel):
    latest_commit: str

class SyncRepoResponse(BaseModel):
    status: str

class InitRepoRequest(BaseModel):
    repo_url: str
    github_access_token: str
