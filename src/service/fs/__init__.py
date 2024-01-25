from pathlib import Path

from src.database.db import DBConnection
from src.database.fs import FileRepoModel

class FileRepo:
    """
    Represents a copy of the user's repo on the server, and is responsible for
    for file operation on the repo
    """
    def __init__(self, 
                 filepath: Path):
        """
        Initializes the FileRepo with the user's local repo for the first time
        """
        pass

    def sync_file_diff(self,
                       diff: str):
        """
        Takes diff and syncs it with the FileRepo location
        """
        pass

class RepoManager:
    """
    Class that manages access to FileRepo. Currently only responsible for creating new and
    getting existing FileRepo objects from the DB FileRepoModel, but in future, will also
    handle authorization checks.
    
    Filepath right now can be arbitrary local path but later may be remote
    """
    def __init__(self, db: DBConnection):
        """
        Initializes the RepoManager with a DBConnection object
        """
        # self.repos = get_repos_from_db()
        pass

    def create_file_repo(self, 
                 github_access_token: str,
                 repo_id: str) -> FileRepo:
        # self._save_repo()
        pass

    def get_file_repo(self, 
                      url: str) -> FileRepo:
        """
        Returns the FileRepo object for the given user_id
        """
        # retrieve from db then convert to FileRepo
        # FileRepoModel.find_one(FileRepoModel.url == url)
        pass

    def _save_repo(self, 
                   github_access_token: str,
                   repo: FileRepo):

        # FileRepoModel(filepath=filepath,
        #               credentials=repo.credentials,
        #               url=repo.url).create()
        """
        Saves the FileRepo object for the given user_id
        """
        pass