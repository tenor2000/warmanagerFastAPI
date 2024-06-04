from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import json
from helperFunc import getObjectbyId

app = FastAPI()

with open('data/reference.json') as f:
    json_data = json.load(f)

# Get All Game Data
@app.get("/{game_name}/data.json")
def getGameData(game_name):
    if game_name == "frostgrave2e":
        return json_data
    raise HTTPException(status_code=404, detail="Game not found")

# Get lists
@app.get("/{game_name}/{listName}")
def getReferenceList(game_name, listName):
    if game_name == "frostgrave2e":
        if listName in json_data:
            return json_data[listName]
        
        raise HTTPException(status_code=404, detail="List not found") 
        
    raise HTTPException(status_code=404, detail="Game not found") 

# Get Object by Id
@app.get("/{game_name}/{listName}/{id}")
def getIdEntries(game_name, listName, id: int):
    if game_name == "frostgrave2e":
        if listName in json_data:
            return getObjectbyId(json_data[listName], id)
            
        raise HTTPException(status_code=404, detail="List not found") 

    raise HTTPException(status_code=404, detail="Game not found") 


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)