from fastapi import FastAPI, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from src.database import SessionLocal, engine, Base
from src.models import BlogPost
from src.auth import verify_google_token
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/posts/")
async def create_post(request: Request,db: Session=Depends(get_db)):
    data = await request.json()
    token = data.get("token")
    user_info = verify_google_token(token)

    post = BlogPost(
        title=data["title"],
        content=data["content"],
        author=user_info["email"]
    )
    
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

@app.get("/posts/")
def get_posts(db: Session=Depends(get_db)):
    return db.query(BlogPost).order_by(BlogPost.created_at.desc()).all()
