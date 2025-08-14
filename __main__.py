#!/usr/bin/env python3
"""
Main entry point when running as module
"""
import os
import sys

print("=== Main Module Entry ===")
print(f"Working directory: {os.getcwd()}")
print(f"Files: {os.listdir('.')}")

try:
    from main_multi_channel import start
    print("✓ Bot imported successfully")
    start()
except Exception as e:
    print(f"✗ Error: {e}")
    sys.exit(1)
