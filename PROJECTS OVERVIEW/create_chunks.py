import os
import json

root = "d:/all projects"
ignore_dirs = {
    "node_modules", "dist", "build", ".git", "venv", "env", "__pycache__",
    ".idea", ".vscode", "tmp", "cache", ".next", "coverage", "vendor"
}

top_level_dirs = [d for d in os.listdir(root) if os.path.isdir(os.path.join(root, d)) and d not in ignore_dirs]

def get_tech(f):
    f = f.lower()
    if f.endswith('.py') or f == 'requirements.txt': return 'Python'
    if f.endswith('.js') or f == 'package.json': return 'JavaScript'
    if f.endswith('.ts') or f == 'tsconfig.json': return 'TypeScript'
    if f.endswith('.html'): return 'HTML'
    if f.endswith('.css'): return 'CSS'
    if f.endswith('.cpp') or f.endswith('.c') or f.endswith('.h'): return 'C/C++'
    if f.endswith('.java'): return 'Java'
    if f.endswith('.go'): return 'Go'
    if f.endswith('.rs'): return 'Rust'
    if f.endswith('.php'): return 'PHP'
    if f.endswith('.rb'): return 'Ruby'
    if f.endswith('.ipynb'): return 'Jupyter Notebook'
    if f == 'dockerfile': return 'Docker'
    if f.endswith('.sh'): return 'Shell'
    return None

def process_dir(project_dir):
    readme_texts = []
    all_techs = set()
    total_files = 0
    important_files = []
    
    for dirpath, dirnames, filenames in os.walk(project_dir):
        dirnames[:] = [d for d in dirnames if d not in ignore_dirs]
        total_files += len(filenames)
        
        for f in filenames:
            tech = get_tech(f)
            if tech: all_techs.add(tech)
            
            if f.lower().startswith('readme'):
                try:
                    with open(os.path.join(dirpath, f), 'r', encoding='utf-8', errors='ignore') as file:
                        content = file.read()[:2000]
                        rel_path = os.path.relpath(os.path.join(dirpath, f), root)
                        readme_texts.append(f"--- README ({rel_path}) ---\n{content}")
                except Exception:
                    pass
            
            # Store some files to give context on architecture
            if total_files < 50:
                important_files.append(os.path.relpath(os.path.join(dirpath, f), project_dir))
                
    return {
        "name": os.path.basename(project_dir),
        "path": os.path.basename(project_dir),
        "readmes": "\n\n".join(readme_texts),
        "techs": list(all_techs),
        "file_count": total_files,
        "sample_files": important_files[:20]
    }

projects_data = []
for d in top_level_dirs:
    p_data = process_dir(os.path.join(root, d))
    # only include if it looks like a project
    if p_data['file_count'] > 0:
        projects_data.append(p_data)

# Sort and divide into chunks of 15
projects_data.sort(key=lambda x: x['name'])
chunk_size = 15

for i in range(0, len(projects_data), chunk_size):
    chunk = projects_data[i:i + chunk_size]
    chunk_text = ""
    for p in chunk:
        chunk_text += f"==== PROJECT: {p['name']} ====\n"
        chunk_text += f"Path: {p['path']}\n"
        chunk_text += f"Technologies: {', '.join(p['techs'])}\n"
        chunk_text += f"Total Files: {p['file_count']}\n"
        chunk_text += f"Sample Files: {', '.join(p['sample_files'])}\n"
        chunk_text += f"{p['readmes']}\n\n"
        
    with open(os.path.join(root, f"project_chunk_{i//chunk_size}.txt"), 'w', encoding='utf-8') as f:
        f.write(chunk_text)

print(f"Processed {len(projects_data)} projects into {(len(projects_data)//chunk_size) + 1} chunks.")
