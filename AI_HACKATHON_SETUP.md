# AI Hackathon Setup Guide

## ✅ Current Installation Status

### Core Tools (Already Installed)
- **Node.js**: v24.11.0 ✅
- **npm**: 11.6.1 ✅ (can update to 11.6.2)
- **Python**: 3.13.5 ✅
- **pip**: 25.1.1 ✅
- **Git**: 2.51.2 ✅
- **VS Code**: Installed ✅
- **Cline AI Extension**: Active ✅

---

## 📦 Recommended Python AI/ML Libraries

### Essential AI Libraries
```bash
# Core ML/AI frameworks
pip install numpy pandas matplotlib seaborn

# Machine Learning
pip install scikit-learn

# Deep Learning (choose based on your needs)
pip install torch torchvision torchaudio  # PyTorch (recommended)
# OR
pip install tensorflow keras  # TensorFlow

# Natural Language Processing
pip install transformers  # Hugging Face transformers
pip install nltk spacy

# Computer Vision
pip install opencv-python pillow

# Data Science Tools
pip install jupyter notebook ipython

# API Development
pip install fastapi uvicorn flask

# Utilities
pip install requests python-dotenv tqdm
```

### Popular AI/LLM APIs
```bash
# OpenAI
pip install openai

# Anthropic (Claude)
pip install anthropic

# Google AI
pip install google-generativeai

# LangChain (for AI app development)
pip install langchain langchain-openai langchain-community

# Vector Databases
pip install chromadb pinecone-client
```

---

## 📦 Recommended Node.js/npm Tools

### Development Tools
```bash
# TypeScript
npm install -g typescript ts-node

# Build tools
npm install -g vite

# API testing
npm install -g httpie

# Code quality
npm install -g prettier eslint
```

### AI/ML JavaScript Libraries (for projects)
```bash
# In your project directory:
npm install @tensorflow/tfjs
npm install @huggingface/inference
npm install openai
npm install @anthropic-ai/sdk
npm install langchain
```

---

## 🚀 Quick Installation Commands

### Minimal AI Setup (Fast Start)
```bash
# Python essentials
pip install numpy pandas matplotlib jupyter openai anthropic transformers langchain

# Node.js essentials
npm install -g typescript
```

### Full AI Setup (Comprehensive)
```bash
# Python - all recommended packages
pip install numpy pandas matplotlib seaborn scikit-learn torch torchvision transformers nltk spacy opencv-python pillow jupyter notebook fastapi uvicorn requests python-dotenv openai anthropic google-generativeai langchain langchain-openai chromadb

# Node.js - global tools
npm install -g typescript ts-node vite prettier
```

---

## 🔧 Additional Recommendations

### 1. API Keys to Prepare
- **OpenAI**: https://platform.openai.com/api-keys
- **Anthropic (Claude)**: https://console.anthropic.com/
- **Google AI**: https://makersuite.google.com/app/apikey
- **Hugging Face**: https://huggingface.co/settings/tokens

### 2. Useful VS Code Extensions
- Python (Microsoft)
- Pylance
- Jupyter
- ESLint
- Prettier
- GitLens
- Thunder Client (API testing)
- REST Client

### 3. Optional Tools
```bash
# Docker (for containerization)
# Download from: https://www.docker.com/products/docker-desktop

# Postman (API testing alternative)
# Download from: https://www.postman.com/downloads/

# Anaconda (Python environment management)
# Download from: https://www.anaconda.com/download
```

### 4. GPU Support for Deep Learning (if you have NVIDIA GPU)
```bash
# PyTorch with CUDA
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# TensorFlow with GPU
pip install tensorflow[and-cuda]
```

---

## 📝 Quick Test Commands

### Test Python Setup
```python
# Save as test_setup.py and run: python test_setup.py
import sys
print(f"Python: {sys.version}")

try:
    import numpy as np
    print("✅ NumPy installed")
except:
    print("❌ NumPy missing")

try:
    import pandas as pd
    print("✅ Pandas installed")
except:
    print("❌ Pandas missing")

try:
    import torch
    print("✅ PyTorch installed")
except:
    print("❌ PyTorch missing")

try:
    import transformers
    print("✅ Transformers installed")
except:
    print("❌ Transformers missing")
```

### Test Node.js Setup
```javascript
// Save as test_setup.js and run: node test_setup.js
console.log(`Node.js: ${process.version}`);
console.log('✅ Node.js working');
```

---

## 🎯 Recommended Installation Order

1. **Update npm** (optional but recommended):
   ```bash
   npm install -g npm@11.6.2
   ```

2. **Install Python AI essentials**:
   ```bash
   pip install numpy pandas matplotlib jupyter openai transformers langchain
   ```

3. **Install TypeScript**:
   ```bash
   npm install -g typescript
   ```

4. **Create a test project structure**:
   ```bash
   mkdir ai-hackathon-test
   cd ai-hackathon-test
   npm init -y
   ```

5. **Test everything** using the test commands above

---

## 💡 Tips for the Hackathon

1. **Use virtual environments** for Python projects:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

2. **Keep API keys secure** - use `.env` files and `.gitignore`

3. **Have backup plans** - download models/datasets before the event if possible

4. **Test your setup** before the hackathon starts

5. **Bookmark documentation**:
   - OpenAI: https://platform.openai.com/docs
   - Anthropic: https://docs.anthropic.com/
   - Hugging Face: https://huggingface.co/docs
   - LangChain: https://python.langchain.com/docs

---

## 🆘 Need Help?

- Check Python package conflicts: `pip check`
- Update all Python packages: `pip list --outdated`
- Clear npm cache: `npm cache clean --force`
- Reinstall package: `pip install --force-reinstall <package>`

Good luck at your AI Hackathon! 🚀
