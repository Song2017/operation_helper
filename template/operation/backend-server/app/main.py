import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.api_v1.api import api_router
from app.core.config import settings

server = FastAPI(
    title=settings.PROJECT_NAME,
    docs_url=f"{settings.API_V1_STR}/docs",
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    server.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

server.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    # uvicorn.run("main:app", host="0.0.0.0", reload=True, port=80)
    uvicorn.run("main:server", host='0.0.0.0', port=8000)
