#!/bin/bash

# Resume Fine-Tuner Agent - Setup Script
# This script sets up everything you need to use the agent

set -e  # Exit on error

echo "╔══════════════════════════════════════════════════════════════════╗"
echo "║        Resume Fine-Tuner Agent - Setup & Installation           ║"
echo "╚══════════════════════════════════════════════════════════════════╝"
echo ""

# Check Python version
echo "🔍 Checking Python version..."
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
    PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
    echo "   ✅ Python found: $PYTHON_VERSION"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
    PYTHON_VERSION=$(python --version 2>&1 | awk '{print $2}')
    echo "   ✅ Python found: $PYTHON_VERSION"
else
    echo "   ❌ Python not found. Please install Python 3.8 or higher."
    exit 1
fi

echo ""

# Check if in correct directory
echo "🔍 Checking current directory..."
if [ ! -f "resume_fine_tuner.py" ]; then
    echo "   ❌ Error: Not in the correct directory!"
    echo "   Please run this script from: episodes/02-resume-fine-tuner/"
    echo "   "
    echo "   Run: cd episodes/02-resume-fine-tuner"
    echo "   Then: bash setup_agent.sh"
    exit 1
fi
echo "   ✅ Correct directory"
echo ""

# Install Python dependencies
echo "📦 Installing Python dependencies..."
echo "   Installing: openai, python-docx, markdown"
echo ""

if $PYTHON_CMD -m pip install -r requirements.txt --quiet; then
    echo "   ✅ Dependencies installed successfully"
else
    echo "   ⚠️  Warning: Some packages may have failed to install"
    echo "   You can try manually: pip install openai python-docx markdown"
fi
echo ""

# Check for OpenAI API key
echo "🔑 Checking for OpenAI API key..."
if [ -z "$OPENAI_API_KEY" ]; then
    echo "   ⚠️  OPENAI_API_KEY not set!"
    echo ""
    echo "   You need an OpenAI API key to use this agent."
    echo "   "
    echo "   To set it up:"
    echo "   1. Get your API key from: https://platform.openai.com/api-keys"
    echo "   2. Run: export OPENAI_API_KEY='sk-your-key-here'"
    echo "   3. Or add it to your ~/.bashrc or ~/.zshrc file"
    echo ""
    echo "   ⏭️  Continuing setup (you can add the key later)"
else
    echo "   ✅ API key found (starts with: ${OPENAI_API_KEY:0:8}...)"
fi
echo ""

# Test the script
echo "🧪 Testing the agent script..."
if $PYTHON_CMD resume_fine_tuner.py --help &> /dev/null; then
    echo "   ✅ Agent script works!"
else
    echo "   ⚠️  Agent test failed - but dependencies are installed"
    echo "   Make sure you have set OPENAI_API_KEY before using"
fi
echo ""

# Check workspace structure
echo "📁 Checking workspace structure..."
WORKSPACE_OK=true

if [ ! -d "workspace/experience-db" ]; then
    echo "   ❌ Missing: workspace/experience-db/"
    WORKSPACE_OK=false
else
    echo "   ✅ workspace/experience-db/ exists"
fi

if [ ! -d "workspace/job-descriptions" ]; then
    echo "   ❌ Missing: workspace/job-descriptions/"
    WORKSPACE_OK=false
else
    echo "   ✅ workspace/job-descriptions/ exists"
fi

if [ ! -d "workspace/outputs" ]; then
    echo "   ⚠️  Creating: workspace/outputs/"
    mkdir -p workspace/outputs
fi
echo "   ✅ workspace/outputs/ exists"

echo ""

# Summary
echo "╔══════════════════════════════════════════════════════════════════╗"
echo "║                        SETUP COMPLETE!                           ║"
echo "╚══════════════════════════════════════════════════════════════════╝"
echo ""

if [ -z "$OPENAI_API_KEY" ]; then
    echo "⚠️  NEXT STEP: Set your OpenAI API key"
    echo ""
    echo "   export OPENAI_API_KEY='sk-your-actual-key-here'"
    echo ""
    echo "   Get your key from: https://platform.openai.com/api-keys"
    echo ""
else
    echo "✅ You're all set! Ready to generate resumes."
    echo ""
fi

echo "📖 HOW TO USE:"
echo ""
echo "   1. Fill out your experience:"
echo "      Edit: workspace/experience-db/YOUR-EXPERIENCE.md"
echo ""
echo "   2. Save a job description:"
echo "      Create: workspace/job-descriptions/company-role.md"
echo ""
echo "   3. Generate your resume:"
echo "      $PYTHON_CMD resume_fine_tuner.py \\"
echo "        -e workspace/experience-db/YOUR-EXPERIENCE.md \\"
echo "        -j workspace/job-descriptions/company-role.md \\"
echo "        -o workspace/outputs/my-resume.md"
echo ""
echo "📚 For detailed instructions, read: HOW_TO_USE.md"
echo ""
echo "🎉 Happy job hunting!"
echo ""
