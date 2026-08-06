#!/bin/bash
# AI System Health Check Script

echo "========================================="
echo "AI System Health Check"
echo "========================================="

# Check Python environment
echo ""
echo "📊 Python Environment:"
if [ -n "$VIRTUAL_ENV" ]; then
    echo "  ✅ Virtual env: $VIRTUAL_ENV"
else
    echo "  ❌ No virtual env active"
fi
echo "  Python: $(python --version 2>/dev/null || echo 'Not found')"

# Check GPU
echo ""
echo "📊 GPU Status:"
if command -v nvidia-smi &> /dev/null; then
    nvidia-smi --query-gpu=name,memory.used,memory.total --format=csv,noheader
else
    echo "  ❌ NVIDIA GPU not detected"
fi

# Check Ollama
echo ""
echo "📊 Ollama Status:"
if curl -s http://localhost:11434/api/tags > /dev/null; then
    echo "  ✅ Ollama running"
    echo "  Models: $(ollama list | tail -n +2 | wc -l) installed"
else
    echo "  ❌ Ollama not running"
fi

# Check Docker
echo ""
echo "📊 Docker Status:"
if command -v docker &> /dev/null; then
    echo "  ✅ Docker installed"
    echo "  Containers: $(docker ps -q | wc -l) running"
else
    echo "  ❌ Docker not installed"
fi

# Check disk space
echo ""
echo "📊 Disk Space:"
df -h / | tail -1

echo ""
echo "========================================="
