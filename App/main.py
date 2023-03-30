from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, Response 
from Domain.scrappingService import scrapping

app = FastAPI()

@app.get("/scrapping_page/")
async def ScrappingPage(url: str):
    try:
        result = await scrapping(url)
        return result
    except:
        raise HTTPException(status_code=400, detail="Error executing scrap")
    

