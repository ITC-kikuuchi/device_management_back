from fastapi import APIRouter

router = APIRouter()


@router.get("/pc")
async def getPc():
    pass


@router.post("/pc")
async def createPc():
    pass


@router.get("/pc/{pc_id}")
async def getPcDetail():
    pass


@router.put("/pc/{pc_id}")
async def updatePc():
    pass


@router.delete("/pc/{pc_id}")
async def deletePc():
    pass