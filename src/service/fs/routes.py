from fastapi import APIRouter, HTTPException, status, Depends, Body
from .schema import SyncRepoRequest, SyncRepoResponse

router = APIRouter()

@router.post("/sync")
def sync_local_user_repo(request: SyncRepoRequest) -> SyncRepoResponse:
    print(request)

    return SyncRepoResponse(status="ok")