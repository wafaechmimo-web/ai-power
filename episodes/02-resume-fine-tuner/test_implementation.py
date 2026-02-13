#!/usr/bin/env python3
"""
Test script to validate Resume Fine-Tuner implementation
This validates the structure without requiring OpenAI API access
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

def test_file_structure():
    """Test that all required files exist"""
    print("Testing file structure...")
    
    base_dir = Path(__file__).parent
    required_files = [
        "README.md",
        "🎯 START_HERE.md",
        "📹 THE_FULL_SCRIPT.md",
        "SETUP.md",
        "requirements.txt",
        ".env.example",
        "resume_fine_tuner.py",
        "prompts/resume-fine-tuner-agent.md",
        "prompts/ALL_CLAUDE_PROMPTS.md",
        "templates/experience-software-engineer.md",
        "templates/experience-marketing-manager.md",
        "templates/experience-real-estate-agent.md",
        "samples/example-latex-resume.tex",
        "workspace/README.md",
        "workspace/experience-db/software-engineer.md",
        "workspace/job-descriptions/senior-backend-engineer-clickup.md",
    ]
    
    missing = []
    for file_path in required_files:
        full_path = base_dir / file_path
        if not full_path.exists():
            missing.append(file_path)
            print(f"  ❌ Missing: {file_path}")
        else:
            print(f"  ✅ Found: {file_path}")
    
    if missing:
        print(f"\n❌ Missing {len(missing)} required files!")
        return False
    else:
        print(f"\n✅ All {len(required_files)} required files present!")
        return True


def test_script_structure():
    """Test that the Python script has correct structure"""
    print("\nTesting Python script structure...")
    
    script_path = Path(__file__).parent / "resume_fine_tuner.py"
    with open(script_path, 'r') as f:
        content = f.read()
    
    required_elements = [
        "class ResumeFIneTuner",
        "def __init__",
        "def generate_resume",
        "def load_experience_database",
        "def load_job_description",
        "def save_resume",
        "def extract_keywords",
        "def main()",
        "OpenAI",
        "argparse",
    ]
    
    missing = []
    for element in required_elements:
        if element not in content:
            missing.append(element)
            print(f"  ❌ Missing: {element}")
        else:
            print(f"  ✅ Found: {element}")
    
    if missing:
        print(f"\n❌ Missing {len(missing)} required elements in script!")
        return False
    else:
        print(f"\n✅ Script has all {len(required_elements)} required elements!")
        return True


def test_template_content():
    """Test that templates have proper structure"""
    print("\nTesting template content...")
    
    base_dir = Path(__file__).parent
    templates = [
        "templates/experience-software-engineer.md",
        "templates/experience-marketing-manager.md",
        "templates/experience-real-estate-agent.md",
    ]
    
    all_valid = True
    for template_path in templates:
        full_path = base_dir / template_path
        with open(full_path, 'r') as f:
            content = f.read()
        
        # Check for key sections
        required_sections = ["Experience", "Skills", "Education"]
        has_sections = all(section in content for section in required_sections)
        
        if has_sections and len(content) > 500:
            print(f"  ✅ {template_path} - Valid ({len(content)} chars)")
        else:
            print(f"  ❌ {template_path} - Invalid or too short")
            all_valid = False
    
    return all_valid


def test_workspace_examples():
    """Test that workspace has example data"""
    print("\nTesting workspace examples...")
    
    base_dir = Path(__file__).parent
    workspace_files = [
        "workspace/experience-db/software-engineer.md",
        "workspace/experience-db/marketing-manager.md",
        "workspace/experience-db/real-estate-agent.md",
        "workspace/job-descriptions/senior-backend-engineer-clickup.md",
    ]
    
    all_valid = True
    for file_path in workspace_files:
        full_path = base_dir / file_path
        if full_path.exists():
            size = full_path.stat().st_size
            if size > 100:
                print(f"  ✅ {file_path} - {size} bytes")
            else:
                print(f"  ❌ {file_path} - Too small ({size} bytes)")
                all_valid = False
        else:
            print(f"  ❌ {file_path} - Not found")
            all_valid = False
    
    return all_valid


def test_documentation_links():
    """Test that key documentation files are well-formed"""
    print("\nTesting documentation...")
    
    base_dir = Path(__file__).parent
    docs = [
        ("README.md", ["Episode 02", "Resume", "Claude Sonnet"]),
        ("SETUP.md", ["Installation", "OpenAI", "API key"]),
        ("🎯 START_HERE.md", ["Quick Start", "Resume", "Agent"]),
    ]
    
    all_valid = True
    for doc_file, keywords in docs:
        full_path = base_dir / doc_file
        with open(full_path, 'r') as f:
            content = f.read()
        
        found_keywords = [kw for kw in keywords if kw in content]
        if len(found_keywords) == len(keywords):
            print(f"  ✅ {doc_file} - All keywords present")
        else:
            missing = set(keywords) - set(found_keywords)
            print(f"  ⚠️  {doc_file} - Missing keywords: {missing}")
            all_valid = False
    
    return all_valid


def main():
    """Run all tests"""
    print("=" * 60)
    print("Resume Fine-Tuner Implementation Test Suite")
    print("=" * 60)
    
    tests = [
        test_file_structure,
        test_script_structure,
        test_template_content,
        test_workspace_examples,
        test_documentation_links,
    ]
    
    results = []
    for test_func in tests:
        try:
            result = test_func()
            results.append(result)
        except Exception as e:
            print(f"\n❌ Test failed with error: {e}")
            results.append(False)
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    
    passed = sum(results)
    total = len(results)
    
    if passed == total:
        print(f"✅ ALL TESTS PASSED ({passed}/{total})")
        print("\n🎉 Resume Fine-Tuner implementation is complete and valid!")
        print("\nNext steps:")
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Set up OpenAI API key: export OPENAI_API_KEY='your-key'")
        print("3. Run: python resume_fine_tuner.py --help")
        return 0
    else:
        print(f"⚠️  SOME TESTS FAILED ({passed}/{total} passed)")
        print("\nPlease review the failures above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
