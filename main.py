from fastapi import FastAPI

from routers import auth, pc, ios, android

app = FastAPI()
app.include_router(auth.router)
app.include_router(pc.router)
app.include_router(ios.router)
app.include_router(android.router)