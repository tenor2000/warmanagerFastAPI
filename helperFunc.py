from fastapi import HTTPException

def getObjectbyId(listName, id):
    for obj in listName:
        if obj["id"] == int(id):
            return obj

    raise HTTPException(status_code=404, detail="ID not found")

def checkGameName(gameName: str):
    if gameName != "frostgrave2e":
        raise HTTPException(status_code=404, detail="Game not found")