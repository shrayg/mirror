#!/usr/bin/env python3
"""
Simple start script for Railway deployment
"""
import os
import sys

print("=== Railway Deployment Debug Info ===")
print(f"Current working directory: {os.getcwd()}")
print(f"Python executable: {sys.executable}")
print(f"Python version: {sys.version}")
print(f"Files in current directory:")
try:
    for file in os.listdir('.'):
        print(f"  - {file}")
except Exception as e:
    print(f"Error listing files: {e}")

print("\n=== Starting Bot ===")
try:
    # Try to import and run the bot
    from main_multi_channel import start
    print("Successfully imported main_multi_channel")
    start()
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
