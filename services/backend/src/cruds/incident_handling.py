from sqlalchemy.orm import Session
from cruds import models
from routers import schemas
from fastapi import HTTPException,status
from io import BytesIO

import pandas as pd
import numpy as np

Model = models.Incident
Schema = schemas.ShowIncident

def get_all(db: Session, current_user):
    records = db.query(Model).all()
    return records

def create(request, db: Session, current_user):
    new_record = Model(
        year = request.year,
        month = request.month,
        region = request.region,
        az = request.az,
        tenant = request.tenant,

        shift_start_date = request.shift_start_date,
        shift_type = request.shift_type,
        level_1_engineer1 = request.level_1_engineer1,
        level_1_engineer2 = request.level_1_engineer2,
        level_2_engineers = request.level_2_engineers,
        how_to_share = request.how_to_share,

        event = request.event,
        action = request.action,
        status = request.status,
        ticket_no = request.ticket_no,
        escalated_to_l3 =  request.escalated_to_l3,
        comment =  request.comment,

        occurred_at = request.occurred_at,
        acknowledged_at = request.acknowledged_at,
        propogated_at = request.propogated_at,
        resolved_at = request.resolved_at,
        
        creator = current_user.email,
    )
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return new_record


def upload_csv(file, db: Session, current_user):
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

def destroy(id:int,db: Session, current_user):
    record = db.query(Model).filter(Model.id == id)
    if not record.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"record with id {id} not found")
    if not db.query(Model).filter(Model.id == id).filter(Model.creator == current_user.email).delete():
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                        detail=f"record with id {id} unauthorized")            
    db.commit()
    return 'done'


def update(id:int,request, db:Session, current_user):
    record = db.query(Model).filter(Model.id == id).first()
    if not record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"record with id {id} not found")

    db.query(Model).filter(Model.id == id).update({
        "year": request.year,
        "month": request.month,
        "region": request.region,
        "az": request.az,
        "tenant": request.tenant,

        "shift_start_date": request.shift_start_date,
        "shift_type": request.shift_type,
        "level_1_engineer1": request.level_1_engineer1,
        "level_1_engineer2": request.level_1_engineer2,
        "level_2_engineers": request.level_2_engineers,
        "how_to_share": request.how_to_share,

        "event": request.event,
        "action": request.action,
        "status": request.status,
        "ticket_no": request.ticket_no,
        "escalated_to_l3":  request.escalated_to_l3,
        "comment":  request.comment,

        "occurred_at": request.occurred_at,
        "acknowledged_at": request.acknowledged_at,
        "propogated_at": request.propogated_at,
        "resolved_at": request.resolved_at,
        
        "updater": current_user.email,
    })
    db.commit()
    db.refresh(record)
    return 'updated'


def show(id:int,db:Session, current_user):
    record = db.query(Model).filter(Model.id == id).first()
    
    if not record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"record with the id {id} is not available")
    return record    