Our repository is setup as follows:

## Services: 
These are all of our external facing endpoints, including those that we use to interact with the client. The structure of a service folder is broken into the following:

### Routes:
- these define the external endpoints (ie. service/fs/routes.py::sync_local_user_repo) and is the entrypoint for the FastAPI webserver to handle an incoming request. 
### Schema:
- these define the service specific models for each service. For instance right now, each service has their request and response models defined inside the schema file
## Shared:
Code (generally, tasks) that are shared amongst the different services are implemented here

## Goals for Capstone:
- finish the /init route from service/fs that initiates a process to acquire access credentials to the user's Github. It then initializes clones the repository to a location on the server, and saves the credentials and filepath to a FileRepoModel object. The creation of a FileRepoModel is done through the RepoManager

- finish the /sync route from service/fs that syncs a local user repo with our remote cloned from the step before. This route will accept a diff file that marks the changes made between the last sync and now. Assume for now that the difference between the local and the remote file is at most one commit. Required for this is also the post-commit hook (in the test_repo/.git folder), which calls post-commit.py which uploads to the server the commit diff

