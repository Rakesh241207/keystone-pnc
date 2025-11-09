from fastapi import APIRouter

router = APIRouter()

@router.get("/discover")
async def discover(lat: float, lon: float, radius: int = 5000, connector: str = "CCS"):
    # TODO: call Hubject/GIREVE connector
    return {"chargers": []}

@router.get("/{charger_id}")
async def get_charger(charger_id: str):
    # return cached charger metadata
    return {"charger_id": charger_id, "operator":"example", "price": "0.35EUR/kWh", "connectors":["CCS"]}
