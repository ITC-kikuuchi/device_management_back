from fastapi import FastAPI

import logging

# ロギングの設定
logging.basicConfig(
    filename="app.log", level=logging.DEBUG, format="%(asctime)s %(message)s"
)

from routers import auth, pc, ios, android, windows

app = FastAPI()
app.include_router(auth.router)
app.include_router(pc.router)
app.include_router(ios.router)
app.include_router(android.router)
app.include_router(windows.router)
