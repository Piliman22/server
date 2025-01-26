# ツールサーバー ダウンロード処理&html表示
from fastapi import APIRouter
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
import os

router = APIRouter()

with open("templates/tools/index.html","r",encoding="UTF-8") as f:
    idx_html = f.read()

@router.get('/tool',response_class=HTMLResponse)
def html():
    return idx_html

@router.get('/tool/{filename}')
def file_response(filename: str):
    path = os.path.join("file", filename)
    if os.path.exists(path):
        return FileResponse(path, filename=filename)
    return RedirectResponse('https://www.youtube.com/@piliman_CH')