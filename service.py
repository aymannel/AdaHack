import base64
import mimetypes
import os
import re
from typing import Dict, List, Optional, Union

import httpx
from fastapi import FastAPI, File, HTTPException, Response, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

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

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "message": "NFPay server is running!"}


@app.post("/approve")
async def approve():
    """Approve check endpoint"""
    return {"status": "approve", "message": "NFPay server is running!"}


@app.post("/decline")
async def decline():
    """Decline endpoint"""
    return {"status": "decline", "message": "NFPay server is running!"}


@app.post("/defer")
async def defer():
    """Defer check endpoint"""
    return {"status": "defer", "message": "NFPay server is running!"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)