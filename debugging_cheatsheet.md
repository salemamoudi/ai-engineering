# Debugging & Profiling Cheat Sheet

## Python Debugging
- `pdb.set_trace()` - Breakpoint
- `n` - Next line
- `s` - Step into function
- `c` - Continue
- `p var` - Print variable
- `q` - Quit

## VS Code Debugging
- `F5` - Start debugging
- `F10` - Step over
- `F11` - Step into
- `Shift+F11` - Step out
- `Ctrl+Shift+F5` - Restart
- `Shift+F5` - Stop

## Profiling Commands
- `python -m cProfile script.py` - CPU profiling
- `kernprof -l -v script.py` - Line profiling
- `python -m memory_profiler script.py` - Memory profiling

## GPU Profiling
- `nvidia-smi` - GPU status
- `torch.cuda.memory_allocated()` - Memory used
- `torch.cuda.synchronize()` - Sync for timing

## Logging Best Practices
- Use `logging` module (not print)
- Set appropriate levels (DEBUG, INFO, WARNING, ERROR)
- Log to file for production
- Include timestamps and context
