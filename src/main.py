from fastapi import FastAPI, Response, status
from typing import Optional
from enum import Enum

app = FastAPI()


class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"


@app.get("/health", tags=["health"])
def health():
    return {"message": "FastAPI app is running..."}


@app.get("/blog/all",
         tags=["blog"],
         summary="Retrieve all blogs",
         description="This api call simulate retrieve all blogs",
         response_description="The list of available blogs")
def get_all_blogs(page=1, page_size: Optional[int] = None):
    return {"message": f"All {page} Blogs with page size {page_size}"}


@app.get("/blog/{id}/comments/{comment_id}/", tags=["blog", "comment"])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    """
    Simulates retrieving comment of a blogs
    - **id** mandatory parameter
    - **comment_id** mandatory parameter
    - **valid** (Optional): bool variable
    - **username** (optional): str variable
    """
    return {"message": f"blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}"}


@app.get("/blog/type/{type}", tags=["blog"])
def get_blog_type(type: BlogType):
    return {"message": f"Returning blog type : {type}"}


@app.get('/blog/{id}', status_code=status.HTTP_200_OK, tags=['blog'])
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"Blog With {id} Not Found"}
    else:
        response.status_code = status.HTTP_200_OK
        return {"message": f"Blog with id {id}"}
