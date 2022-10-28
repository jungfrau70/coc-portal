from sqlalchemy.orm import Session
from cruds import models
from routers import schemas
from fastapi import HTTPException,status
from io import BytesIO

import csv, codecs, json
import pandas as pd
import numpy as np
import re

def get_all(db: Session):
    problems = db.query(models.Problem).all()
    return problems

def create(request: schemas.Problem, db: Session):
    new_problem = models.Problem(title=request.title, body=request.body,user_id=1)
    db.add(new_problem)
    db.commit()
    db.refresh(new_problem)
    return new_problem

def upload_csv(form_data: schemas.AwesomeForm, db: Session):
    contents = form_data.file.file.read()
    data = BytesIO(contents)
    df = pd.read_csv(data)

    df['reviewed_at'] = df['reviewed_at'].fillna(np.nan).replace([np.nan], ['1970-01-01'])
    df['reviewed_at'] = pd.to_datetime(df['reviewed_at'])
         
    data.close()
    form_data.file.file.close()
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    try:
        db.query(models.Problem).delete()
        dicts = df.to_dict(orient='records')
        db.bulk_insert_mappings(models.Problem, dicts)        
        db.commit()
    except Exception as e:
        print(e)
        print("Sorry, some error has occurred!")

    return "uploaded"

def destroy(id:int,db: Session):
    problem = db.query(models.Problem).filter(models.Problem.id == id)

    if not problem.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"problem with id {id} not found")

    problem.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id:int,request:schemas.Problem, db:Session):
    problem = db.query(models.Problem).filter(models.Problem.id == id)

    if not problem.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"problem with id {id} not found")

    problem.update(request)
    db.commit()
    return 'updated'

def show(id:int,db:Session):
    problem = db.query(models.Problem).filter(models.Problem.id == id).first()
    if not problem:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"problem with the id {id} is not available")
    return problem