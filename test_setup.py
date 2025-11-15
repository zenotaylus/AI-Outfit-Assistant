"""
AI Hackathon Setup Test Script
Run this to verify your Python environment is ready
"""

import sys

print("=" * 60)
print("AI HACKATHON SETUP VERIFICATION")
print("=" * 60)
print(f"\nPython Version: {sys.version}")
print("-" * 60)

packages = {
    "numpy": "NumPy (numerical computing)",
    "pandas": "Pandas (data manipulation)",
    "matplotlib": "Matplotlib (plotting)",
    "sklearn": "Scikit-learn (machine learning)",
    "torch": "PyTorch (deep learning)",
    "transformers": "Hugging Face Transformers (NLP)",
    "openai": "OpenAI API client",
    "anthropic": "Anthropic API client",
    "langchain": "LangChain (AI app framework)",
    "fastapi": "FastAPI (web framework)",
    "jupyter": "Jupyter Notebook",
    "requests": "Requests (HTTP library)",
}

installed = []
missing = []

print("\nChecking installed packages:")
print("-" * 60)

for package, description in packages.items():
    try:
        __import__(package)
        print(f"✅ {description}")
        installed.append(package)
    except ImportError:
        print(f"❌ {description}")
        missing.append(package)

print("\n" + "=" * 60)
print(f"SUMMARY: {len(installed)}/{len(packages)} packages installed")
print("=" * 60)

if missing:
    print("\n⚠️  Missing packages:")
    for pkg in missing:
        print(f"   - {pkg}")
    print("\nTo install missing packages, run:")
    print(f"   pip install {' '.join(missing)}")
else:
    print("\n🎉 All recommended packages are installed!")
    print("You're ready for the AI Hackathon!")

print("\n" + "=" * 60)
