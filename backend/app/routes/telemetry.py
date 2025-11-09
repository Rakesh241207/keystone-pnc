from fastapi import APIRouter, Body

router = APIRouter()

@router.post("/vehicle")
async def telemetry_vehicle(payload: dict = Body(...)):
    # payload expected: {vehicle_id, emaid, soc, lat, lon, timestamp}
    # Insert/update DB. Trigger charger discovery when soc <= 20 (or mobile does)
    return {"ok": True}
