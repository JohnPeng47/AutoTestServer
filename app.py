from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import uvicorn
from logging import getLogger

from src.service.auth.routes import router as auth_router
from src.service.fs.routes import router as fs_router

from config import settings

logger = getLogger("base")

app = FastAPI()

# Set up the CORS middleware
origins = [
    "http://localhost:3000",  # Allow requests from your local frontend
    "http://localhost:5900",
    "http://localhost:10559",
    "http://18.221.129.100:8000",
    "http://172.31.32.87:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(fs_router)


# TODO: add linux yaml_config
# with open(settings.LOG_CONFIG, "r") as config_file:
#     yaml_config = yaml.safe_load(config_file.read())

if __name__ == "__main__":
    uvicorn.run("app:app", 
                host="0.0.0.0", 
                port=settings.API_PORT, 
                reload=True) 
                # log_config=yaml_config)
