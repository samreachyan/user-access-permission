from fastapi import APIRouter, Depends, Request
from app.api.deps import require_role
from app.utils.response import api_response, get_language

router = APIRouter()

@router.get("/admin-only")
def admin_only(request: Request, user=Depends(require_role(["admin"]))):
    lang = get_language(request)
    return api_response(True, "Admin access granted.", lang)

@router.get("/manager-or-admin")
def manager_or_admin(request: Request, user=Depends(require_role(["admin", "manager"]))):
    lang = get_language(request)
    return api_response(True, "Manager or Admin access granted.", lang)

@router.get("/user-access")
def user_access(request: Request, user=Depends(require_role(["admin", "manager", "user"]))):
    lang = get_language(request)
    return api_response(True, "User access granted.", lang)
