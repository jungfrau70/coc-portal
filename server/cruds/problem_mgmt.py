from sqlalchemy.orm import Session
from cruds import models
from routers import schemas
from fastapi import HTTPException,status
from io import BytesIO

import pandas as pd
import numpy as np

Model = models.Problem
Schema = schemas.ShowProblem

def get_all(db: Session):
    records = db.query(Model).all()
    return records

def create(request: Schema, db: Session):
    new_record = Model(title=request.title, body=request.body,user_id=1)
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return new_record

# def upload_csv(form_data: schemas.AwesomeForm, db: Session):
def upload_csv(file, db: Session):
    contents = form_data.file.file.read()
    data = BytesIO(contents)
    df = pd.read_csv(data)

    df['reviewed_at'] = df['reviewed_at'].fillna(np.nan).replace([np.nan], ['1970-01-01'])
    df['reviewed_at'] = pd.to_datetime(df['reviewed_at'])
         
    data.close()
    form_data.file.file.close()
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    try:
        db.query(Model).delete()
        dicts = df.to_dict(orient='records')
        db.bulk_insert_mappings(Model, dicts)        
        db.commit()
    except Exception as e:
        print(e)
        print("Sorry, some error has occurred!")

    return "uploaded"

def destroy(id:int,db: Session):
    record = db.query(Model).filter(Model.id == id)

    if not record.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"record with id {id} not found")

    record.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id:int,request:Schema, db:Session):
    record = db.query(Model).filter(Model.id == id)

    if not record.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"record with id {id} not found")

    record.update(request)
    db.commit()
    return 'updated'

def show(id:int,db:Session):
    record = db.query(Model).filter(Model.id == id).first()
    if not record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"record with the id {id} is not available")
    return record    