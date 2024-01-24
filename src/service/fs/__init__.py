from src.database.db import DBConnection

class FileRepo:
    """
    This represents the server copy of a user's Git Repo, and contains
    all methods required to access and modify the repo. Once initialized, this object
    must be kept in sync with the user's local repo on a commit by commit basis
    """
    def __init__(self):
        """
        Initializes the FileRepo with the user's local repo for the first time
        """
        pass

    def run_test():
        pass

class RepoManager:
    """
    Class that manages access to FileRepo. Checks 
    """
    def __init__(self, db: DBConnection):
        """
        Initializes the RepoManager with a DBConnection object
        """
        # self.repos = get_repos_from_db()
        pass

    def get_repo(self, user_id) -> FileRepo:
        """
        Returns the FileRepo object for the given user_id
        """
        pass

    def save_repo(self, user_id, repo: FileRepo):
        """
        Saves the FileRepo object for the given user_id
        """
        pass