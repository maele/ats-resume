from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
RESUME_PATH = os.path.join(DATA_DIR, "resume.json")

os.makedirs(DATA_DIR, exist_ok=True)

if not os.path.exists(RESUME_PATH):
    with open(RESUME_PATH, "w") as f:
        json.dump({
            "name": "Your Name",
            "title": "Your Title",
            "contact": {},
            "summary": "",
            "experience": [],
            "education": {},
            "skills": []
        }, f)

app = FastAPI(title="Resume API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    education: EducationInfo
    skills: List[str]

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

app.mount("/", StaticFiles(directory="../frontend", html=True), name="frontend")
