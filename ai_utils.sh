#!/bin/bash
# AI Engineering Utility Script

echo "========================================="
echo "AI Engineering Utilities"
echo "========================================="

# Function to check if Ollama is running
check_ollama() {
    if curl -s http://localhost:11434/api/tags > /dev/null; then
        echo "✅ Ollama is running"
    else
        echo "❌ Ollama is not running"
        echo "   Start with: ollama serve &"
    fi
}

# Function to check Python environment
check_python() {
    if [ -n "$VIRTUAL_ENV" ]; then
        echo "✅ Virtual environment active: $VIRTUAL_ENV"
    else
        echo "❌ No virtual environment active"
        echo "   Activate with: source .venv/bin/activate"
    fi
}

# Function to show disk usage
show_disk_usage() {
    echo "📊 Disk Usage:"
    df -h / | tail -1
}

# Function to show memory usage
show_memory() {
    echo "💾 Memory Usage:"
    free -h | grep -E "Mem|Swap"
}

# Run all checks
echo ""
check_python
echo ""
check_ollama
echo ""
show_disk_usage
echo ""
show_memory
echo ""
echo "========================================="
