from fastapi import FastAPI

from routers import auth, pc, ios

app = FastAPI()
app.include_router(auth.router)
app.include_router(pc.router)
app.include_router(ios.router)