from sqlalchemy.orm import Session
from cruds import models
from routers import schemas
from fastapi import HTTPException,status, File, UploadFile, BackgroundTasks
from io import BytesIO, StringIO
from datetime import datetime

import pandas as pd
import numpy as np
import csv, codecs

Model = models.Incident
Schema = schemas.ShowIncident

def get_all(db: Session):
    records = db.query(Model).all()
    return records

def create(request: Schema, db: Session):
    
    new_record = Model(title=request.title, body=request.body,user_id=1)
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return new_record


def upload_csv(file, db: Session):
    contents = file.file.read()
    data = BytesIO(contents)
    df = pd.read_csv(data)    
    data.close()
    file.file.close()
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    
    df['region'] = df['region'].fillna(np.nan).replace([np.nan], ['NA'])

    df['year'] = df['year'].fillna(np.nan).replace([np.nan], 0)
    df['month'] = df['month'].fillna(np.nan).replace([np.nan], 0)
    df['az'] = df['az'].fillna(np.nan).replace([np.nan], 0)

    df['year'] = df['year'].astype(int)
    df['month'] = df['month'].astype(int)
    df['az'] = df['az'].astype(int)

    df['shift_start_date'] = df['shift_start_date'].fillna(np.nan).replace([np.nan], ['1900-01-01'])
    df['shift_start_date'] = pd.to_datetime(df['shift_start_date'])

    df['occurred_at'] = df['occurred_at'].fillna(np.nan).replace([np.nan], ['1900-01-01'])
    df['occurred_at'] = pd.to_datetime(df['occurred_at'])

    df['acknowledged_at'] = df['acknowledged_at'].fillna(np.nan).replace([np.nan], ['1900-01-01'])
    df['acknowledged_at'] = pd.to_datetime(df['acknowledged_at'])

    df['propogated_at'] = df['propogated_at'].fillna(np.nan).replace([np.nan], ['1900-01-01'])
    df['propogated_at'] = pd.to_datetime(df['propogated_at'])

    df['resolved_at'] = df['resolved_at'].fillna(np.nan).replace([np.nan], ['1900-01-01'])
    df['resolved_at'] = pd.to_datetime(df['resolved_at'])
    # df['resolved_at'].map(lambda x: datetime.strptime(x, '%Y-%m-%d'), na_action='ignore')

    # print(df)
    # print(df.info())

    # df['time_to_acknowledge'] = df['time_to_acknowledge'].fillna(np.nan).replace([np.nan], ['1900-01-01'])
    # df['time_to_acknowledge'] = pd.to_datetime(df['time_to_acknowledge'])

    # df['time_to_propogated'] = df['time_to_propogated'].fillna(np.nan).replace([np.nan], ['1900-01-01'])
    # df['time_to_propogated'] = pd.to_datetime(df['time_to_propogated'])    

    try:
        db.query(Model).delete()
        dicts = df.to_dict(orient='records')
        db.bulk_insert_mappings(Model, dicts)        
        db.commit()
    except Exception as e:
        print(e)
        print("Sorry, some error has occurred!")

    return f"uploaded {file.filename}"

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