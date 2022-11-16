from typing import Any
from fastapi import APIRouter

from schemas.user import User

router = APIRouter()


@router.post("/login/test-token", response_model=User)
def test_token() -> Any:
    """
    Test access token
    """
    return {
        "email": "test@ddd.com",
        "is_active": True,
        "is_superuser": False,
        "full_name": "test",
        "id": "1000"
    }
