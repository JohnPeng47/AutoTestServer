from pydantic import BaseModel

class SyncRepoRequest(BaseModel):
    latest_commit: str

class SyncRepoResponse(BaseModel):
    status: str