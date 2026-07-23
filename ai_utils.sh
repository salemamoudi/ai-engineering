#!/bin/bash
# AI Engineering Utility Script

echo "========================================="
echo "AI Engineering Utilities"
echo "========================================="

check_ollama() {
    if curl -s http://localhost:11434/api/tags > /dev/null; then
        echo "✅ Ollama is running"
    else
        echo "❌ Ollama is not running"
    fi
}

check_python() {
    if [ -n "$VIRTUAL_ENV" ]; then
        echo "✅ Virtual environment active: $VIRTUAL_ENV"
    else
        echo "❌ No virtual environment active"
    fi
}

check_python
check_ollama
echo "========================================="
