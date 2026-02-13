# Quick Start Example - Resume Fine-Tuner

This is a complete example showing how to generate a tailored resume in 2 minutes.

## Prerequisites

```bash
# 1. Install dependencies
pip install openai

# 2. Set your OpenAI API key
export OPENAI_API_KEY="sk-your-api-key-here"
```

## Example 1: Software Engineer Resume

### Step 1: Navigate to the episode directory
```bash
cd episodes/02-resume-fine-tuner
```

### Step 2: Generate resume
```bash
python resume_fine_tuner.py \
  -e workspace/experience-db/software-engineer.md \
  -j workspace/job-descriptions/senior-backend-engineer-clickup.md \
  -o workspace/outputs/clickup-resume.md \
  -m gpt-4
```

### Expected Output
```
Generating resume using gpt-4...

✅ Resume generated successfully!
📄 Saved to: workspace/outputs/clickup-resume.md

Preview (first 500 chars):
==================================================
# John Doe
San Francisco, CA | john.doe@email.com | (555) 123-4567 | linkedin.com/in/johndoe

## Professional Summary
Results-driven Senior Software Engineer with 8+ years of experience 
building scalable backend systems and microservices architectures. 
Proven expertise in Python, AWS, and Kubernetes, with a track record 
of improving system performance and reliability...
==================================================
```

## Example 2: Marketing Manager Resume

```bash
python resume_fine_tuner.py \
  -e workspace/experience-db/marketing-manager.md \
  -j workspace/job-descriptions/marketing-role.md \
  -o workspace/outputs/marketing-resume.md \
  -m gpt-4
```

## Example 3: Real Estate Agent Resume

```bash
python resume_fine_tuner.py \
  -e workspace/experience-db/real-estate-agent.md \
  -j workspace/job-descriptions/real-estate-role.md \
  -o workspace/outputs/real-estate-resume.md \
  -m gpt-4
```

## Example 4: Extract Keywords Only

Want to see what skills are required before generating a resume?

```bash
python resume_fine_tuner.py \
  -j workspace/job-descriptions/senior-backend-engineer-clickup.md \
  --keywords-only
```

Output:
```json
{
  "critical_skills": [
    "Python",
    "AWS",
    "Kubernetes",
    "Microservices",
    "Docker",
    "REST APIs"
  ],
  "technical_skills": [
    "PostgreSQL",
    "Redis",
    "CI/CD",
    "Git",
    "Linux"
  ],
  "soft_skills": [
    "Team leadership",
    "Code review",
    "Agile methodology",
    "Communication"
  ],
  "nice_to_have": [
    "Go",
    "GraphQL",
    "Terraform",
    "Kafka"
  ]
}
```

## Example 5: Using Different Models

### GPT-4 (Best Quality)
```bash
python resume_fine_tuner.py -e experience.md -j job.md -m gpt-4
# Cost: ~$0.15-0.25 per resume
# Time: 30-60 seconds
```

### GPT-4 Turbo (Balanced)
```bash
python resume_fine_tuner.py -e experience.md -j job.md -m gpt-4-turbo
# Cost: ~$0.05-0.10 per resume
# Time: 20-40 seconds
```

### GPT-3.5 Turbo (Fast & Cheap)
```bash
python resume_fine_tuner.py -e experience.md -j job.md -m gpt-3.5-turbo
# Cost: ~$0.01-0.03 per resume
# Time: 10-20 seconds
```

## Converting to Other Formats

### Convert to DOCX (for ATS systems)
```bash
# Install pandoc if not already installed
# Mac: brew install pandoc
# Linux: apt-get install pandoc

pandoc workspace/outputs/clickup-resume.md \
  -o workspace/outputs/clickup-resume.docx
```

### Convert to PDF
```bash
pandoc workspace/outputs/clickup-resume.md \
  -o workspace/outputs/clickup-resume.pdf \
  --pdf-engine=xelatex
```

### Convert to HTML
```bash
pandoc workspace/outputs/clickup-resume.md \
  -o workspace/outputs/clickup-resume.html \
  --standalone \
  --css=style.css
```

## Batch Processing Multiple Jobs

Generate resumes for multiple job postings:

```bash
#!/bin/bash
# batch_generate.sh

EXPERIENCE="workspace/experience-db/software-engineer.md"
OUTPUT_DIR="workspace/outputs"
MODEL="gpt-4"

for JOB_DESC in workspace/job-descriptions/*.md; do
  JOB_NAME=$(basename "$JOB_DESC" .md)
  echo "Generating resume for: $JOB_NAME"
  
  python resume_fine_tuner.py \
    -e "$EXPERIENCE" \
    -j "$JOB_DESC" \
    -o "$OUTPUT_DIR/${JOB_NAME}-resume.md" \
    -m "$MODEL"
  
  echo "✅ Completed: $JOB_NAME"
  echo "---"
done

echo "🎉 All resumes generated!"
```

Make it executable and run:
```bash
chmod +x batch_generate.sh
./batch_generate.sh
```

## Tips for Best Results

### 1. Detailed Experience Database
The more detailed your experience database, the better the results:
- Include specific technologies used
- Add quantifiable achievements (15-30% improvements)
- Mention team sizes and collaboration
- Include project durations

### 2. Complete Job Descriptions
Copy the full job description including:
- Required qualifications
- Preferred qualifications
- Responsibilities
- About the company

### 3. Multiple Iterations
Generate 2-3 versions and pick the best:
```bash
for i in {1..3}; do
  python resume_fine_tuner.py -e exp.md -j job.md -o "resume-v$i.md"
done
```

### 4. Review and Edit
Always review the generated resume:
- Verify all facts are accurate
- Adjust tone if needed
- Add any missing information
- Remove any hallucinated content

## Troubleshooting

### Error: "OpenAI library not installed"
```bash
pip install openai
```

### Error: "API key required"
```bash
export OPENAI_API_KEY="sk-your-key-here"
# Or pass directly:
python resume_fine_tuner.py --api-key "sk-your-key" -e exp.md -j job.md
```

### Error: "Experience database not found"
Make sure you're using the correct path from the episode directory:
```bash
# ✅ Correct
python resume_fine_tuner.py -e workspace/experience-db/software-engineer.md ...

# ❌ Wrong
python resume_fine_tuner.py -e software-engineer.md ...
```

### Rate Limit Errors
If you hit rate limits:
1. Wait 60 seconds and try again
2. Use GPT-3.5-turbo for higher throughput
3. Add delays between batch requests

## Success Metrics

Track your results:

| Metric | Before AI | After AI | Improvement |
|--------|-----------|----------|-------------|
| Response Rate | 12% | 44% | +267% |
| Interview Rate | 6% | 36% | +500% |
| Time per Resume | 90 min | 2 min | 98% faster |
| Resumes per Week | 5 | 50 | 10x more |

## Next Steps

1. ✅ Generate your first resume
2. 📊 Track response rates
3. 🔄 Iterate and improve
4. 💼 Land more interviews!

## Support

- **Full Guide**: [🎯 START_HERE.md](🎯%20START_HERE.md)
- **Setup Instructions**: [SETUP.md](SETUP.md)
- **YouTube Tutorial**: [Episode 02](https://youtu.be/RfwZSRRRtmY)
- **GitHub Issues**: [Report bugs](https://github.com/anton-abyzov/ai-power/issues)

---

**Ready to 3x your interview rate? Start now! 🚀**
