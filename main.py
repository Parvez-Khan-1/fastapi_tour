from routers import blog_get, blog_post
from fastapi import FastAPI
from src.db import models
from src.db.database import engine


app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get("/health", tags=["health"])
async def health():
    return {"message": "FastAPI app is running..."}

models.Base.metadata.create_all(engine)