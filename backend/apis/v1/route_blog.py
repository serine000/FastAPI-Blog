from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session


from database.session import get_database
from schemas.blog import ShowBlog, CreateBlog
from database.repository.blog import create_new_blog, retreive_blog

router = APIRouter()


@router.post("/blogs", response_model = ShowBlog, status_code = status.HTTP_201_CREATED)
async def create_blog(blog: CreateBlog, db: Session = Depends(get_database)):
    blog = create_new_blog(blog = blog, db = db, author_id = 1)
    return blog

@router.get("/blog/{id}", response_model = ShowBlog)
def get_blog(id: int, db: Session= Depends(get_database)):
    blog = retreive_blog(id=id, db=db)
    if not blog:
        raise HTTPException(detail=f"Blog with ID {id} does not exist.", status_code=status.HTTP_404_NOT_FOUND)
    return blog