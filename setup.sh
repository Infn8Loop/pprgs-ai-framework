#!/bin/bash

# PPRGS Framework - Initial Setup Script
# Run this to set up your development environment

set -e  # Exit on error

echo "╔════════════════════════════════════════════════════════════╗"
echo "║  PPRGS Framework - Setup Script                            ║"
echo "║  Making wisdom the goal since 2025                         ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Check Python version
echo "🔍 Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
required_version="3.8"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" = "$required_version" ]; then 
    echo "✅ Python $python_version detected"
else
    echo "❌ Python 3.8+ required. Found: $python_version"
    exit 1
fi

# Create virtual environment
echo ""
echo "📦 Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "⚠️  Virtual environment already exists"
fi

# Activate virtual environment
echo ""
echo "🔌 Activating virtual environment..."
source venv/bin/activate || {
    echo "❌ Failed to activate virtual environment"
    exit 1
}
echo "✅ Virtual environment activated"

# Upgrade pip
echo ""
echo "⬆️  Upgrading pip..."
pip install --upgrade pip -q
echo "✅ Pip upgraded"

# Install dependencies
echo ""
echo "📥 Installing dependencies..."
pip install -r requirements.txt -q
echo "✅ Dependencies installed"

# Create directory structure
echo ""
echo "📁 Creating directory structure..."

directories=(
    "implementations/gpt4/system_prompts"
    "implementations/gpt4/functions"
    "implementations/aws-bedrock/step-functions"
    "implementations/aws-bedrock/lambda"
    "implementations/aws-bedrock/cloudformation"
    "implementations/gemini/tools"
    "implementations/gemini/prompts"
    "implementations/grok/multi_agent_config"
    "experiments/experiment_1_stability"
    "experiments/experiment_2_enrichment"
    "experiments/experiment_3_strategic_planning"
    "experiments/experiment_4_existential_conflict"
    "metrics"
    "tests/unit"
    "tests/integration"
    "results/experiment_1"
    "results/experiment_2"
    "results/experiment_3"
    "results/experiment_4"
    "docs/architecture_diagrams"
    "docs/experimental_protocols"
    "paper"
)

for dir in "${directories[@]}"; do
    mkdir -p "$dir"
done

echo "✅ Directory structure created"

# Create .env template if it doesn't exist
echo ""
echo "🔐 Setting up environment variables..."
if [ ! -f ".env" ]; then
    cat > .env << 'EOF'
# PPRGS Framework Environment Variables
# Copy this to .env and fill in your actual values

# OpenAI (for GPT-4 implementation)
OPENAI_API_KEY=your-openai-api-key-here

# AWS (for Bedrock implementation)
AWS_ACCESS_KEY_ID=your-aws-access-key-here
AWS_SECRET_ACCESS_KEY=your-aws-secret-key-here
AWS_DEFAULT_REGION=us-east-1

# Google (for Gemini implementation