from datetime import datetime, timezone
from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI(title="HKS Insurance Advisory API", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Lead(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    phone: str = Field(min_length=8, max_length=24)
    email: Optional[str] = None
    interest: str = Field(min_length=2, max_length=120)

@app.get("/api/health")
def health():
    return {"status": "ok", "service": "HKS Insurance Advisory", "mode": "prototype"}

@app.get("/api/products")
def products():
    return [
        {"id":"health","category":"Health","title":"Health insurance","from":"₹12,400 / year"},
        {"id":"term","category":"Life","title":"Term life cover","from":"₹540 / month"},
        {"id":"motor","category":"Motor","title":"Car insurance","from":"₹2,100 / year"},
        {"id":"travel","category":"Travel","title":"Travel insurance","from":"₹399 / trip"},
        {"id":"business","category":"Corporate","title":"Business protection","from":"Tailored to your team"},
        {"id":"loan","category":"Finance","title":"Loans & finance","from":"Check your options"},
    ]

@app.post("/api/leads", status_code=201)
def create_lead(lead: Lead):
    # Prototype behavior: acknowledge the enquiry without persisting personal data.
    return {"received": True, "interest": lead.interest, "received_at": datetime.now(timezone.utc).isoformat()}
