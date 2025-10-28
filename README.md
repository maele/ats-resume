# 🧑‍💼 Resume Builder

A modern, **ATS-friendly**, **self-hosted** resume builder with a clean UI, real-time preview, and full control over your data. Built with **Tailwind CSS**, **FastAPI**, and **vanilla JavaScript**.

---

## ✨ Features

- ✅ **Live Resume Builder**: Add experience, education, projects, certifications, skills, and more  
- ✅ **Real-time Preview**: See changes instantly as you type  
- ✅ **Export Options**:  
  - **PDF** (print-ready, A4-optimized)  
  - **JSON** (for backup or sharing)  
- ✅ **Import JSON**: Restore or share templates  
- ✅ **Save to Backend**: Persist your resume via a secure REST API  
- ✅ **ATS-Optimized**: Clean semantic HTML, no columns, linear flow  
- ✅ **Responsive Design**: Works on mobile, tablet, and desktop  
- ✅ **Custom Theme**: Beautiful teal-blue color scheme (`#0094bb`)  
- ✅ **Free Hosting**: Deploy in minutes on Render (no credit card required)

---

## 🚀 Demo

Try the live demo: [https://resume-builder.onrender.com](https://resume-builder.onrender.com)

---

## 🛠️ Tech Stack

- **Frontend**: HTML, Tailwind CSS (via CDN), Vanilla JavaScript  
- **Backend**: FastAPI (Python)  
- **Deployment**: Render (free tier)  
- **Fonts**: Inter (text), JetBrains Mono (code-like skills)

---

## 📦 Project Structure
resume-builder/

├── backend/

│ ├── main.py # FastAPI app

│ ├── requirements.txt # Python dependencies

│ └── data/

│ └── resume.json # Your resume data (persistent on Render)

└── frontend/

└── index.html # Resume builder UI


---

## 🚀 Deployment (Free on Render)

### 1. Push to GitHub
```bash
git init
git add .
git commit -m "Resume Builder"
git branch -M main
git remote add origin https://github.com/your-username/resume-builder.git
git push -u origin main
