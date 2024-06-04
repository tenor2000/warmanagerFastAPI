from fastapi import HTTPException

def getObjectbyId(listName, id):
    for obj in listName:
        if obj["id"] == int(id):
            return obj

    raise HTTPException(status_code=404, detail="ID not found")