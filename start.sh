#!/bin/bash
echo "Starting Telegram to Discord Mirror Bot..."
echo "Current directory: $(pwd)"
echo "Files in directory:"
ls -la
echo "Running bot..."
python ./main_multi_channel.py
