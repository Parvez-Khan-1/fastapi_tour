from fastapi import APIRouter

router = APIRouter(prefix="/blog", tags=["blog"])


@router.post("/new")
async def create_blog():
    pass
