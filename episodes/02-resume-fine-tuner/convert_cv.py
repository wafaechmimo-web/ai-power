#!/usr/bin/env python3
"""
CV Converter - Convert user's CV into agent format

This script helps convert various CV formats into the structure
expected by the Resume Fine-Tuner agent.
"""

import sys
import re
from pathlib import Path
from datetime import datetime


def print_header():
    """Print welcome header"""
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║           CV Converter for Resume Fine-Tuner Agent          ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print()


def read_cv_file(filepath):
    """Read CV from file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"❌ Error: File not found: {filepath}")
        return None
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return None


def interactive_cv_builder():
    """Interactive mode to build CV section by section"""
    print("🎯 Interactive CV Builder")
    print("I'll guide you through each section.")
    print()
    
    cv_data = {}
    
    # Personal Information
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("📋 PERSONAL INFORMATION")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    cv_data['name'] = input("Full Name: ").strip()
    cv_data['email'] = input("Email: ").strip()
    cv_data['phone'] = input("Phone: ").strip()
    cv_data['location'] = input("Location (City, State): ").strip()
    cv_data['linkedin'] = input("LinkedIn URL (optional): ").strip()
    cv_data['github'] = input("GitHub URL (optional): ").strip()
    cv_data['website'] = input("Personal Website (optional): ").strip()
    
    # Professional Summary
    print()
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("💼 PROFESSIONAL SUMMARY")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Write 2-3 sentences about your professional background:")
    cv_data['summary'] = input("> ").strip()
    
    # Work Experience
    print()
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("🏢 WORK EXPERIENCE")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    cv_data['experience'] = []
    while True:
        print(f"\nJob #{len(cv_data['experience']) + 1}")
        job = {}
        job['company'] = input("Company Name: ").strip()
        if not job['company']:
            break
        job['title'] = input("Job Title: ").strip()
        job['location'] = input("Location: ").strip()
        job['start_date'] = input("Start Date (e.g., Jan 2020): ").strip()
        job['end_date'] = input("End Date (or 'Present'): ").strip()
        
        print("Achievements/Responsibilities (one per line, empty line to finish):")
        job['achievements'] = []
        while True:
            achievement = input("  - ").strip()
            if not achievement:
                break
            job['achievements'].append(achievement)
        
        job['technologies'] = input("Technologies Used: ").strip()
        cv_data['experience'].append(job)
        
        more = input("\nAdd another job? (y/n): ").strip().lower()
        if more != 'y':
            break
    
    # Education
    print()
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("🎓 EDUCATION")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    cv_data['education'] = []
    while True:
        print(f"\nDegree #{len(cv_data['education']) + 1}")
        edu = {}
        edu['degree'] = input("Degree (e.g., Bachelor of Science in Computer Science): ").strip()
        if not edu['degree']:
            break
        edu['school'] = input("School/University: ").strip()
        edu['year'] = input("Graduation Year: ").strip()
        edu['gpa'] = input("GPA (optional): ").strip()
        cv_data['education'].append(edu)
        
        more = input("\nAdd another degree? (y/n): ").strip().lower()
        if more != 'y':
            break
    
    # Skills
    print()
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("💻 SKILLS")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    cv_data['skills'] = {}
    cv_data['skills']['languages'] = input("Programming Languages: ").strip()
    cv_data['skills']['frameworks'] = input("Frameworks & Libraries: ").strip()
    cv_data['skills']['tools'] = input("Tools & Platforms: ").strip()
    cv_data['skills']['databases'] = input("Databases: ").strip()
    
    return cv_data


def generate_agent_format(cv_data):
    """Convert CV data to agent's expected format"""
    output = []
    
    # Header
    output.append(f"# {cv_data.get('name', 'Your Name')} - Experience Database")
    output.append("")
    output.append("## Personal Information")
    output.append("")
    output.append(f"**Full Name**: {cv_data.get('name', '')}")
    output.append(f"**Location**: {cv_data.get('location', '')}")
    output.append(f"**Email**: {cv_data.get('email', '')}")
    output.append(f"**Phone**: {cv_data.get('phone', '')}")
    
    if cv_data.get('linkedin'):
        output.append(f"**LinkedIn**: {cv_data['linkedin']}")
    if cv_data.get('github'):
        output.append(f"**GitHub**: {cv_data['github']}")
    if cv_data.get('website'):
        output.append(f"**Website**: {cv_data['website']}")
    
    output.append("")
    output.append("---")
    output.append("")
    
    # Professional Summary
    if cv_data.get('summary'):
        output.append("## Professional Summary")
        output.append("")
        output.append(cv_data['summary'])
        output.append("")
        output.append("---")
        output.append("")
    
    # Work Experience
    if cv_data.get('experience'):
        output.append("## Work Experience")
        output.append("")
        
        for i, job in enumerate(cv_data['experience']):
            if i == 0:
                output.append("### Current/Most Recent Job")
            else:
                output.append(f"### Previous Job #{i}")
            output.append("")
            output.append(f"**Company Name**: {job.get('company', '')}")
            output.append(f"**Job Title**: {job.get('title', '')}")
            output.append(f"**Location**: {job.get('location', '')}")
            output.append(f"**Period**: {job.get('start_date', '')} - {job.get('end_date', '')}")
            output.append("")
            
            if job.get('achievements'):
                output.append("**Key Achievements**:")
                for achievement in job['achievements']:
                    output.append(f"- {achievement}")
                output.append("")
            
            if job.get('technologies'):
                output.append(f"**Technologies Used**: {job['technologies']}")
            
            output.append("")
            output.append("---")
            output.append("")
    
    # Education
    if cv_data.get('education'):
        output.append("## Education")
        output.append("")
        
        for edu in cv_data['education']:
            output.append(f"**{edu.get('degree', '')}** - {edu.get('school', '')} ({edu.get('year', '')})")
            if edu.get('gpa'):
                output.append(f"- GPA: {edu['gpa']}")
            output.append("")
        
        output.append("---")
        output.append("")
    
    # Technical Skills
    if cv_data.get('skills'):
        output.append("## Technical Skills")
        output.append("")
        
        if cv_data['skills'].get('languages'):
            output.append("### Programming Languages")
            output.append(cv_data['skills']['languages'])
            output.append("")
        
        if cv_data['skills'].get('frameworks'):
            output.append("### Frameworks & Libraries")
            output.append(cv_data['skills']['frameworks'])
            output.append("")
        
        if cv_data['skills'].get('tools'):
            output.append("### Tools & Platforms")
            output.append(cv_data['skills']['tools'])
            output.append("")
        
        if cv_data['skills'].get('databases'):
            output.append("### Databases")
            output.append(cv_data['skills']['databases'])
            output.append("")
    
    return "\n".join(output)


def save_output(content, output_path):
    """Save the converted CV to file"""
    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"❌ Error saving file: {e}")
        return False


def main():
    """Main function"""
    print_header()
    
    print("This tool helps convert your CV into the Resume Fine-Tuner agent format.")
    print()
    print("Options:")
    print("  1. Interactive mode (I'll ask you questions)")
    print("  2. Convert from filled MY-CV-FORM.md")
    print("  3. Convert from text file")
    print()
    
    choice = input("Choose option (1-3): ").strip()
    
    if choice == '1':
        print("\n🎯 Starting interactive mode...")
        cv_data = interactive_cv_builder()
        
    elif choice == '2':
        form_path = Path('MY-CV-FORM.md')
        if not form_path.exists():
            print(f"❌ Error: {form_path} not found")
            print("Please fill out MY-CV-FORM.md first!")
            return 1
        
        print("📝 Reading MY-CV-FORM.md...")
        # Parse the form (simplified - would need more robust parsing)
        content = read_cv_file(form_path)
        if not content:
            return 1
        
        print("⚠️  Note: Automatic parsing is basic. Please review the output!")
        print("Consider using interactive mode (option 1) for better results.")
        return 0
        
    elif choice == '3':
        filepath = input("Enter path to your CV file: ").strip()
        content = read_cv_file(filepath)
        if not content:
            return 1
        
        print("⚠️  Note: Automatic parsing is basic. Please review the output!")
        print("Consider using interactive mode (option 1) for better results.")
        return 0
        
    else:
        print("❌ Invalid choice")
        return 1
    
    # Generate output
    print("\n✨ Converting to agent format...")
    output = generate_agent_format(cv_data)
    
    # Save to file
    output_name = cv_data.get('name', 'user').lower().replace(' ', '-')
    output_path = Path(f"workspace/experience-db/{output_name}-experience.md")
    
    print(f"\n💾 Saving to: {output_path}")
    if save_output(output, output_path):
        print("✅ Conversion complete!")
        print()
        print("Next steps:")
        print(f"1. Review the file: {output_path}")
        print("2. Make any necessary edits")
        print("3. Use it with the agent:")
        print()
        print(f"   python resume_fine_tuner.py \\")
        print(f"     -e {output_path} \\")
        print(f"     -j workspace/job-descriptions/job.md \\")
        print(f"     -o workspace/outputs/resume.md")
        print()
        return 0
    else:
        return 1


if __name__ == "__main__":
    sys.exit(main())
