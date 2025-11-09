from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class ChargeReq(BaseModel):
    session_id: int

@router.post("/charge")
async def charge(req: ChargeReq):
    # compute cost and call PSP or internal ledger
    return {"success": True, "session_id": req.session_id}
