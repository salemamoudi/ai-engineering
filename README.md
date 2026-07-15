# AI Engineering from Scratch - Learning Journey

This repository contains my work as I progress through the **AI Engineering from Scratch** curriculum.

## 📚 Curriculum
### Phase 0: Setup & Tooling

#### Lesson 01: Dev Environment
- Set up WSL Ubuntu on Windows
- Installed Python 3.12 with `uv`
- Set up Node.js 22 with `fnm`
- Installed Rust via `rustup`
- Installed Julia
- Created virtual environment
- Verified all tools working
- Created `requirements.txt`

#### Lesson 02: Git & Collaboration
- Configured Git with user name and email
- Generated SSH keys for GitHub
- Created GitHub repository
- Initialized local Git repository
- Learned branching strategies (main, develop, feature)
- Created `.gitignore` for AI projects
- Made first commit and pushed to GitHub
- Learned Pull Request workflow

#### Lesson 03: GPU Setup & Cloud
- Installed NVIDIA drivers for WSL
- Set up CUDA toolkit
- Installed PyTorch with CUDA support
- Verified GPU detection with `torch.cuda.is_available()`
- Created GPU benchmark scripts
- Tested matrix multiplication on GPU
- Set up Google Colab for free GPU
- Learned cloud GPU options (AWS, GCP, Lambda Labs)

#### Lesson 04: APIs & Keys
- Created secure `.env` file for API keys
- Set up OpenAI API key
- Set up Anthropic Claude API key
- Set up Hugging Face API key
- Created `config.py` for loading environment variables
- Built unified API client
- Created API test scripts
- Learned security best practices
- Never commit `.env` to Git
#### Lesson 05: Jupyter Notebooks
- Installed Jupyter Lab
- Created interactive notebooks
- Integrated with Ollama for AI
- Built interactive widgets
- Learned Markdown cells
- Used magic commands (`%matplotlib inline`, `%timeit`)
- Created visualizations with matplotlib
#### Lesson 06: Python Environments
- Understood virtual environments
- Used `uv` for dependency management
- Created `requirements.txt`
- Managed multiple environments
- Learned PEP 668 (externally-managed-environment)
- Created `env_manager.py` script
- Updated `.gitignore` for environments
#### Lesson 07: Docker for AI
- Installed Docker Engine
- Set up NVIDIA Container Toolkit
- Created Dockerfile for AI environment
- Built Docker image with CUDA support
- Ran containers with GPU access
- Mounted volumes for code persistence
- Learned `.dockerignore` best practices
- Tested PyTorch inside container
#### Lesson 08: Editor Setup
- Set up VS Code with WSL Remote
- Installed Python, Jupyter, GitLens extensions
- Configured settings.json for AI development
- Learned keyboard shortcuts
- Created .vscode workspace settings
- Installed helpful extensions (Prettier, Black, Error Lens)
- Set up Jupyter in VS Code
- Tested Python debugging
## 📊 Progress Tracker

| Phase | Topic | Status |
|-------|-------|--------|
| **Phase 0** | **Setup & Tooling** | ✅ **COMPLETE** |
| Lesson 01 | Dev Environment | ✅ Done |
| Lesson 02 | Git & Collaboration | ✅ Done |
| Lesson 03 | GPU Setup & Cloud | ✅ Done |
| Lesson 04 | APIs & Keys | ✅ Done |
| Lesson 05 | Jupyter Notebooks | ✅ Done |
| Lesson 06 | Python Environments | ✅ Done |
| Lesson 07 | Docker for AI | ✅ Done |
| Lesson 08 | Editor Setup | ✅ Done |
## 🛠️ Environment

- **OS:** WSL Ubuntu 22.04
- **Python:** 3.12 (via uv)
- **Node.js:** 22 (via fnm)
- **Rust:** Latest (via rustup)

## 📦 Key Dependencies

- numpy
- matplotlib
- scikit-learn
- pandas
- jupyter

## 📝 Notes

- All work is done in WSL Ubuntu
- Virtual environment: `.venv/`
- Python packages listed in `requirements.txt`
