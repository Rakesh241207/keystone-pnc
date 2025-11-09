from sqlalchemy import Column, Integer, String, JSON, Numeric, ForeignKey, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    irideto_user_id = Column(String, unique=True, nullable=True)
    wallet_id = Column(String, nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now())

class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True, index=True)
    vin = Column(String, unique=True, nullable=True)
    emaid = Column(String, unique=True, nullable=True)
    owner_user_id = Column(Integer, ForeignKey("users.id"))
    last_soc = Column(Integer, default=100)
    last_seen = Column(TIMESTAMP, server_default=func.now())

class Charger(Base):
    __tablename__ = 'chargers'
    id = Column(Integer, primary_key=True, index=True)
    charger_id = Column(String, unique=True, nullable=False)
    operator = Column(String)
    location = Column(JSON)
    connectors = Column(JSON)
    price_info = Column(JSON)
    last_updated = Column(TIMESTAMP, server_default=func.now())

class Session(Base):
    __tablename__ = 'sessions'
    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    charger_id = Column(Integer, ForeignKey("chargers.id"))
    start_ts = Column(TIMESTAMP)
    end_ts = Column(TIMESTAMP)
    kwh = Column(Numeric)
    cost = Column(Numeric)
    status = Column(String, default="started")
