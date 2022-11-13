from typing import Union,Optional

from bson.objectid import ObjectId
from fastapi import APIRouter, Request, Response, status

from config.db import collection_name
from models.task import Task, TaskList , TaskDeleteList , Ids
from schemas.taskSchema import taskEntity, tasksEntity

task = APIRouter()

# listing all tasks created
@task.get('/v1/tasks',status_code=status.HTTP_200_OK)
async def find_all_tasks():
    return {"tasks":tasksEntity(collection_name.find())}

# getting a single task
@task.get('/v1/tasks/{id}',status_code=status.HTTP_200_OK)
async def find_one_task(id,response:Response):
    if not list(collection_name.find({"_id":ObjectId(id)})):
        response.status_code=status.HTTP_404_NOT_FOUND
        return {'error':'There is no task at that id'}
    return taskEntity(collection_name.find_one({"_id":ObjectId(id)}))

#adding a single or multiple tasks
@task.post('/v1/tasks',status_code=status.HTTP_201_CREATED)
async def create_task(task:Union[Task,TaskList]):

    #adding a single task
    if 'tasks' not in dict(task):
     _id=collection_name.insert_one(dict(task))
     id=_id.inserted_id
     return {"id":str(id)}
    
    #adding multiple tasks
    tasks=[] 
    if 'tasks' in dict(task):
      for x in dict(task)['tasks']:
         print(dict(x))
         _id = collection_name.insert_one(dict(x))
         id=_id.inserted_id
         tasks.append({"id":str(id)})
    taskDict={"tasks":tasks}
    return taskDict

#updating a task
@task.put('/v1/tasks/{id}',status_code=status.HTTP_204_NO_CONTENT)
async def updating_task(id,task:Task,response:Response):

    if not list(collection_name.find({"_id":ObjectId(id)})):
        response.status_code=status.HTTP_404_NOT_FOUND
        return {'error':'There is no task at that id'}
    collection_name.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(task)
    })
    return taskEntity(collection_name.find_one({"_id":ObjectId(id)}))

#deleting a single task
@task.delete('/v1/tasks/{id}',status_code=status.HTTP_204_NO_CONTENT)
async def deleting_task(id):

    if not list(collection_name.find({"_id":ObjectId(id)})):
         return 
    taskEntity(collection_name.find_one_and_delete({"_id":ObjectId(id)}))
    return

@task.delete('/v1/tasks',status_code=status.HTTP_204_NO_CONTENT)
async def deleting_tasks(ids:TaskDeleteList):
    for x in dict(ids)['tasks']:
        if not list(collection_name.find({"_id":ObjectId(dict(x)['id'])})):
            continue 
        taskEntity(collection_name.find_one_and_delete({"_id":ObjectId(dict(x)['id'])}))



    
    






 