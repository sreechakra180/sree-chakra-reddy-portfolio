import os
import shutil
import subprocess
import time

BASE_DIR = r"D:\all projects"
SUMMARY_FILE = os.path.join(BASE_DIR, "project_summary_report.md")

PROJECT_MARKERS = [
    "package.json", "requirements.txt", "pyproject.toml",
    ".git", "src", "app", "main.py", "index.js"
]

IGNORE_DIRS = {
    ".gemini", "AppData", "$RECYCLE.BIN", "node_modules", "venv", "env",
    ".venv", "build", "dist", "__pycache__", ".vscode", ".idea"
}

CLEANUP_DIRS = ["node_modules", "venv", "env", ".venv", "build", "dist", "__pycache__"]

SENSITIVE_FILES_GLOBS = [
    ".env*", "*.pem", "*.key", "secret*", "config.local*", "firebase*.json", "*credentials*.json"
]

GITIGNORE_CONTENT = """
# Python
venv/
env/
.venv/
__pycache__/
*.pyc
.env

# Node
node_modules/
dist/
build/
.next/

# General
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/

# Logs
*.log

# Secrets
.env*
*.pem
*.key
secret*
config.local*
*credentials*.json
firebase*.json
"""

def is_project(dir_path):
    try:
        items = os.listdir(dir_path)
        for item in items:
            if item in PROJECT_MARKERS:
                return True
    except Exception:
        pass
    return False

def get_dir_size_limit(dir_path, limit_bytes=5*1024*1024*1024):
    total_size = 0
    try:
        for dirpath, dirnames, filenames in os.walk(dir_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)
                if total_size > limit_bytes:
                    return total_size
    except Exception:
        pass
    return total_size

def run_git_cmd(cmd, cwd):
    try:
        res = subprocess.run(cmd, cwd=cwd, shell=True, check=True, capture_output=True, text=True)
        return True, res.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr

def process_project(project_path, summary_data):
    project_name = os.path.basename(project_path)
    print(f"Processing project: {project_name}")
    
    # 1. Cleanup
    for item in os.listdir(project_path):
        item_path = os.path.join(project_path, item)
        if os.path.isdir(item_path) and item in CLEANUP_DIRS:
            try:
                shutil.rmtree(item_path)
                print(f"  Removed: {item}")
            except Exception as e:
                print(f"  Failed to remove {item}: {e}")
                
    # 2. README.md
    readme_path = os.path.join(project_path, "README.md")
    readme_status = "Skipped"
    if not os.path.exists(readme_path):
        try:
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(f"# {project_name}\n\nThis is the {project_name} project.\n")
            readme_status = "Created"
        except Exception as e:
            readme_status = f"Error: {e}"
    else:
        readme_status = "Exists"

    # 3. .gitignore
    gitignore_path = os.path.join(project_path, ".gitignore")
    gitignore_status = "Updated"
    existing_lines = []
    if os.path.exists(gitignore_path):
        try:
            with open(gitignore_path, "r", encoding="utf-8") as f:
                existing_lines = f.read().splitlines()
        except Exception:
            pass
            
    required_lines = [line.strip() for line in GITIGNORE_CONTENT.split('\n') if line.strip() and not line.startswith('#')]
    missing_lines = [line for line in required_lines if line not in existing_lines]
    
    if missing_lines or not os.path.exists(gitignore_path):
        try:
            with open(gitignore_path, "a", encoding="utf-8") as f:
                f.write("\n\n# Auto-added standard ignores\n")
                for line in missing_lines:
                    f.write(line + "\n")
        except Exception as e:
            gitignore_status = f"Error: {e}"
    else:
        gitignore_status = "Exists/Ok"

    # 4. Security Check (Basic check for presence, handled by gitignore)
    # The .gitignore should catch them, so they won't be staged. We'll just note if any exist at root level.
    sensitive_detected = False
    try:
        items = os.listdir(project_path)
        for item in items:
            litem = item.lower()
            if litem.startswith('.env') or litem.endswith('.pem') or litem.endswith('.key') or litem.startswith('secret') or litem.startswith('config.local') or 'credentials' in litem:
                sensitive_detected = True
                break
    except Exception:
        pass
        
    sensitive_status = "Yes (Ignored)" if sensitive_detected else "No"

    # 5. Git Setup & Commit
    git_status = "Existing"
    git_dir = os.path.join(project_path, ".git")
    if not os.path.exists(git_dir):
        success, _ = run_git_cmd("git init", project_path)
        git_status = "Initialized" if success else "Failed Init"
    
    ready_status = "Yes"
    if git_status in ["Initialized", "Existing"]:
        # check if there's anything to commit
        status_ok, status_out = run_git_cmd("git status --porcelain", project_path)
        if status_ok and status_out.strip():
            # There are changes to commit
            run_git_cmd("git add .", project_path)
            c_ok, c_out = run_git_cmd('git commit -m "Initial clean commit"', project_path)
            if not c_ok:
                ready_status = "Commit Failed"
        else:
            ready_status = "Clean (No changes)"
            
    summary_data.append({
        "Project": project_name,
        "Git": git_status,
        "README": readme_status,
        "Gitignore": gitignore_status,
        "Secrets": sensitive_status,
        "Ready": ready_status
    })

def main():
    summary_data = []
    
    print(f"Scanning base directory: {BASE_DIR}")
    for item in os.listdir(BASE_DIR):
        item_path = os.path.join(BASE_DIR, item)
        if not os.path.isdir(item_path):
            continue
            
        if item in IGNORE_DIRS or item.startswith('.'):
            continue
            
        if is_project(item_path):
            size = get_dir_size_limit(item_path)
            if size > 5 * 1024 * 1024 * 1024:
                print(f"Skipping {item} (exceeds 5GB limit)")
                summary_data.append({
                    "Project": item,
                    "Git": "Skipped",
                    "README": "Skipped",
                    "Gitignore": "Skipped",
                    "Secrets": "Unknown",
                    "Ready": "Size > 5GB"
                })
                continue
                
            process_project(item_path, summary_data)
            
    # Write report
    with open(SUMMARY_FILE, "w", encoding="utf-8") as f:
        f.write("# Project Processing Summary Report\n\n")
        f.write("| Project | Git | README | Gitignore | Secrets Detected | Ready for GitHub |\n")
        f.write("|---|---|---|---|---|---|\n")
        for sd in summary_data:
            f.write(f"| {sd['Project']} | {sd['Git']} | {sd['README']} | {sd['Gitignore']} | {sd['Secrets']} | {sd['Ready']} |\n")
            
    print(f"\nDone! Report written to {SUMMARY_FILE}")

if __name__ == "__main__":
    main()
