import logging
from typing import Annotated
from fastapi import FastAPI, Request, File
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pathlib
import uvicorn

from whisper import WhisperAPI

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")
whisper = WhisperAPI()


@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse("whisper.html", {"request": request})


@app.post("/")
async def create_file(file: Annotated[bytes, File()], request: Request):
    with open("audio.mp3", "wb") as temp_file:
        temp_file.write(file)
    text = await whisper.trancribe_file(pathlib.Path(temp_file.name), "whisper-1")
    return text


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
