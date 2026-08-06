# AI Engineering from Scratch - Learning Journey

This repository contains my work as I progress through the **AI Engineering from Scratch** curriculum
## 📚 Curriculum
### Phase 0: Setup & Tooling

### Lesson 01: Dev Environment
- ✅ Set up WSL Ubuntu on Windows
- ✅ Installed Python 3.12 with `uv` (10-100x faster than pip)
- ✅ Installed Node.js 22 with `fnm`
- ✅ Installed Rust with `rustup`
- ✅ Installed Julia
- ✅ Created virtual environment (`.venv`)
- ✅ Installed core Python packages: numpy, pandas, matplotlib, scikit-learn
- ✅ Verified all tools working

### Lesson 02: Git & Collaboration
- ✅ Configured Git with user name, email, and default branch (`main`)
- ✅ Generated SSH keys and added to GitHub
- ✅ Created GitHub repository
- ✅ Learned branching strategy: `main` → `develop` → `feature/*`
- ✅ Created `.gitignore` for AI projects
- ✅ Made first commit and pushed to GitHub
- ✅ Created and merged feature branches
- ✅ Learned Pull Request workflow

### Lesson 03: GPU Setup & Cloud
- ✅ Installed NVIDIA drivers for WSL
- ✅ Set up CUDA toolkit
- ✅ Installed PyTorch with CUDA support
- ✅ Verified GPU detection with `torch.cuda.is_available()`
- ✅ Created GPU benchmark scripts
- ✅ Set up Google Colab for free GPU access
- ✅ Learned cloud GPU options (AWS, GCP, Lambda Labs, Vast.ai)

### Lesson 04: APIs & Keys
- ✅ Created secure `.env` file with restricted permissions (`chmod 600`)
- ✅ Set up OpenAI API key
- ✅ Set up Anthropic Claude API key
- ✅ Set up Hugging Face API key (✅ Working)
- ✅ Created `config.py` for loading environment variables
- ✅ Built unified API client
- ✅ Created API test scripts
- ✅ Learned security best practices (never commit `.env`)
- ✅ Pushed `.env.example` with placeholders only

### Lesson 05: Jupyter Notebooks
- ✅ Installed Jupyter Lab and Jupyter Notebook
- ✅ Created interactive notebooks
- ✅ Integrated with Ollama for AI
- ✅ Built interactive widgets with `ipywidgets`
- ✅ Learned Markdown cells (headings, lists, checkboxes)
- ✅ Used magic commands (`%matplotlib inline`, `%timeit`)
- ✅ Created visualizations with matplotlib
- ✅ Created template notebook for future use

### Lesson 06: Python Environments
- ✅ Understood virtual environments (isolation, dependency management)
- ✅ Used `uv` for dependency management
- ✅ Created `requirements.txt` with all dependencies
- ✅ Installed from `requirements.txt`
- ✅ Managed multiple environments
- ✅ Created `env_manager.py` script
- ✅ Updated `.gitignore` for environments
- ✅ Learned PEP 668 (externally-managed-environment)

### Lesson 07: Docker for AI
- ✅ Installed Docker Engine
- ✅ Set up NVIDIA Container Toolkit for GPU access
- ✅ Created `.dockerignore` to exclude large files
- ✅ Created `Dockerfile` for AI environment
- ✅ Built Docker image with CUDA support
- ✅ Ran containers with GPU access
- ✅ Mounted volumes for code persistence
- ✅ Ran Jupyter from inside container
- ✅ Learned `.dockerignore` best practices
- ✅ Tested PyTorch inside container
- ✅ Created `docker_commands.sh` helper script

### Lesson 08: Editor Setup
- ✅ Set up VS Code with WSL Remote
- ✅ Installed Python, Jupyter, GitLens extensions
- ✅ Configured `settings.json` for AI development
- ✅ Learned keyboard shortcuts
- ✅ Created `.vscode` workspace settings
- ✅ Installed helpful extensions (Prettier, Black, Error Lens, Material Icon Theme)
- ✅ Set up Jupyter in VS Code
- ✅ Created debugging configuration (`launch.json`)

### Lesson 09: Data Management
- ✅ Installed `datasets`, `pandas`, `huggingface-hub`
- ✅ Learned to load datasets with `load_dataset()`
- ✅ Handled Hugging Face server timeout issues
- ✅ Created local datasets using pandas
- ✅ Explored dataset structure (features, size, splits)
- ✅ Analyzed data using pandas (`df.describe()`, `df.head()`)
- ✅ Calculated text statistics (length, word count)
- ✅ Built reusable data pipeline
- ✅ Split data into train/test sets with `train_test_split()`
- ✅ Generated datasets with Ollama

### Lesson 10: Terminal & Shell
- ✅ Mastered essential terminal commands (`pwd`, `ls`, `cd`, `cp`, `mv`, `rm`)
- ✅ Learned file viewing (`cat`, `head`, `tail`, `grep`)
- ✅ Practiced piping and redirection (`|`, `>`, `>>`)
- ✅ Set and used environment variables (`$PATH`, `$HOME`)
- ✅ Managed processes (`ps`, `top`, `kill`)
- ✅ Changed file permissions (`chmod`, `chown`)
- ✅ Created shell aliases for common commands
- ✅ Built shell script (`ai_utils.sh`)
- ✅ Created terminal cheat sheet

### Lesson 11: Linux for AI
- ✅ Learned Linux filesystem structure (`/home`, `/etc`, `/var`, `/opt`)
- ✅ Mastered user and permission management (`chmod`, `chown`)
- ✅ Used APT package management (`apt update`, `apt install`)
- ✅ Managed processes and system monitoring (`htop`, `free`, `df`, `du`)
- ✅ Learned networking basics (`ping`, `curl`, `ssh`, `scp`)
- ✅ Mastered text processing (`grep`, `awk`, `sed`)
- ✅ Installed and used `tmux` for terminal multiplexing
- ✅ Created `ai_system_check.sh` health check script
- ✅ Learned SSH for remote work
- ✅ Created Linux cheat sheet

### Lesson 12: Debugging & Profiling
- ✅ Installed debugging tools (`pdb`, `ipdb`)
- ✅ Practiced print debugging
- ✅ Set breakpoints with `pdb.set_trace()`
- ✅ Used `ipdb` for better debugging
- ✅ Configured VS Code debugger with `launch.json`
- ✅ Implemented logging with `logging` module
- ✅ Used `cProfile` for CPU profiling
- ✅ Used `line_profiler` for line-by-line profiling
- ✅ Used `memory_profiler` for memory tracking
- ✅ Profiled GPU with PyTorch (`torch.cuda`)
- ✅ Created debugging cheat sheet

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
| Lesson 09 | Data Management | ✅ Done |
| Lesson 10 | Terminal & Shell | ✅ Done |
| Lesson 11 | Linux for AI | ✅ Done |
| Lesson 12 | Debugging & Profiling | ✅ Done |

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
