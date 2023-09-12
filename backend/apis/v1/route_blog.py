from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from typing import List

from database.session import get_database
from schemas.blog import ShowBlog, CreateBlog, UpdateBlog
from database.repository.blog import (create_new_blog, retreive_blog, 
                                      list_blogs, update_a_blog, delete_the_blog)

router = APIRouter()


@router.post("/blogs", response_model = ShowBlog, status_code = status.HTTP_201_CREATED)
def create_blog(blog: CreateBlog, db: Session = Depends(get_database)):
    blog = create_new_blog(blog = blog, db = db, author_id = 1)
    return blog

@router.get("/blog/{id}", response_model = ShowBlog)
def get_blog(id: int, db: Session = Depends(get_database)):
    blog = retreive_blog(id = id, db = db)
    if not blog:
        raise HTTPException(detail = f"Blog with ID {id} does not exist.", status_code=status.HTTP_404_NOT_FOUND)
    return blog

@router.get("/blogs", response_model = List[ShowBlog])
def get_all_blogs(db: Session = Depends(get_database)):
    blogs = list_blogs(db = db)
    return blogs

@router.put("/blog/{id}", response_model= ShowBlog)
def update_blog(id: int, blog: UpdateBlog,  db: Session = Depends(get_database)):
    blog = update_a_blog(id = id, blog = blog, author_id = 1, db = db)
    if not blog:
        raise HTTPException(detail = f"Blog with id {id} does not exist")
    return blog


@router.delete("/delete_blog/{id}")
def delete_blog(id: int, db: Session = Depends(get_database)):
    message = delete_the_blog(id = id, author_id = 1,db = db)
    if message.get("error"):
        raise HTTPException(detail = message.get("error"), status_code = status.HTTP_400_BAD_REQUEST)
    return {"msg":f"Successfully deleted blog with id {id}"}
