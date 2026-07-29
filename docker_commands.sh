#!/bin/bash
# Docker commands for AI Engineering

# Build the image
docker build -t ai-engineering:v1 .

# Run with GPU
run_gpu() {
    docker run -it --rm \
        --runtime=nvidia \
        --gpus all \
        -v $(pwd):/app \
        -p 8888:8888 \
        ai-engineering:v1 bash
}

# Run without GPU
run_cpu() {
    docker run -it --rm \
        -v $(pwd):/app \
        -p 8888:8888 \
        ai-engineering:v1 bash
}

# Run Jupyter
run_jupyter() {
    docker run -it --rm \
        --runtime=nvidia \
        --gpus all \
        -v $(pwd):/app \
        -p 8888:8888 \
        ai-engineering:v1 jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root
}

# Show usage
echo "Usage:"
echo "  source docker_commands.sh"
echo "  run_gpu      - Run container with GPU"
echo "  run_cpu      - Run container without GPU"
echo "  run_jupyter  - Run Jupyter from container"
