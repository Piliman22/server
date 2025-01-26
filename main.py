from fastapi import FastAPI
from fastapi.responses import FileResponse, RedirectResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from router import tools
from router import duplication
from router import noisegen

import json

with open("config.json",encoding="utf-8") as f:
    conf = json.load(f)
    host = conf["Host"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        host,
        "http://localhost:5000",
        "http://127.0.0.1:5000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tools.router)
app.include_router(duplication.router)
app.include_router(noisegen.router)

with open("templates/index.html","r",encoding="UTF-8") as f:
    idx_content = f.read()

@app.get('/',response_class=HTMLResponse)
async def index():
    return idx_content

@app.get('/{word}')
async def res_word(word:str):
    return word

@app.get('/css/{filename}')
def css(filename: str):
    return FileResponse(f"templates/css/{filename}")

@app.exception_handler(404)
async def notfound(request,exc):
    return RedirectResponse('https://www.youtube.com/@piliman_CH')

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, host="127.0.0.1", reload=True)