from fastapi import FastAPI
from routers import blog_get, blog_post


app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get("/health", tags=["health"])
async def health():
    return {"message": "FastAPI app is running..."}


