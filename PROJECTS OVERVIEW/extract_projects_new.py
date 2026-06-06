import json
import re
import os

MASTER_FILE = "PORTFOLIO_PROJECTS_MASTER.md"
OUTPUT_FILE = "../portfolio-web/data/projects.json"

MANUAL_FLAGSHIPS = [
    "A Recursively Adaptive Meta-Plasticity Framework with Lyapunov-Constrained Stability",
    "Anti-Gravity Bot - Quant Trading Orchestrator",
    "EchoSoul - Full-Stack Generative AI Companion Platform",
    "Buddhi Core - Enterprise RAG & Transformer Orchestrator",
    "AnimeFaceReplace - Face Mesh Overlay Tool",
    "AutoMail - RAG Email & Browser Automation Engine"
]

MATURITY_LEVELS = ["Concept", "Experiment", "Prototype", "Production", "Research", "Commercial"]

def generate_slug(title):
    slug = title.lower().strip()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'[\s-]+', '-', slug)
    return slug

def parse_markdown():
    with open(MASTER_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Split by #### which denotes a project
    blocks = re.split(r'\n#### ', content)
    
    # The first block is the intro/executive summary
    project_blocks = blocks[1:]
    
    projects = []
    duplicate_check = set()
    duplicate_check_already_added = set()
    duplicates = []
    missing_fields_report = []

    for idx, block in enumerate(project_blocks):
        lines = block.split('\n')
        title = lines[0].strip()
        
        # Skip if empty title
        if not title:
            continue
            
        if title in duplicate_check:
            duplicates.append(title)
        duplicate_check.add(title)
        
        project = {
            "title": title,
            "slug": generate_slug(title),
            "elevatorPitch": "",
            "tags": [],
            "category": "",
            "maturity": "",
            "technologies": [],
            "repositoryPath": "",
            "sections": {},
            "tier": 1 if title in MANUAL_FLAGSHIPS else 3,
            "coverImage": "",
            "galleryImages": [],
            "thumbnailImage": ""
        }
        
        current_section = None
        section_content = []
        
        for line in lines[1:]:
            line_s = line.strip()
            
            # Match metadata
            if line_s.startswith("**Elevator Pitch:**"):
                # Remove markdown italics if present
                pitch = line_s.replace("**Elevator Pitch:**", "").strip()
                if pitch.startswith("*") and pitch.endswith("*"):
                    pitch = pitch[1:-1]
                project["elevatorPitch"] = pitch
            elif line_s.startswith("**Portfolio Tags:**"):
                tags_raw = line_s.replace("**Portfolio Tags:**", "").strip()
                # Split by ` | ` or `|`
                tags = [t.strip().replace("`", "") for t in tags_raw.split("|")]
                
                # Extract maturity
                for tag in tags:
                    if tag in MATURITY_LEVELS:
                        project["maturity"] = tag
                
                # Assuming last tag is category as per master file pattern
                if tags:
                    project["category"] = tags[-1]
                
                project["tags"] = [t for t in tags if t not in MATURITY_LEVELS and t != project["category"]]
                
                # Adjust tier based on tags if not flagship
                if project["tier"] != 1:
                    if "Production" in tags or "Commercial" in tags:
                        project["tier"] = 2
                    elif "Experiment" in tags or "Concept" in tags:
                        project["tier"] = 4
                        
            elif line_s.startswith("**Technologies:**"):
                tech_raw = line_s.replace("**Technologies:**", "").strip()
                project["technologies"] = [t.strip() for t in tech_raw.split(",")]
            elif line_s.startswith("**Repository Path:**"):
                project["repositoryPath"] = line_s.replace("**Repository Path:**", "").strip()
            elif line_s.startswith("##### "):
                # Save previous section
                if current_section:
                    project["sections"][current_section] = "\n".join(section_content).strip()
                
                current_section = line_s.replace("##### ", "").strip()
                section_content = []
            elif line_s == "<br/>" or line_s == "---":
                continue
            else:
                if current_section:
                    section_content.append(line)
        
        # Save last section
        if current_section:
            project["sections"][current_section] = "\n".join(section_content).strip()
            
        # Validation checks
        missing = []
        if not project["elevatorPitch"]: missing.append("Elevator Pitch")
        if not project["sections"].get("Overview"): missing.append("Overview section")
        if not project["technologies"]: missing.append("Technologies")
        
        if missing:
            missing_fields_report.append({"title": title, "missing": missing})
            
        # Ensure slug uniqueness before appending
        if title not in duplicate_check_already_added:
            projects.append(project)
            duplicate_check_already_added.add(title)

    # Generate Project Ecosystem Connections (Graph)
    for i, p in enumerate(projects):
        # Built before / after based on sequential array (mocking timeline)
        if i > 0:
            p["builtAfter"] = projects[i-1]["slug"]
        else:
            p["builtAfter"] = None
            
        if i < len(projects) - 1:
            p["builtBefore"] = projects[i+1]["slug"]
        else:
            p["builtBefore"] = None
            
        # Related projects based on shared tech / category (simplified Jaccard)
        related = []
        for j, other_p in enumerate(projects):
            if i != j:
                shared_tech = set(p["technologies"]).intersection(set(other_p["technologies"]))
                if p["category"] == other_p["category"] or len(shared_tech) > 0:
                    related.append(other_p["slug"])
        
        # Keep top 3 related
        p["relatedProjects"] = related[:3]

    # Save JSON
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(projects, f, indent=2)
        
    print("=" * 50)
    print("EXTRACTION AUDIT REPORT")
    print("=" * 50)
    print(f"Total Projects Parsed: {len(projects)}")
    print(f"Duplicate Projects Found: {len(duplicates)}")
    if duplicates:
        print("Duplicates:", duplicates)
    print(f"Projects with Missing Fields: {len(missing_fields_report)}")
    for m in missing_fields_report[:5]:
        print(f" - {m['title']}: {m['missing']}")
    if len(missing_fields_report) > 5:
        print(f" ... and {len(missing_fields_report) - 5} more.")
    print("=" * 50)
    print(f"Data written to {OUTPUT_FILE}")

if __name__ == "__main__":
    parse_markdown()
