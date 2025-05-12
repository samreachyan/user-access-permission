from fastapi import Request
from app.core.messages import get_message
from app.schemas.user import ResponseModel

def api_response(success: bool, key: str, lang: str = "en", data=None, error_code=None):
    return ResponseModel(
        success=success,
        message=get_message(key, lang),
        data=data,
        error_code=error_code
    )

def get_language(request: Request):
    lang = request.headers.get("accept-language", "en").lower()
    if lang not in ["en", "km", "vn"]:
        lang = "en"
    return lang
