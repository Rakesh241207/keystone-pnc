from fastapi import FastAPI
from .routes import auth, telemetry, charger, payment

app = FastAPI(title="Keystone PnC Orchestrator")

app.include_router(auth.router, prefix="/auth")
app.include_router(telemetry.router, prefix="/telemetry")
app.include_router(charger.router, prefix="/charger")
app.include_router(payment.router, prefix="/payment")
