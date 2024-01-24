from fastapi import APIRouter
from .schema import SyncRepoRequest, SyncRepoResponse

router = APIRouter()

@router.post("/sync")
def sync_local_user_repo(request: SyncRepoRequest) -> SyncRepoResponse:
    print(request.latest_commit)

    return SyncRepoResponse(status="Sync started..")

@router.post("/initialize")
def init_local_user_repo():
    pass