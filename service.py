from typing import Dict, List, Optional, Union

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from decimal import Decimal          # safer for money than float
import json
from datetime import datetime, timezone
from pathlib import Path
import random

from config import config

# Initialize the FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_FILE = Path("transactions.json")

# ──────────────────────────────────────────────────────────────────────────
# helpers
# ──────────────────────────────────────────────────────────────────────────
def _ensure_file():
    """Create `transactions.json` with an empty list if it does not exist."""
    if not DATA_FILE.exists():
        DATA_FILE.write_text("[]", encoding="utf-8")


def _generate_tx_id() -> str:
    """Return something like TX-123456 (always six digits)."""
    return "TX-" + str(random.randint(0, 999_999)).zfill(6)


def _append_record(record: dict):
    """Append `record` to the JSON array on disk, in a single, simple step."""
    _ensure_file()
    # load → modify → save
    with DATA_FILE.open("r", encoding="utf-8") as f:
        data = json.load(f)

    data.append(record)

    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")   # nice trailing newline


def _make_record(kind: str, amount: Decimal) -> dict:
    """
    Return a dict that looks like

    {
      "id": "TX-000123",
      "date": "2025-05-02T14:26:09Z",
      "name": "Ishan",
      "description": "[placeholder]",
      "amount": "£10.00",
      "status": "Completed",
      "type": "send"       # one extra field to keep track
    }
    """
    return {
        "id": _generate_tx_id(),
        "date": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "name": "Ishan",                      # constant for now
        "description": "[placeholder]",       # constant (change as needed)
        "amount": f"£{amount:.2f}",           # always two decimals
        "status": "Completed" if kind == "send" else "Requested",
        "type": kind,                         # optional but handy
    }


# ──────────────────────────────────────────────────────────────────────────
# API routes
# ──────────────────────────────────────────────────────────────────────────

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "message": "NFPay server is running!"}

@app.post("/approve")
async def approve():
    """Approve check endpoint"""
    return {"status": "approve", "message": "Approved the payment!"}


@app.post("/decline")
async def decline():
    """Decline endpoint"""
    return {"status": "decline", "message": "Declined the payment!"}


@app.post("/defer")
async def defer():
    """Defer check endpoint"""
    return {"status": "defer", "message": "Deferred the payment!"}

@app.post("/send")
async def send(amount: Decimal = Query(..., gt=0)):
    record = _make_record("send", amount)
    _append_record(record)
    return {"status": "Send", "message": f"£{amount} sent!"}


@app.post("/request")
async def request(amount: Decimal = Query(..., gt=0)):
    record = _make_record("request", amount)
    _append_record(record)
    return {"status": "Requested", "message": f"£{amount} requested!"}


# ---- list everything that’s in transactions.json
@app.get("/transactions")
async def list_transactions():
    _ensure_file()                      # from the helper we wrote earlier
    with DATA_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)             # FastAPI auto‑serialises to JSON


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)