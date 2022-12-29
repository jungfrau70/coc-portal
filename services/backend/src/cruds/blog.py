from sqlalchemy.orm import Session
from cruds import models
from routers import schemas
from fastapi import HTTPException,status

Model = models.Blog
Schema = schemas.ShowBlog

def get_all(db: Session):
    blogs = db.query(Model).all()
    return blogs

def create(request: Schema,db: Session):
    new_blog = Model(title=request.title, body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id:int,db: Session):
    blog = db.query(Model).filter(Model.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")

    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id:int,request:Schema, db:Session):
    blog = db.query(Model).filter(Model.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")

    blog.update(request)
    db.commit()
    return 'updated'

def show(id:int,db:Session):
    blog = db.query(Model).filter(Model.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not available")
    return blog
    