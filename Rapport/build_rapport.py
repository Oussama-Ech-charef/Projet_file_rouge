import os
import re
import shutil
from pathlib import Path

# Base Paths
RAPPORT_DIR = Path(__file__).resolve().parent
RAPPORT_FINAL_FILE = RAPPORT_DIR / "rapport-final.md"
SKELETON_FILE = RAPPORT_DIR / "skeleton.md"

def normalize_name(s: str) -> str:
    """Normalize string for fuzzy matching folder names to section titles."""
    s = s.lower().strip()
    replacements = {
        "é": "e", "è": "e", "ê": "e", "ë": "e",
        "à": "a", "â": "a", "ä": "a",
        "î": "i", "ï": "i",
        "ô": "o", "ö": "o",
        "ù": "u", "û": "u", "ü": "u",
        "ç": "c", "'": "", "`": "", "-": " ", "_": " "
    }
    for k, v in replacements.items():
        s = s.replace(k, v)
    s = re.sub(r"[^a-z0-9]", "", s)
    return s

# Define canonical structure from skeleton.md
STRUCTURE = [
    {"title": "Remerciements", "level": 2},
    {"title": "Introduction", "level": 2},
    {"title": "Contexte du projet", "level": 2},
    {"title": "Cahier des charges", "level": 2},
    {"title": "Méthodologie de travail", "level": 2},
    {"title": "Méthodologie Scrum", "level": 3},
    {"title": "Processus 2TUP", "level": 3},
    {"title": "Design Thinking", "level": 3},
    {"title": "Planification", "level": 2},
    {"title": "Branche fonctionnelle", "level": 2},
    {"title": "Carte d'empathie", "level": 3},
    {"title": "Définition du problème", "level": 3},
    {"title": "Idéation", "level": 3},
    {"title": "Diagramme de cas d'utilisation", "level": 3},
    {"title": "Branche technique", "level": 2},
    {"title": "Stack technologique", "level": 3},
    {"title": "Architecture logicielle", "level": 3},
    {"title": "Prototype (fonctionnalités, classes)", "level": 3},
    {"title": "Conception", "level": 2},
    {"title": "Diagramme de classes", "level": 3},
    {"title": "Maquettes", "level": 3},
    {"title": "Réalisation", "level": 2},
    {"title": "Interfaces", "level": 3},
    {"title": "Conclusion", "level": 2},
]

# Section title aliases / directory synonyms
SECTION_ALIASES = {
    normalize_name("Remerciements"): [normalize_name("Remerciement")],
    normalize_name("Processus 2TUP"): [normalize_name("2TUP")],
    normalize_name("Méthodologie Scrum"): [normalize_name("Scrum"), normalize_name("SCRUM")],
    normalize_name("Architecture logicielle"): [normalize_name("architecture_du_system")],
}

def adjust_image_paths(content: str, source_folder: Path, target_file: Path) -> str:
    """
    Ensures relative image paths in markdown/html point correctly
    from target_file (rapport/rapport-final.md) to images in source_folder.
    """
    rel_folder = os.path.relpath(source_folder, target_file.parent).replace("\\", "/")

    # Markdown format: ![alt](path "optional title")
    def md_repl(match):
        alt = match.group(1)
        full_url = match.group(2).strip()
        parts = full_url.split(maxsplit=1)
        url = parts[0]
        title_part = " " + parts[1] if len(parts) > 1 else ""

        if url.startswith(("http://", "https://", "data:", "/")):
            return match.group(0)

        clean_url = url.lstrip("./").lstrip("/")
        # If the path already has the folder prefix, avoid duplication
        if clean_url.startswith(rel_folder + "/"):
            new_url = clean_url
        else:
            new_url = f"{rel_folder}/{clean_url}" if rel_folder != "." else clean_url

        return f"![{alt}]({new_url}{title_part})"

    content = re.sub(r'!\[(.*?)\]\((.*?)\)', md_repl, content)

    # HTML img tag format: <img ... src="..." ... />
    def html_repl(match):
        full_tag = match.group(0)
        src_match = re.search(r'src=["\'](.*?)["\']', full_tag)
        if not src_match:
            return full_tag
        url = src_match.group(1).strip()
        if url.startswith(("http://", "https://", "data:", "/")):
            return full_tag

        clean_url = url.lstrip("./").lstrip("/")
        if clean_url.startswith(rel_folder + "/"):
            new_url = clean_url
        else:
            new_url = f"{rel_folder}/{clean_url}" if rel_folder != "." else clean_url

        return full_tag.replace(src_match.group(0), f'src="{new_url}"')

    content = re.sub(r'<img\s+[^>]*src=["\'][^"\']+["\'][^>]*>', html_repl, content)
    return content

def adjust_heading_levels(content: str, section_level: int, section_title: str) -> str:
    """
    Cleans top-level headings that duplicate the section name and
    shifts sub-headings to maintain consistent markdown hierarchy.
    """
    lines = content.splitlines()

    # Strip YAML front matter if present
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                lines = lines[i + 1:]
                break

    while lines and not lines[0].strip():
        lines.pop(0)

    # If first heading is identical/similar to section title, remove it
    if lines and re.match(r'^#{1,3}\s+', lines[0]):
        h_text = re.sub(r'^#{1,3}\s+', '', lines[0]).strip()
        norm_h = normalize_name(h_text)
        norm_sec = normalize_name(section_title)
        if norm_h == norm_sec or norm_h in SECTION_ALIASES.get(norm_sec, []):
            lines.pop(0)

    while lines and not lines[0].strip():
        lines.pop(0)

    # Adjust inner heading levels: inner headings inside a level 3 section should be level 4+
    adjusted_lines = []
    for line in lines:
        match = re.match(r'^(#{1,6})\s+(.*)$', line)
        if match:
            hashes = match.group(1)
            text = match.group(2)
            lvl = len(hashes)
            min_sub = section_level + 1
            if lvl <= section_level:
                new_lvl = min(min_sub + (lvl - 1), 6)
                adjusted_lines.append(f"{'#' * new_lvl} {text}")
            else:
                adjusted_lines.append(line)
        else:
            adjusted_lines.append(line)

    return "\n".join(adjusted_lines).strip()

def parse_existing_sections(rapport_file: Path):
    """Parses existing rapport-final.md into {normalized_title: content}."""
    if not rapport_file.exists():
        return {}

    lines = rapport_file.read_text(encoding="utf-8").splitlines()
    sections = {}
    current_title = None
    current_lines = []
    in_sections = False

    for line in lines:
        match = re.match(r'^(#{2,3})\s+(.+)$', line)
        if match:
            heading = match.group(2).strip()
            # If it's the TOC heading, skip
            if "table des mati" in normalize_name(heading):
                continue
            if current_title:
                sections[normalize_name(current_title)] = "\n".join(current_lines).strip()
            current_title = heading
            current_lines = []
            in_sections = True
        elif in_sections:
            current_lines.append(line)

    if current_title:
        sections[normalize_name(current_title)] = "\n".join(current_lines).strip()

    return sections

def find_folder_for_section(title: str, base_dir: Path):
    """Finds matching folder for a section title."""
    target_norm = normalize_name(title)
    aliases = SECTION_ALIASES.get(target_norm, [])

    subdirs = [d for d in base_dir.iterdir() if d.is_dir()]
    for d in subdirs:
        d_norm = normalize_name(d.name)
        if d_norm == target_norm or d_norm in aliases:
            return d
    return None

def generate_slug(title: str) -> str:
    slug = title.lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"\s+", "-", slug)
    return slug

def main():
    print(f"Reading skeleton from: {SKELETON_FILE}")
    print(f"Target report file: {RAPPORT_FINAL_FILE}")

    existing_sections = parse_existing_sections(RAPPORT_FINAL_FILE)

    # Backup original rapport-final.md
    if RAPPORT_FINAL_FILE.exists():
        backup = RAPPORT_DIR / "rapport-final.md.bak"
        shutil.copy(RAPPORT_FINAL_FILE, backup)
        print(f"Backup created at: {backup.name}")

    parts_changed = []
    parts_same = []
    parts_empty = []

    # Build TOC
    toc = ["#### Table des matières\n"]
    for sec in STRUCTURE:
        indent = "  " if sec["level"] == 3 else ""
        slug = generate_slug(sec["title"])
        toc.append(f"{indent}- [{sec['title']}](#{slug})")

    body_sections = []

    for sec in STRUCTURE:
        title = sec["title"]
        level = sec["level"]
        norm_title = normalize_name(title)
        heading_prefix = "#" * level

        folder = find_folder_for_section(title, RAPPORT_DIR)
        new_content = ""

        if folder:
            md_files = [f for f in folder.glob("*.md")]
            if md_files:
                combined_md = []
                for f in sorted(md_files):
                    raw_text = f.read_text(encoding="utf-8")
                    rel_text = adjust_image_paths(raw_text, folder, RAPPORT_FINAL_FILE)
                    adj_text = adjust_heading_levels(rel_text, level, title)
                    if adj_text:
                        combined_md.append(adj_text)
                if combined_md:
                    new_content = "\n\n".join(combined_md).strip()

        old_content = existing_sections.get(norm_title, "").strip()

        # Decide content and categorize status
        if new_content:
            final_content = new_content
            if old_content and old_content == final_content:
                parts_same.append(title)
            else:
                parts_changed.append(title)
        elif old_content:
            final_content = old_content
            parts_same.append(title)
        else:
            final_content = ""
            parts_empty.append(title)

        sec_block = f"{heading_prefix} {title}"
        if final_content:
            sec_block += f"\n\n{final_content}"
        else:
            sec_block += "\n"

        body_sections.append(sec_block)

    # Document Header
    header = """---
layout: default
title: Rapport
---

# Rapport

""" + "\n".join(toc) + "\n\n"

    full_document = header + "\n\n".join(body_sections).strip() + "\n"

    RAPPORT_FINAL_FILE.write_text(full_document, encoding="utf-8")
    print(f"\n[OK] rapport-final.md successfully updated!\n")

    # Final summary display
    print("=" * 60)
    print("RESUME DES PARTIES DU RAPPORT")
    print("=" * 60)

    print(f"\n1. Parties modifiees / mises a jour ({len(parts_changed)}) :")
    for p in parts_changed:
        print(f"   [+] {p}")

    print(f"\n2. Parties inchangees ({len(parts_same)}) :")
    for p in parts_same:
        print(f"   [=] {p}")

    print(f"\n3. Parties vides ({len(parts_empty)}) :")
    for p in parts_empty:
        print(f"   [-] {p}")

    print("=" * 60)

if __name__ == "__main__":
    main()
