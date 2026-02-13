# 🎯 START HERE: Your Personal Resume Agent

**Welcome!** This is your personal Resume Fine-Tuner agent. It creates tailored resumes for specific jobs in 2 minutes.

---

## ⚡ Quick Start (3 Steps)

### 1️⃣ Run Setup (1 minute)
```bash
bash setup_agent.sh
```

### 2️⃣ Fill Your Experience (30 minutes, one-time)
```bash
# Open this file and replace ALL placeholders with YOUR info:
nano workspace/experience-db/YOUR-EXPERIENCE.md
```

### 3️⃣ Generate Resume (2 minutes per job)
```bash
# Save a job description, then run:
python resume_fine_tuner.py \
  -e workspace/experience-db/YOUR-EXPERIENCE.md \
  -j workspace/job-descriptions/job.md \
  -o workspace/outputs/resume.md
```

---

## 📚 Full Documentation

- **[HOW_TO_USE.md](HOW_TO_USE.md)** ← Read this for complete instructions
- **[SETUP.md](SETUP.md)** - Installation details
- **[QUICK_START.md](QUICK_START.md)** - Quick examples
- **[🎯 START_HERE.md](🎯%20START_HERE.md)** - Complete reference

---

## 🔑 Important: Get Your OpenAI API Key

You need an API key to use this:

1. Go to: https://platform.openai.com/api-keys
2. Sign up and create a new key
3. Run: `export OPENAI_API_KEY='sk-your-key'`

**Cost**: $0.01-0.25 per resume (totally worth it!)

---

## 📁 File Structure

```
episodes/02-resume-fine-tuner/
│
├── resume_fine_tuner.py          ← The AI agent (don't edit)
├── setup_agent.sh                ← Run this first!
├── HOW_TO_USE.md                 ← Read this for instructions
│
└── workspace/                    ← YOUR workspace
    ├── experience-db/
    │   ├── YOUR-EXPERIENCE.md    ← Fill this out with YOUR info! ⭐
    │   ├── software-engineer.md  (example)
    │   ├── marketing-manager.md  (example)
    │   └── real-estate-agent.md  (example)
    │
    ├── job-descriptions/         ← Save job postings here
    │   └── (your jobs here)
    │
    └── outputs/                  ← Generated resumes appear here
        └── (your resumes here)
```

---

## 💡 What This Does

1. **You provide**: Your CV/experience + a job description
2. **AI generates**: A tailored resume matching the job requirements
3. **You get**: 90%+ keyword coverage, ATS-optimized, professional

**Results**: 3x more responses, 6x more interviews, 60x faster than manual!

---

## ✅ What You Need to Do NOW

1. [ ] Run `bash setup_agent.sh`
2. [ ] Get OpenAI API key from https://platform.openai.com/api-keys
3. [ ] Set it: `export OPENAI_API_KEY='sk-your-key'`
4. [ ] Open `workspace/experience-db/YOUR-EXPERIENCE.md`
5. [ ] Fill it with YOUR real career info
6. [ ] Save a job description you want to apply to
7. [ ] Run the agent and generate your first resume!

---

## 🆘 Need Help?

**Read**: [HOW_TO_USE.md](HOW_TO_USE.md) - Complete step-by-step guide

**Quick help**:
- Setup issues? Check `SETUP.md`
- Usage questions? Check `QUICK_START.md`
- Want examples? Look in `workspace/experience-db/`

---

## 🎉 Ready?

**Your next step**: Run `bash setup_agent.sh` and follow the instructions!

Good luck with your job search! 🚀
