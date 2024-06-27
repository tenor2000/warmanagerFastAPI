from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
# from pydantic import BaseModel
from typing import List, Optional
import json
import os
from helperFunc import getObjectbyId, checkGameName, combineReferenceData

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Get All Reference Data
@app.get("/{gameName}/refData.json")
def getFullReferenceData(gameName: str):
    print(f"Checking game: {gameName}")
    checkGameName(gameName)
    print(f"Combining reference data for game: {gameName}")
    combinedData = combineReferenceData(gameName)
    print(f"Combined data: {combinedData}")
    return JSONResponse(content=combinedData)

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