#!/usr/bin/env python3
"""
Resume Fine-Tuner Agent - OpenAI API Implementation
Replicates Claude Sonnet 4.5 functionality using GPT-4 or GPT-3.5-turbo

Based on Episode 02: AI Resume Fine-Tuner from Anton Abyzov's YouTube series
"""

import os
import sys
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
import argparse

try:
    from openai import OpenAI
except ImportError:
    print("Error: OpenAI library not installed. Install with: pip install openai")
    sys.exit(1)


class ResumeFIneTuner:
    """AI-powered resume optimization agent using OpenAI API"""
    
    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-4"):
        """
        Initialize the Resume Fine-Tuner agent
        
        Args:
            api_key: OpenAI API key (or set OPENAI_API_KEY env variable)
            model: Model to use (gpt-4, gpt-4-turbo, or gpt-3.5-turbo)
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key required. Set OPENAI_API_KEY environment variable or pass api_key parameter.")
        
        self.client = OpenAI(api_key=self.api_key)
        self.model = model
        
        # Load the agent prompt
        self.agent_prompt = self._load_agent_prompt()
    
    def _load_agent_prompt(self) -> str:
        """Load the agent configuration from prompts/resume-fine-tuner-agent.md"""
        prompt_path = Path(__file__).parent / "prompts" / "resume-fine-tuner-agent.md"
        
        if not prompt_path.exists():
            # Fallback to embedded prompt
            return self._get_default_prompt()
        
        with open(prompt_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Remove YAML frontmatter if present
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    content = parts[2].strip()
            return content
    
    def _get_default_prompt(self) -> str:
        """Fallback agent prompt if file not found"""
        return """
# Resume Fine-Tuner Agent

## Core Mission
Generate job-optimized resumes achieving 90%+ keyword coverage while maintaining factual accuracy, natural language, and ATS compatibility.

## Key Principles
1. **Authenticity**: NEVER fabricate companies I worked for
2. **Natural Language**: Avoid robotic, AI-generated patterns
3. **Realistic Metrics**: Use believable improvements (15-30%), not 10x claims
4. **ATS Optimization**: Ensure machine readability while maintaining human appeal

## Output Format
Generate a professional resume in Markdown format with these sections:
- Professional Summary (3-4 sentences tailored to the role)
- Experience (with achievements tailored to JD requirements)
- Technical Skills (organized by category, prioritized based on JD)
- Education
- Certifications (if relevant)

## Writing Style
- Use varied action verbs: Mix "Built", "Developed", "Worked on", "Contributed to"
- Use natural quantifiers: "roughly 25%", "around 10K users", "approximately 3 months"
- Include collaboration: "Worked with team of 12", "Collaborated with architects"
- Show progression: "Initially", "Later", "Eventually", "Over time"
- Use realistic metrics: 15-30% improvements, 99.9% uptime
"""
    
    def load_experience_database(self, experience_file: Path) -> str:
        """Load user's experience database from markdown file"""
        if not experience_file.exists():
            raise FileNotFoundError(f"Experience database not found: {experience_file}")
        
        with open(experience_file, 'r', encoding='utf-8') as f:
            return f.read()
    
    def load_job_description(self, jd_file: Path) -> str:
        """Load job description from file"""
        if not jd_file.exists():
            raise FileNotFoundError(f"Job description not found: {jd_file}")
        
        with open(jd_file, 'r', encoding='utf-8') as f:
            return f.read()
    
    def generate_resume(self, job_description: str, experience_db: str, 
                       additional_instructions: str = "") -> str:
        """
        Generate a tailored resume using OpenAI API
        
        Args:
            job_description: The target job description
            experience_db: User's experience database in markdown
            additional_instructions: Any additional customization instructions
        
        Returns:
            Generated resume in markdown format
        """
        system_prompt = f"""{self.agent_prompt}

You are an expert resume writer. Your task is to create a tailored, ATS-friendly resume 
based on the user's experience database and a specific job description.

Remember to:
1. Extract key requirements and keywords from the job description
2. Match user's experience to job requirements authentically
3. Use natural, non-robotic language
4. Optimize for ATS while maintaining human readability
5. Include realistic metrics and achievements
"""

        user_message = f"""Please create a tailored resume for the following job:

# JOB DESCRIPTION:
{job_description}

# MY EXPERIENCE DATABASE:
{experience_db}

{additional_instructions}

Generate a complete, professional resume in Markdown format that:
- Achieves 90%+ keyword coverage from the job description
- Maintains authenticity (only use real companies and experiences from my database)
- Uses natural language (avoid robotic AI patterns)
- Is ATS-optimized
- Highlights relevant achievements with realistic metrics
"""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ],
                temperature=0.7,
                max_tokens=2500
            )
            
            return response.choices[0].message.content
        
        except Exception as e:
            raise Exception(f"Error generating resume: {str(e)}")
    
    def save_resume(self, resume_content: str, output_path: Path) -> Path:
        """Save the generated resume to a file"""
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(resume_content)
        
        return output_path
    
    def extract_keywords(self, job_description: str) -> Dict[str, List[str]]:
        """Extract key requirements and keywords from job description"""
        system_prompt = "You are an expert at analyzing job descriptions and extracting key requirements."
        
        user_message = f"""Analyze this job description and extract:
1. Critical skills (mentioned 3+ times or in requirements)
2. Important technical skills
3. Soft skills
4. Nice-to-have qualifications

Job Description:
{job_description}

Return the analysis in JSON format with keys: critical_skills, technical_skills, soft_skills, nice_to_have
"""
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ],
                temperature=0.3,
                max_tokens=1000
            )
            
            content = response.choices[0].message.content
            # Try to parse JSON from the response
            try:
                return json.loads(content)
            except json.JSONDecodeError:
                # If not valid JSON, return the raw text
                return {"raw_analysis": content}
        
        except Exception as e:
            print(f"Warning: Could not extract keywords: {str(e)}")
            return {}


def main():
    """CLI interface for the Resume Fine-Tuner"""
    parser = argparse.ArgumentParser(
        description="Resume Fine-Tuner - AI-powered resume optimization using OpenAI API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate resume for a specific job
  python resume_fine_tuner.py -e workspace/experience-db/software-engineer.md \\
                              -j workspace/job-descriptions/senior-backend-engineer.md \\
                              -o workspace/outputs/tailored-resume.md
  
  # Use GPT-3.5-turbo (cheaper)
  python resume_fine_tuner.py -e experience.md -j job.md -m gpt-3.5-turbo
  
  # Extract keywords only
  python resume_fine_tuner.py -j job.md --keywords-only
"""
    )
    
    parser.add_argument('-e', '--experience', type=str,
                       help='Path to experience database markdown file')
    parser.add_argument('-j', '--job', type=str, required=True,
                       help='Path to job description file')
    parser.add_argument('-o', '--output', type=str,
                       help='Output file path (default: workspace/outputs/resume-{timestamp}.md)')
    parser.add_argument('-m', '--model', type=str, default='gpt-4',
                       choices=['gpt-4', 'gpt-4-turbo', 'gpt-3.5-turbo'],
                       help='OpenAI model to use (default: gpt-4)')
    parser.add_argument('--keywords-only', action='store_true',
                       help='Only extract keywords from job description')
    parser.add_argument('--api-key', type=str,
                       help='OpenAI API key (or set OPENAI_API_KEY env variable)')
    
    args = parser.parse_args()
    
    try:
        # Initialize the agent
        agent = ResumeFIneTuner(api_key=args.api_key, model=args.model)
        
        # Load job description
        job_description = agent.load_job_description(Path(args.job))
        
        # If keywords-only mode
        if args.keywords_only:
            print("Extracting keywords from job description...")
            keywords = agent.extract_keywords(job_description)
            print("\n=== KEYWORD ANALYSIS ===")
            print(json.dumps(keywords, indent=2))
            return
        
        # Load experience database
        if not args.experience:
            print("Error: --experience is required for resume generation")
            sys.exit(1)
        
        experience_db = agent.load_experience_database(Path(args.experience))
        
        # Generate resume
        print(f"Generating resume using {args.model}...")
        resume = agent.generate_resume(job_description, experience_db)
        
        # Determine output path
        if args.output:
            output_path = Path(args.output)
        else:
            timestamp = datetime.now().strftime("%Y-%m-%d-%H%M%S")
            output_path = Path(__file__).parent / "workspace" / "outputs" / f"resume-{timestamp}.md"
        
        # Save resume
        saved_path = agent.save_resume(resume, output_path)
        
        print(f"\n✅ Resume generated successfully!")
        print(f"📄 Saved to: {saved_path}")
        print(f"\nPreview (first 500 chars):")
        print("=" * 50)
        print(resume[:500])
        print("=" * 50)
        
    except Exception as e:
        print(f"❌ Error: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
