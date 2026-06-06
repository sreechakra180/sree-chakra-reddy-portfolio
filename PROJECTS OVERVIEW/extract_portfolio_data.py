import os
import json

root = "d:/all projects"
ignore_dirs = {
    "node_modules", "dist", "build", ".git", "venv", "env", "__pycache__",
    ".idea", ".vscode", "tmp", "cache", ".next", "coverage", "vendor"
}

project_data = []

def get_technologies(filenames):
    tech = set()
    for f in filenames:
        f = f.lower()
        if f.endswith('.py'): tech.add('Python')
        if f.endswith('.js'): tech.add('JavaScript')
        if f.endswith('.ts'): tech.add('TypeScript')
        if f.endswith('.html'): tech.add('HTML')
        if f.endswith('.css'): tech.add('CSS')
        if f.endswith('.cpp') or f.endswith('.c'): tech.add('C/C++')
        if f.endswith('.java'): tech.add('Java')
        if f.endswith('.go'): tech.add('Go')
        if f.endswith('.rs'): tech.add('Rust')
        if f.endswith('.php'): tech.add('PHP')
        if f.endswith('.rb'): tech.add('Ruby')
        if f.endswith('.ipynb'): tech.add('Jupyter Notebook')
        if f == 'package.json': tech.add('Node.js')
        if f == 'requirements.txt': tech.add('Python')
        if f == 'dockerfile': tech.add('Docker')
    return list(tech)

for dirpath, dirnames, filenames in os.walk(root):
    # filter directories
    dirnames[:] = [d for d in dirnames if d not in ignore_dirs]
    
    # Check if this folder looks like a project
    # A project typically has a README or some source files
    readme_content = ""
    has_source_code = False
    
    for f in filenames:
        if f.lower().startswith('readme'):
            try:
                with open(os.path.join(dirpath, f), 'r', encoding='utf-8') as file:
                    readme_content = file.read()[:5000] # Grab first 5000 chars
            except Exception:
                pass
        
        if f.lower().endswith(('.py', '.js', '.ts', '.html', '.cpp', '.java', '.go', '.rs', '.php', '.rb', '.ipynb')):
            has_source_code = True

    if readme_content or has_source_code:
        # Don't add the root directory itself
        if dirpath == root:
            continue
            
        tech = get_technologies(filenames)
        
        # Check if it's deeply nested - we might want to group them, but we'll let the LLM decide
        rel_path = os.path.relpath(dirpath, root)
        
        project_data.append({
            "path": rel_path,
            "name": os.path.basename(dirpath),
            "readme": readme_content,
            "technologies": tech,
            "files": filenames[:30] # list up to 30 files for context
        })

with open(os.path.join(root, "extracted_portfolio_data.json"), "w", encoding="utf-8") as f:
    json.dump(project_data, f, indent=2)

print(f"Extracted data for {len(project_data)} potential projects.")
