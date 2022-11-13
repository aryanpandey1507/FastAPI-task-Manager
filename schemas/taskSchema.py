def taskEntity(item) -> dict:
    return {
        "_id":str(item["_id"]),
        "title":item["title"],
        "is_completed":item["is_completed"]
    }

def tasksEntity(entity)-> list:
    return [taskEntity(item) for item in entity]