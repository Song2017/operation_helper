from fastapi import APIRouter

# from server.api.api_v1.endpoints import items, login, users, utils
from api.api_v1.endpoints import login, operation_info, sms_authentication

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(operation_info.router, prefix="/operation", tags=["operation info"])
api_router.include_router(sms_authentication.router, prefix="/sms-authentication", tags=["SMS authentication"])
# api_router.include_router(users.router, prefix="/users", tags=["users"])
# api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
# api_router.include_router(items.router, prefix="/items", tags=["items"])
