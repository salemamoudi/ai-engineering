# Terminal Cheat Sheet for AI Engineering

## Navigation
- `pwd` - Print working directory
- `ls -la` - List all files with details
- `cd ~/ai-engineering` - Change directory
- `cd ..` - Go up one level
- `cd -` - Go to previous directory

## File Management
- `touch file.txt` - Create empty file
- `cat file.txt` - View file
- `cp source dest` - Copy file
- `mv source dest` - Move/rename
- `rm file.txt` - Remove file
- `mkdir dir` - Create directory
- `rm -rf dir` - Remove directory recursively

## Viewing Files
- `head -n 10 file` - First 10 lines
- `tail -n 10 file` - Last 10 lines
- `grep "text" file` - Search for text
- `wc -l file` - Count lines

## Piping & Redirection
- `command1 | command2` - Pipe output
- `command > file` - Redirect output
- `command >> file` - Append output

## System Info
- `nvidia-smi` - GPU info
- `top` - Process monitor
- `free -h` - Memory usage
- `df -h` - Disk usage
- `ps aux` - Running processes

## Python/AI
- `source .venv/bin/activate` - Activate virtual env
- `uv pip list` - List packages
- `python file.py` - Run Python file
- `jupyter lab` - Start Jupyter

## Docker
- `docker ps` - Running containers
- `docker images` - Docker images
- `docker build -t name .` - Build image
- `docker run -it name` - Run container

## Git
- `git status` - Check status
- `git add .` - Stage all changes
- `git commit -m "message"` - Commit
- `git push origin branch` - Push
- `git pull origin branch` - Pull
