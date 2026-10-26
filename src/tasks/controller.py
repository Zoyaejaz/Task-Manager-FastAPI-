from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel
from fastapi import HTTPException
from src.user.models import UserModel

def create_task(body:TaskSchema,db:Session,user:UserModel):
    data=body.model_dump()
    new_task=TaskModel(title=data["title"], 
                       description=data["description"],
                       is_completed=data["is_completed"],
                       user_id=user.id
                       )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def get_tasks(db:Session,user:UserModel):
    tasks=db.query(TaskModel).filter(TaskModel.user_id==user.id).all()
    return tasks


def get_one_task(task_id:int,db:Session):
    one_task=db.query(TaskModel).get(task_id)
    if not one_task:
       raise  HTTPException(404,detail="Task Id is Incorrect") #we use raise instead of return to show it as error. So that it will give 404 not found, but if we write return then it will give 200 ok and we don't want that

    return one_task


def update_task(body:TaskSchema,task_id:int,db:Session,user:UserModel):
    one_task:TaskModel=db.query(TaskModel).get(task_id)
    if not one_task:
        raise  HTTPException(404,detail="Task Id is Incorrect") 
    if one_task.user_id !=user.id:
        raise HTTPException(404, detail="You are not allowed to update this task.")
    body=body.model_dump()
    for field, value in body.items():
        setattr(one_task,field,value)

    db.add(one_task)
    db.commit()
    db.refresh(one_task)

    return one_task


def delete_task(task_id:int,db:Session,user:UserModel):
    one_task=db.query(TaskModel).get(task_id)
    if not one_task:
        raise  HTTPException(404,detail="Task Id is Incorrect")

    if one_task.user_id !=user.id:
            raise HTTPException(404, detail="You are not allowed to delete this task.")
    
    db.delete(one_task)
    db.commit()

    return None #the controller of delete does not return anything that's why we have written None
