#!/bin/bash

# Print message
echo "Running command: cloudflared tunnel --url 127.0.0.1:8002"
echo

# Run command and redirect output to output.txt
cloudflared tunnel --url 127.0.0.1:8002 > output.txt 2>&1

# Wait for 5 seconds
sleep 5
