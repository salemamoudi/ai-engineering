# Linux Cheat Sheet for AI Engineering

## File System
- `/home/` - User home directories
- `/etc/` - System configuration
- `/var/log/` - System logs
- `/tmp/` - Temporary files
- `/opt/` - Optional software

## User & Permissions
- `whoami` - Current user
- `groups` - User groups
- `chmod 755 file` - Set permissions
- `chown user:group file` - Change ownership
- `sudo` - Run as root

## Package Management
- `sudo apt update` - Update package lists
- `sudo apt install package` - Install package
- `sudo apt remove package` - Remove package
- `uv pip install package` - Install Python package
- `uv pip list` - List Python packages

## Process Management
- `ps aux` - All processes
- `top` / `htop` - Process monitor
- `kill -9 PID` - Kill process
- `nvidia-smi` - GPU status
- `pkill name` - Kill by name

## System Monitoring
- `free -h` - Memory usage
- `df -h` - Disk usage
- `du -sh *` - Directory sizes
- `uptime` - System load
- `dmesg` - Kernel messages

## Networking
- `ip addr` - IP addresses
- `ss -tulpn` - Open ports
- `curl URL` - HTTP request
- `ping host` - Test connectivity
- `scp` - Secure copy

## Text Processing
- `grep pattern file` - Search
- `grep -r pattern .` - Search recursively
- `awk '{print $1}'` - Extract columns
- `sed 's/old/new/g'` - Replace text
- `wc -l file` - Count lines

## tmux (Terminal Multiplexer)
- `tmux new -s name` - New session
- `tmux ls` - List sessions
- `tmux attach -t name` - Attach
- `Ctrl+B, D` - Detach
- `Ctrl+B, %` - Vertical split
- `Ctrl+B, "` - Horizontal split

## AI-Specific Commands
- `nvidia-smi` - GPU info
- `ollama list` - Ollama models
- `docker ps` - Running containers
- `jupyter lab` - Start Jupyter
- `python train.py` - Run training
