from fastapi import FastAPI, Response, status
from typing import Optional
from enum import Enum
from fastapi import APIRouter

router = APIRouter(prefix="/blog", tags=["blog"])


class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"


@router.get("/all",
            summary="Retrieve all blogs",
            description="This api call simulate retrieve all blogs",
            response_description="The list of available blogs")
async def get_all_blogs(page=1, page_size: Optional[int] = None):
    return {"message": f"All {page} Blogs with page size {page_size}"}


@router.get("/{id}/comments/{comment_id}/", tags=["comment"])
async def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    """
    Simulates retrieving comment of a blogs
    - **id** mandatory parameter
    - **comment_id** mandatory parameter
    - **valid** (Optional): bool variable
    - **username** (optional): str variable
    """
    return {"message": f"blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}"}


@router.get("/type/{type}")
async def get_blog_type(type: BlogType):
    return {"message": f"Returning blog type : {type}"}


@router.get('/{id}', status_code=status.HTTP_200_OK)
async def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"Blog With {id} Not Found"}
    else:
        response.status_code = status.HTTP_200_OK
        return {"message": f"Blog with id {id}"}
