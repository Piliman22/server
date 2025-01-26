# ノイズ生成ツール サーバー
from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

with open("templates/tools/noise/index.html","r",encoding="UTF-8") as f:
    idx_html = f.read()

@router.get('/noisegen',response_class=HTMLResponse)
def html():
    return idx_html