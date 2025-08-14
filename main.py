#!/usr/bin/env python3
"""
Main entry point for Railway deployment
"""
import os
import sys

print("=== Railway Bot Startup ===")
print(f"Working directory: {os.getcwd()}")
print(f"Files available: {os.listdir('.')}")

# Import and run the multi-channel bot
try:
    from main_multi_channel import start
    print("Bot imported successfully, starting...")
    start()
except Exception as e:
    print(f"Failed to start bot: {e}")
    sys.exit(1)
