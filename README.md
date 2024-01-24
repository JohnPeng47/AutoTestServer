Our repository is setup as follows:

## 1.Services: 
These are all of our external facing endpoints, including those that we use to interact with the client. The structure of a service folder is broken into the following:

### a.Routes:
- these define the external endpoints (ie. service/fs/routes.py::sync_local_user_repo) and is the entrypoint for the FastAPI webserver to handle an incoming request. 
### b.Schema:
- these define the service specific models for each service. For instance right now, each service has their request and response models defined inside the schema file

## 2.Shared:
Code (generally, tasks) that are shared amongst the different services are implemented here


