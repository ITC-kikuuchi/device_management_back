from fastapi import FastAPI

from routers import auth, pc

app = FastAPI()
app.include_router(auth.router)
app.include_router(pc.router)