from fastapi import FastAPI
from app.api.v1 import users
from app.api.v1 import auth

app = FastAPI()

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])

# Ensure tables are created at startup (dev only)
from app.db.base import Base
from app.db.session import engine
Base.metadata.create_all(bind=engine)
