from fastapi import HTTPException
import os
import json

def getObjectbyId(listName, id):
    for obj in listName:
        if obj["id"] == int(id):
            return obj

    raise HTTPException(status_code=404, detail="ID not found")

def checkGameName(gameName: str):
    path = os.path.join('ReferenceData/' + gameName)
    if not os.path.isdir(path):
        raise HTTPException(status_code=404, detail="Game not found")
    
def combineReferenceData(gameName: str):
    combinedData = {}

    directoryPath = 'ReferenceData/' + gameName

    for filename in os.listdir(directoryPath):
        if filename.endswith('.json'):
            dataname = filename[:-5]
            filePath = os.path.join(directoryPath, filename)
            try:
                with open(filePath, 'r', encoding='utf-8') as file:
                    fileContent = file.read().strip()
                    # print(f"File content for {filename}: {fileContent}")
                    if not fileContent:
                        print(f"Skipping empty file: {filePath}")
                        continue
                    data = json.loads(fileContent)
                    combinedData[dataname] = data
            except json.JSONDecodeError as e:
                raise HTTPException(status_code=500, detail=f"Error reading {filePath}: {e}")
    
    return combinedData