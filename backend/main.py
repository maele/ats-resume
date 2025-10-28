from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import json
import os
from pathlib import Path

# --- PATH CONFIGURATION ---
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "backend" / "data"
RESUME_PATH = DATA_DIR / "resume.json"
FRONTEND_DIR = BASE_DIR / "frontend"

# Ensure data directory exists
DATA_DIR.mkdir(exist_ok=True)

# Create default resume.json if missing
if not RESUME_PATH.exists():
    with open(RESUME_PATH, "w") as f:
        json.dump({
            "name": "Your Name",
            "title": "Your Title",
            "contact": {},
            "summary": "",
            "experience": [],
            "education": [],
            "skills": []
        }, f)

# --- FASTAPI SETUP ---
app = FastAPI(title="Resume API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- PYDANTIC MODELS ---
class ContactInfo(BaseModel):
    email: str
    phone: str
    website: str
    linkedin: str

class ExperienceItem(BaseModel):
    role: str
    company: str
    duration: str
    highlights: List[str]

class EducationInfo(BaseModel):
    degree: str
    school: str
    duration: str
    details: str

class ResumeData(BaseModel):
    name: str
    title: str
    contact: ContactInfo
    summary: str
    experience: List[ExperienceItem]
    education: List[EducationInfo]
    skills: List[str]

# --- API ROUTES ---
@app.get("/api/resume", response_model=ResumeData)
async def get_resume():
    try:
        with open(RESUME_PATH, "r") as f:
            return json.load(f)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/api/resume")
async def update_resume(resume: ResumeData):
    try:
        with open(RESUME_PATH, "w") as f:
            json.dump(resume.dict(), f, indent=2)
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# --- SERVE FRONTEND ---
if not FRONTEND_DIR.exists():
    print(f"⚠️ Warning: Frontend not found at {FRONTEND_DIR}")
else:
    app.mount("/", StaticFiles(directory=str(FRONTEND_DIR), html=True), name="frontend")
