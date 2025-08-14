#!/usr/bin/env python3
"""
Railway entry point for Telegram to Discord Mirror Bot
"""
import os
import sys

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import and run the main bot
if __name__ == "__main__":
    try:
        from main_multi_channel import start
        print("Starting Telegram to Discord Mirror Bot...")
        start()
    except ImportError as e:
        print(f"Import error: {e}")
        print("Current directory:", os.getcwd())
        print("Files in directory:", os.listdir('.'))
        sys.exit(1)
    except Exception as e:
        print(f"Error starting bot: {e}")
        sys.exit(1)
