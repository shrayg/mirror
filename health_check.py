#!/usr/bin/env python3
"""
Simple health check endpoint for Railway deployment
"""
import os
import sys
import time
from datetime import datetime

def health_check():
    """Basic health check function"""
    try:
        # Check if required environment variables are set
        required_vars = ['APPID', 'APIHASH', 'APINAME']
        missing_vars = [var for var in required_vars if not os.environ.get(var)]
        
        if missing_vars:
            print(f"ERROR: Missing required environment variables: {missing_vars}")
            return False
            
        print(f"Health check passed at {datetime.now()}")
        print(f"Python version: {sys.version}")
        print(f"Environment variables: APPID={'*' * len(os.environ.get('APPID', ''))}, APIHASH={'*' * len(os.environ.get('APIHASH', ''))}")
        return True
        
    except Exception as e:
        print(f"Health check failed: {e}")
        return False

if __name__ == "__main__":
    success = health_check()
    sys.exit(0 if success else 1)
