from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import json
from helperFunc import getObjectbyId, checkGameName

app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

with open('data/reference.json') as f:
    json_data = json.load(f)

# Get All Game Data
@app.get("/{gameName}/data.json")
def getGameData(gameName):
    checkGameName(gameName)
    return json_data

# Get lists or entries
@app.get("/{gameName}/{listName}")
def getReferenceList(gameName: str, listName: str, id: Optional[int] = None):
    checkGameName(gameName)
    if listName in json_data:
        if id is not None:
            return getObjectbyId(json_data[listName], id)
        return json_data[listName]
    raise HTTPException(status_code=404, detail="List not found") 


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)