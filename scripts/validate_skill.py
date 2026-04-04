#!/usr/bin/env python3
"""Consolidated validation for the new-feature-sdlc-skill repository."""

import subprocess
import sys
from pathlib import Path

def run_command(command: list[str], root: Path) -> int:
    print(f"--- Running: {' '.join(command)} ---")
    try:
        result = subprocess.run(command, cwd=root, check=False)
        return result.returncode
    except FileNotFoundError as exc:
        print(f"Error: Command not found: {exc}")
        return 1

def main() -> int:
    root = Path(__file__).resolve().parent.parent
    
    # 1. Quick Validate
    rc = run_command([sys.executable, "scripts/quick_validate.py", "."], root)
    if rc != 0:
        return rc
        
    # 2. Generate Eval View
    rc = run_command([sys.executable, "scripts/generate_eval_view.py", "."], root)
    if rc != 0:
        return rc
    
    # 3. Pester Tests (only if on Windows and Pester exists)
    if sys.platform == "win32":
        print("--- Running Pester Tests ---")
        try:
            rc = run_command(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", "Invoke-Pester .\\tests"], root)
            if rc != 0:
                print("Pester tests failed.")
                return rc
        except Exception as exc:
            print(f"Warning: Could not run Pester tests: {exc}")
            
    print("\nValidation complete!")
    return 0

if __name__ == "__main__":
    sys.exit(main())
