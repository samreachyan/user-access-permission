from fastapi import APIRouter, Depends, HTTPException, Request, Form
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, ResponseModel
from app.models.user import User
from app.core.security import get_password_hash, verify_password, create_access_token
from app.utils.response import api_response, get_language
from app.api.deps import get_db

router = APIRouter()

@router.post("/register", response_model=ResponseModel)
def register(user: UserCreate, request: Request, db: Session = Depends(get_db)):
    lang = get_language(request)
    existing = db.query(User).filter(User.username == user.username).first()
    if existing:
        return api_response(False, "bad_request", lang, error_code="user_exists")
    db_user = User(username=user.username, hashed_password=get_password_hash(user.password), role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    access_token = create_access_token(data={"sub": db_user.username, "role": db_user.role.value})
    return api_response(True, "user_created", lang, data={"access_token": access_token, "token_type": "bearer"})

@router.post("/login")
def login(
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
):
    db_user = db.query(User).filter(User.username == username).first()
    if not db_user or not verify_password(password, db_user.hashed_password):
        # Return error in the requested language
        from app.utils.response import get_message
        raise HTTPException(status_code=401, detail=get_message("unauthorized"))
    access_token = create_access_token(data={"sub": db_user.username, "role": db_user.role.value})
    return {"access_token": access_token, "token_type": "bearer"}
