from sqlalchemy.orm import Session

from database.repository.blog import create_new_blog
from schemas.blog import CreateBlog
from tests.utils.user import create_random_user


def create_random_blog(db: Session):
    create_blog = CreateBlog(
        title = "first_blog",
        slug = "",
        content = "Tests make the system stable!",
        is_active = 1
        )
    user = create_random_user(db = db)
    blog = create_new_blog(
        blog = create_blog,
        db = db,
        author_id = user.id
        )
    return blog