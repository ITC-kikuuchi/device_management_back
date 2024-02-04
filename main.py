from fastapi import FastAPI

from routers import auth, pc, ios, android, windows

app = FastAPI()
app.include_router(auth.router)
app.include_router(pc.router)
app.include_router(ios.router)
app.include_router(android.router)
app.include_router(windows.router)