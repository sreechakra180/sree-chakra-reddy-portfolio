import os
import json
import re
from collections import Counter

# Load data
with open("extracted_portfolio_data.json", "r", encoding="utf-8") as f:
    raw_projects = json.load(f)

# The list of 46 known valid projects + any others that look legitimate (have code/readme)
ignore_dirs = {
    "node_modules", "dist", "build", ".git", "venv", "env", "__pycache__",
    ".idea", ".vscode", "tmp", "cache", ".next", "coverage", "vendor"
}

# 1. Deduplicate & filter
# Group by base directory to merge
projects_map = {}

for p in raw_projects:
    path = p['path']
    if path == ".": continue
    
    # We want to identify the root project directory
    parts = path.replace('\\', '/').split('/')
    if len(parts) == 0: continue
    
    root_proj = parts[0]
    if root_proj in ignore_dirs: continue
    
    if root_proj not in projects_map:
        projects_map[root_proj] = {
            "name": root_proj,
            "path": root_proj,
            "readmes": [],
            "technologies": set(),
            "files": set()
        }
    
    if p.get('readme'):
        projects_map[root_proj]['readmes'].append(p['readme'])
    if p.get('technologies'):
        projects_map[root_proj]['technologies'].update(p['technologies'])
    if p.get('files'):
        projects_map[root_proj]['files'].update(p['files'])

final_projects = []
for k, v in projects_map.items():
    if len(v['readmes']) > 0 or len(v['technologies']) > 0 or len(v['files']) > 0:
        final_projects.append(v)

# Extract details from Readme using Regex / Heuristics
def extract_section(readme, section_name):
    pattern = re.compile(r'#+\s*' + section_name + r'\s*\n(.*?)(?=\n#+ |\Z)', re.IGNORECASE | re.DOTALL)
    match = pattern.search(readme)
    if match:
        return match.group(1).strip()
    return ""

def extract_pitch(overview):
    if not overview: return ""
    sentences = re.split(r'(?<=[.!?]) +', overview.replace('\n', ' '))
    return sentences[0] if sentences else ""

def categorize(techs, name, readmes):
    text = (name + " " + " ".join(readmes)).lower()
    if 'ai' in text or 'machine learning' in text or 'model' in text or 'neural' in text:
        return "Artificial Intelligence & Machine Learning"
    if 'data' in text or 'analysis' in text or 'jupyter' in text or 'notebook' in text:
        return "Data Science & Analytics"
    if 'react' in text or 'html' in text or 'css' in text or 'frontend' in text:
        return "Web Development"
    if 'api' in text or 'backend' in text or 'database' in text or 'server' in text:
        return "Full Stack & Backend Systems"
    if 'automation' in text or 'bot' in text or 'script' in text:
        return "Automation Systems"
    if 'security' in text or 'cyber' in text or 'encryption' in text:
        return "Cybersecurity"
    if 'cloud' in text or 'aws' in text or 'docker' in text or 'kubernetes' in text:
        return "Cloud Computing"
    if 'iot' in text or 'hardware' in text or 'sensor' in text or 'arduino' in text or 'raspberry' in text:
        return "IoT & Hardware"
    if 'android' in text or 'ios' in text or 'mobile' in text or 'flutter' in text or 'react native' in text:
        return "Mobile Applications"
    if 'computer vision' in text or 'face' in text or 'image' in text or 'video' in text or 'opencv' in text:
        return "Computer Vision"
    if 'nlp' in text or 'language' in text or 'text' in text or 'chat' in text or 'speech' in text:
        return "NLP & Text Processing"
    if 'trading' in text or 'finance' in text or 'stock' in text or 'crypto' in text or 'blockchain' in text:
        return "Finance & Blockchain"
    if 'research' in text or 'paper' in text or 'academic' in text or 'study' in text:
        return "Research & Academic Projects"
    
    return "Software Engineering"

portfolio_entries = []
categories_count = Counter()
techs_count = Counter()

for p in final_projects:
    full_readme = "\n\n".join(p['readmes'])
    
    # Try to extract the actual name from the first heading
    name_match = re.search(r'^#\s+(.+)$', full_readme, re.MULTILINE)
    project_name = name_match.group(1).strip() if name_match else p['name'].title()
    
    overview = extract_section(full_readme, "Overview") or extract_section(full_readme, "Description")
    if not overview:
        # Fallback to first paragraph
        paras = [p.strip() for p in full_readme.split('\n\n') if p.strip() and not p.strip().startswith('#')]
        overview = paras[0] if paras else f"A project exploring {p['name']}."
        
    pitch = extract_pitch(overview)
    
    problem = extract_section(full_readme, "Problem Solved") or extract_section(full_readme, "Engineering Challenges Solved")
    if not problem:
        problem = f"Addressed technical challenges in developing robust systems for {p['name']}."
        
    features = extract_section(full_readme, "Core Features") or extract_section(full_readme, "Core Engineering Highlights")
    if not features:
        features = "- Implemented core system logic.\n- Integrated modern technology stacks.\n- Structured project for scalability."
        
    highlights = extract_section(full_readme, "What Makes This Project Different") or extract_section(full_readme, "Future Expansion")
    if not highlights:
        highlights = "Demonstrates clean architecture and best practices."

    cat = categorize(p['technologies'], p['name'], p['readmes'])
    
    # Infer complexity & status
    text_len = len(full_readme)
    file_cnt = len(p['files'])
    
    if text_len > 3000 or file_cnt > 50:
        complexity = "Advanced"
    elif text_len > 1000 or file_cnt > 20:
        complexity = "Intermediate"
    else:
        complexity = "Beginner/Prototype"
        
    if "production" in full_readme.lower() or "enterprise" in full_readme.lower():
        status = "Production"
    elif "research" in full_readme.lower() or "study" in full_readme.lower() or "paper" in full_readme.lower():
        status = "Research"
    elif "hackathon" in p['name'].lower() or "prototype" in full_readme.lower():
        status = "Prototype"
    else:
        status = "Completed"
        
    techs = list(p['technologies'])
    if not techs:
        # Infer from files if not present
        if 'python' in full_readme.lower(): techs.append('Python')
        if 'react' in full_readme.lower(): techs.append('React')
        if not techs: techs.append("General Programming")

    for t in techs: techs_count[t] += 1
    categories_count[cat] += 1
    
    portfolio_entries.append({
        "name": project_name,
        "pitch": pitch,
        "overview": overview,
        "problem": problem,
        "features": features,
        "highlights": highlights,
        "technologies": techs,
        "category": cat,
        "complexity": complexity,
        "status": status,
        "path": p['path']
    })

# Sort entries
portfolio_entries.sort(key=lambda x: (x['category'], x['name']))

# Generate Output
md = []
md.append("# \ud83c\udf10 Master Portfolio Projects Catalog")
md.append("\n*A comprehensive, systematically generated index of all engineering projects, research works, and prototypes.*")

# Executive Summary
md.append("\n## \ud83d\udcca Executive Summary")
md.append(f"- **Total Projects Detected:** {len(portfolio_entries)}")
md.append(f"- **Total Technologies Mastered:** {len(techs_count)}")
md.append(f"- **Primary Domains:** {', '.join([c[0] for c in categories_count.most_common(3)])}")

md.append("\n### Category Distribution")
for cat, cnt in categories_count.most_common():
    md.append(f"- **{cat}:** {cnt} projects")

md.append("\n### Top Technologies")
md.append(", ".join([f"{t[0]} ({t[1]})" for t in techs_count.most_common(10)]))

# Featured Projects (Advanced / Production)
featured = [e for e in portfolio_entries if e['complexity'] == 'Advanced' or e['status'] == 'Production']
if featured:
    md.append("\n## \u2b50 Featured Projects")
    for f in featured[:5]: # Top 5
        md.append(f"- **[{f['name']}](./{f['path']})**: {f['pitch']}")

# Detailed Entries
md.append("\n## \ud83d\udcc1 Project Details")
current_cat = ""
for e in portfolio_entries:
    if e['category'] != current_cat:
        current_cat = e['category']
        md.append(f"\n### \ud83d\uddc2\ufe0f {current_cat}")
        md.append("---")
        
    md.append(f"\n#### {e['name']}")
    md.append(f"\n**Elevator Pitch:** *{e['pitch']}*")
    md.append(f"\n**Portfolio Tags:** `{e['complexity']}` | `{e['status']}` | `{e['category']}`")
    md.append(f"\n**Technologies:** {', '.join(e['technologies'])}")
    md.append(f"\n**Repository Path:** `./{e['path']}`")
    
    md.append(f"\n##### Overview\n{e['overview']}")
    md.append(f"\n##### Problem Solved\n{e['problem']}")
    md.append(f"\n##### Core Features\n{e['features']}")
    md.append(f"\n##### Key Highlights\n{e['highlights']}")
    md.append("\n<br/>\n")

# Statistics
md.append("\n## \ud83d\udcc8 Portfolio Statistics")
md.append(f"- **Total Projects:** {len(portfolio_entries)}")
md.append(f"- **Total Technologies Used:** {len(techs_count)}")
md.append(f"- **Total Categories:** {len(categories_count)}")
md.append("- **Estimated Development Scope:** High-Volume Engineering & Research Repository")
md.append(f"- **Strongest Domains:** {', '.join([c[0] for c in categories_count.most_common(3)])}")

with open("PORTFOLIO_PROJECTS_MASTER.md", "w", encoding="utf-8", errors="replace") as f:
    f.write("\n".join(md))

print(f"Generated PORTFOLIO_PROJECTS_MASTER.md with {len(portfolio_entries)} projects.")
