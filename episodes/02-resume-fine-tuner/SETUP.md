# 🚀 Setup Guide - Resume Fine-Tuner Agent

## Prerequisites

- Python 3.8 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- Basic command line knowledge

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/anton-abyzov/ai-power.git
cd ai-power/episodes/02-resume-fine-tuner
```

### 2. Install Python Dependencies

```bash
# Install required packages
pip install -r requirements.txt
```

Or install individually:
```bash
pip install openai python-docx markdown
```

### 3. Configure API Key

**Option A: Environment Variable (Recommended)**
```bash
# Linux/Mac
export OPENAI_API_KEY="your-api-key-here"

# Windows (Command Prompt)
set OPENAI_API_KEY=your-api-key-here

# Windows (PowerShell)
$env:OPENAI_API_KEY="your-api-key-here"
```

**Option B: .env File**
```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your API key
nano .env  # or use your favorite editor
```

**Option C: Pass as Command Line Argument**
```bash
python resume_fine_tuner.py --api-key "your-key" -j job.md -e experience.md
```

### 4. Prepare Your Experience Database

Choose a template based on your profession:

```bash
# Copy a template
cp templates/experience-software-engineer.md workspace/experience-db/my-experience.md

# Edit with your actual experience
nano workspace/experience-db/my-experience.md
```

Available templates:
- `templates/experience-software-engineer.md` - For software/tech roles
- `templates/experience-marketing-manager.md` - For marketing/creative roles
- `templates/experience-real-estate-agent.md` - For sales/real estate roles

### 5. Add Job Descriptions

Save job descriptions you're interested in:

```bash
# Create a new job description file
nano workspace/job-descriptions/company-role.md

# Paste the job description from LinkedIn, Indeed, etc.
```

## Usage

### Basic Usage

```bash
# Generate a tailored resume
python resume_fine_tuner.py \
  -e workspace/experience-db/my-experience.md \
  -j workspace/job-descriptions/company-role.md \
  -o workspace/outputs/company-role-resume.md
```

### Model Selection

```bash
# Use GPT-4 (best quality, higher cost)
python resume_fine_tuner.py -e experience.md -j job.md -m gpt-4

# Use GPT-4 Turbo (balanced)
python resume_fine_tuner.py -e experience.md -j job.md -m gpt-4-turbo

# Use GPT-3.5 Turbo (fast and cheap)
python resume_fine_tuner.py -e experience.md -j job.md -m gpt-3.5-turbo
```

### Extract Keywords Only

```bash
# Analyze job requirements without generating resume
python resume_fine_tuner.py -j workspace/job-descriptions/company-role.md --keywords-only
```

### Complete Example

```bash
# 1. Set API key
export OPENAI_API_KEY="sk-..."

# 2. Generate resume for a backend engineering role
python resume_fine_tuner.py \
  -e workspace/experience-db/software-engineer.md \
  -j workspace/job-descriptions/senior-backend-engineer-clickup.md \
  -o workspace/outputs/clickup-backend-resume.md \
  -m gpt-4

# 3. Check the output
cat workspace/outputs/clickup-backend-resume.md
```

## Workspace Structure

After setup, your workspace should look like this:

```
workspace/
├── experience-db/          # Your experience databases
│   ├── my-experience.md
│   └── ...
├── job-descriptions/       # Job postings you're applying to
│   ├── company-role.md
│   └── ...
└── outputs/                # Generated resumes
    ├── company-role-resume.md
    └── ...
```

## Converting to Other Formats

### Markdown to PDF/DOCX

Use `pandoc` to convert generated resumes:

```bash
# Install pandoc (if not already installed)
# Mac: brew install pandoc
# Linux: apt-get install pandoc
# Windows: Download from pandoc.org

# Convert to DOCX (for ATS systems)
pandoc workspace/outputs/resume.md -o workspace/outputs/resume.docx

# Convert to PDF
pandoc workspace/outputs/resume.md -o workspace/outputs/resume.pdf
```

### Using LaTeX

A LaTeX template is provided in `samples/example-latex-resume.tex`:

```bash
# Generate resume content
python resume_fine_tuner.py -e experience.md -j job.md -o output.md

# Convert to LaTeX format (manual editing may be needed)
# Then compile with pdflatex
pdflatex samples/example-latex-resume.tex
```

## Cost Estimation

| Model | Input Cost | Output Cost | Est. Per Resume |
|-------|-----------|-------------|-----------------|
| GPT-4 | $0.03/1K | $0.06/1K | $0.10 - $0.25 |
| GPT-4-Turbo | $0.01/1K | $0.03/1K | $0.03 - $0.10 |
| GPT-3.5-Turbo | $0.002/1K | $0.002/1K | $0.01 - $0.03 |

Average resume generation uses ~3,000-5,000 tokens total.

## Troubleshooting

### "OpenAI library not installed"
```bash
pip install openai
```

### "API key required"
Make sure you've set the `OPENAI_API_KEY` environment variable or pass it with `--api-key`.

### "Experience database not found"
Check the file path. Use relative paths from the episode directory:
```bash
python resume_fine_tuner.py -e workspace/experience-db/my-experience.md ...
```

### Rate Limits
If you hit rate limits, wait a few seconds and try again. Consider using GPT-3.5-turbo for higher throughput.

### Poor Results
- Ensure your experience database is detailed and well-formatted
- Try using GPT-4 instead of GPT-3.5-turbo for better quality
- Add more context about your achievements and metrics
- Make sure the job description is complete

## Next Steps

1. ✅ Complete setup
2. ✅ Create your experience database
3. ✅ Find job postings you want to apply to
4. ✅ Generate tailored resumes
5. ✅ Convert to PDF/DOCX for applications
6. 📊 Track your success rate!

## Support

- **Documentation**: [🎯 START_HERE.md](🎯%20START_HERE.md)
- **Video Tutorial**: [Episode 02 on YouTube](https://youtube.com/@antonabyzov)
- **Issues**: [GitHub Issues](https://github.com/anton-abyzov/ai-power/issues)
- **Community**: Comment on the YouTube video

---

**Ready to 3x your interview rate? Start generating resumes! 🚀**
