from fastapi import FastAPI, HTTPException, Depends
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise
from typing import List
from sqlalchemy.orm import Session
from models import About, Resume, Service, Skill, Project, Category, Tag, Post, Contact
import schema
import models

app = FastAPI()


# Dependency
def get_db():
    pass  # SQLite bilan ishlayotganimiz uchun ma'lumotlar bazasini to'g'ridan-to'g'ri bog'laymiz.


# About CRUD
@app.get("/about/", response_model=List[schema.About])
async def get_about():
    return await About.all()


@app.post("/about/", response_model=schema.About)
async def create_about(about: schema.AboutCreate):
    new_about = await About.create(**about.dict())
    return new_about


@app.put("/abouts/{about_id}", response_model=schema.About)
def update_about(about_id: int, about: schema.AboutCreate, db: Session = Depends(get_db)):
    db_about = db.query(models.About).filter(models.About.id == about_id).first()
    if db_about is None:
        raise HTTPException(status_code=404, detail='About not found')
    for key, value in about.dict().items():
        setattr(db_about, key, value)
    db.commit()
    db.refresh(db_about)
    return db_about


@app.delete('/abouts/{about_id}')
def delete_about(about_id: int, db: Session = Depends(get_db)):
    db_about = db.query(models.About).filter(models.About.id == about_id).first()
    if db_about is None:
        raise HTTPException(status_code=404, detail='About not found')
    db.delete(db_about)
    db.commit()
    return {'message': 'About delete'}


# Resume CRUD
@app.get("/resume/", response_model=List[schema.Resume])
async def get_resume():
    return await Resume.all()


@app.post("/resume/", response_model=schema.Resume)
async def create_resume(resume: schema.ResumeCreate):
    new_resume = await Resume.create(**resume.dict())
    return new_resume


@app.put("/resumes/{resume_id}", response_model=schema.Resume)
def update_resume(resume_id: int, resume: schema.ResumeCreate, db: Session = Depends(get_db)):
    db_resume = db.query(models.Resume).filter(models.Resume.id == resume_id).first()
    if db_resume is None:
        raise HTTPException(status_code=404, detail='Resume not found')
    for key, value in resume.dict().items():
        setattr(db_resume, key, value)
    db.commit()
    db.refresh(db_resume)
    return db_resume


@app.delete('/resumes/{resume_id}')
def delete_resume(resume_id: int, db: Session = Depends(get_db)):
    db_resume = db.query(models.Resume).filter(models.Resume.id == resume_id).first()
    if db_resume is None:
        raise HTTPException(status_code=404, detail='Resume not found')
    db.delete(db_resume)
    db.commit()
    return {'message': 'Resume delete'}


# Service CRUD
@app.get("/services/", response_model=List[schema.Service])
async def get_services():
    return await Service.all()


@app.post("/services/", response_model=schema.Service)
async def create_service(service: schema.ServiceCreate):
    new_service = await Service.create(**service.dict())
    return new_service


@app.put("/services/{services_id}", response_model=schema.Service)
def update_service(service_id: int, service: schema.ServiceCreate, db: Session = Depends(get_db)):
    db_service = db.query(models.Service).filter(models.Service.id == service_id).first()
    if db_service is None:
        raise HTTPException(status_code=404, detail='Service not found')
    for key, value in service.dict().items():
        setattr(db_service, key, value)
    db.commit()
    db.refresh(db_service)
    return db_service


@app.delete('/services/{service_id}')
def delete_service(service_id: int, db: Session = Depends(get_db)):
    db_service = db.query(models.Service).filter(models.Service.id == service_id).first()
    if db_service is None:
        raise HTTPException(status_code=404, detail='Service not found')
    db.delete(db_service)
    db.commit()
    return {'message': 'Service delete'}


# Skill CRUD
@app.get("/skills/", response_model=List[schema.Skill])
async def get_skills():
    return await Skill.all()


@app.post("/skills/", response_model=schema.Skill)
async def create_skill(skill: schema.SkillCreate):
    new_skill = await Skill.create(**skill.dict())
    return new_skill


@app.put("/skills/{skill_id}", response_model=schema.Skill)
def update_skill(skill_id: int, skill: schema.SkillCreate, db: Session = Depends(get_db)):
    db_skill = db.query(models.Skill).filter(models.Skill.id == skill_id).first()
    if db_skill is None:
        raise HTTPException(status_code=404, detail='Skill not found')
    for key, value in skill.dict().items():
        setattr(db_skill, key, value)
    db.commit()
    db.refresh(db_skill)
    return db_skill


@app.delete('/skills/{skill_id}')
def delete_skill(skill_id: int, db: Session = Depends(get_db)):
    db_skill = db.query(models.Skill).filter(models.Skill.id == skill_id).first()
    if db_skill is None:
        raise HTTPException(status_code=404, detail='Skill not found')
    db.delete(db_skill)
    db.commit()
    return {'message': 'Skill delete'}


# Project CRUD
@app.get("/projects/", response_model=List[schema.Project])
async def get_projects():
    return await Project.all()


@app.post("/projects/", response_model=schema.Project)
async def create_project(project: schema.ProjectCreate):
    new_project = await Project.create(**project.dict())
    return new_project


@app.put("/projects/{project_id}", response_model=schema.Project)
def update_project(project_id: int, project: schema.ProjectCreate, db: Session = Depends(get_db)):
    db_project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if db_project is None:
        raise HTTPException(status_code=404, detail='Project not found')
    for key, value in project.dict().items():
        setattr(db_project, key, value)
    db.commit()
    db.refresh(db_project)
    return db_project


@app.delete('/projects/{project_id}')
def delete_project(project_id: int, db: Session = Depends(get_db)):
    db_project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if db_project is None:
        raise HTTPException(status_code=404, detail='Project not found')
    db.delete(db_project)
    db.commit()
    return {'message': 'Project delete'}


# Category CRUD
@app.get("/categories/", response_model=List[schema.Category])
async def get_categories():
    return await Category.all()


@app.post("/categories/", response_model=schema.Category)
async def create_category(category: schema.CategoryCreate):
    new_category = await Category.create(**category.dict())
    return new_category


@app.put("/categories/{category_id}", response_model=schema.Category)
def update_category(category_id: int, category: schema.CategoryCreate, db: Session = Depends(get_db)):
    db_category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if db_category is None:
        raise HTTPException(status_code=404, detail='Category not found')
    for key, value in category.dict().items():
        setattr(db_category, key, value)
    db.commit()
    db.refresh(db_category)
    return db_category


@app.delete('/categories/{category_id}')
def delete_category(category_id: int, db: Session = Depends(get_db)):
    db_category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if db_category is None:
        raise HTTPException(status_code=404, detail='Category not found')
    db.delete(db_category)
    db.commit()
    return {'message': 'Category delete'}


# Tag CRUD
@app.get("/tags/", response_model=List[schema.Tag])
async def get_tags():
    return await Tag.all()


@app.post("/tags/", response_model=schema.Tag)
async def create_tag(tag: schema.TagCreate):
    new_tag = await Tag.create(**tag.dict())
    return new_tag


@app.put("/tags/{tag_id}", response_model=schema.Tag)
def update_tag(tag_id: int, tag: schema.Tag, db: Session = Depends(get_db)):
    db_tag = db.query(models.Tag).filter(models.Tag.id == tag_id).first()
    if db_tag is None:
        raise HTTPException(status_code=404, detail='Tag not found')
    for key, value in tag.dict().items():
        setattr(db_tag, key, value)
    db.commit()
    db.refresh(db_tag)
    return db_tag


@app.delete('/tags/{tag_id}')
def delete_tag(tag_id: int, db: Session = Depends(get_db)):
    db_tag = db.query(models.Tag).filter(models.Tag.id == tag_id).first()
    if db_tag is None:
        raise HTTPException(status_code=404, detail='Tag not found')
    db.delete(db_tag)
    db.commit()
    return {'message': 'Tag delete'}


# Post CRUD
@app.get("/posts/", response_model=List[schema.Post])
async def get_posts():
    return await Post.all().prefetch_related("category", "tags")


@app.post("/posts/", response_model=schema.Post)
async def create_post(post: schema.PostCreate):
    new_post = await Post.create(**post.dict(exclude={"tag_ids"}))
    tags = await Tag.filter(id__in=post.tag_ids)
    await new_post.tags.add(*tags)
    return new_post


@app.put("/posts/{post_id}", response_model=schema.Post)
def update_post(post_id: int, post: schema.Post, db: Session = Depends(get_db)):
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if db_post is None:
        raise HTTPException(status_code=404, detail='Post not found')
    for key, value in post.dict().items():
        setattr(db_post, key, value)
    db.commit()
    db.refresh(db_post)
    return db_post


@app.delete('/posts/{post_id}')
def delete_post(post_id: int, db: Session = Depends(get_db)):
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if db_post is None:
        raise HTTPException(status_code=404, detail='Post not found')
    db.delete(db_post)
    db.commit()
    return {'message': 'Post delete'}


# Contact CRUD
@app.post("/contact/", response_model=schema.Contact)
async def create_contact(contact: schema.ContactCreate):
    new_contact = await Contact.create(**contact.dict())
    return new_contact


# Tortoise ORMni FastAPI bilan bog'lash
register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
