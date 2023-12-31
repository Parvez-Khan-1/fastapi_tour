from routers import blog_get, blog_post, user
from fastapi import FastAPI
from db import models
from db.database import engine


app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)


@app.get("/health", tags=["health"])
async def health():
    return {"message": "FastAPI app is running..."}

models.Base.metadata.create_all(engine)