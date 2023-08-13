from fastapi import FastAPI
from typing import Optional
from enum import Enum

app = FastAPI()


@app.get("/health")
def health():
    return {"message": "FastAPI app is running..."}


@app.get("/blog/all")
def get_all_blogs(page=1, page_size: Optional[int] = None):
    return {"message": f"All {page} Blogs with page size {page_size}"}


class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"


@app.get("/blog/type/{type}")
def get_blog_type(type: BlogType):
    return {"message": f"Returning blog type : {type}"}


@app.get('/blog/{id}')
def get_blog(id: int):
    return {"message": f"Blog with id {id}"}


