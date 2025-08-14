#!/usr/bin/env python3
"""
WSGI entry point for Railway deployment
"""
import os
import sys

print("=== WSGI Entry Point ===")
print(f"Working directory: {os.getcwd()}")
print(f"Files available: {os.listdir('.')}")

# Import and run the bot
try:
    from main_multi_channel import start
    print("✓ Bot imported successfully")
    print("✓ Starting bot...")
    start()
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
