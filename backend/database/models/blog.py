from datetime import datetime
from sqlalchemy import (Column, Integer, Text, 
                        String, Boolean, DateTime, ForeignKey)
from sqlalchemy.orm import relationship

from database.base_class import Base


class Blog(Base):
    id = Column(Integer, primary_key = True)
    title = Column(String, nullable = False)
    slug = Column(String, nullable = False)
    content = Column(Text, nullable = False)
    author_id = Column(Integer, ForeignKey("user.id"))
    author = relationship("user", back_populates = "blogs")
    creation_date = Column(DateTime, default = datetime.now)
    is_active = Column(Boolean, default = False)