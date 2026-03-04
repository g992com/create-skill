#!/usr/bin/env python3
"""
Skill Packager - Creates a distributable .skill file.
Usage: python package_skill.py <path/to/skill-folder> [output-directory]
"""

import sys
import zipfile
from pathlib import Path

# Ensure same directory as quick_validate for import
_scripts_dir = Path(__file__).resolve().parent
if str(_scripts_dir) not in sys.path:
    sys.path.insert(0, str(_scripts_dir))

from quick_validate import validate_skill


def _is_within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def package_skill(skill_path, output_dir=None):
    skill_path = Path(skill_path).resolve()
    if not skill_path.exists():
        print(f"[ERROR] Skill folder not found: {skill_path}")
        return None
    if not skill_path.is_dir():
        print(f"[ERROR] Path is not a directory: {skill_path}")
        return None
    if not (skill_path / "SKILL.md").exists():
        print(f"[ERROR] SKILL.md not found in {skill_path}")
        return None
    print("Validating skill...")
    valid, message = validate_skill(skill_path)
    if not valid:
        print(f"[ERROR] Validation failed: {message}")
        return None
    print(f"[OK] {message}\n")
    skill_name = skill_path.name
    output_path = Path(output_dir).resolve() if output_dir else Path.cwd()
    output_path.mkdir(parents=True, exist_ok=True)
    skill_filename = output_path / f"{skill_name}.skill"
    EXCLUDED_DIRS = {".git", ".svn", ".hg", "__pycache__", "node_modules"}
    try:
        with zipfile.ZipFile(skill_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
            for file_path in skill_path.rglob("*"):
                if file_path.is_symlink():
                    continue
                if any(part in EXCLUDED_DIRS for part in file_path.relative_to(skill_path).parts):
                    continue
                if file_path.is_file():
                    resolved = file_path.resolve()
                    if not _is_within(resolved, skill_path):
                        print(f"[ERROR] File escapes skill root: {file_path}")
                        return None
                    if resolved == skill_filename.resolve():
                        continue
                    arcname = Path(skill_name) / file_path.relative_to(skill_path)
                    zipf.write(file_path, arcname)
                    print(f"  Added: {arcname}")
        print(f"\n[OK] Packaged to: {skill_filename}")
        return skill_filename
    except Exception as e:
        print(f"[ERROR] {e}")
        return None


def main():
    if len(sys.argv) < 2:
        print("Usage: python package_skill.py <path/to/skill-folder> [output-directory]")
        sys.exit(1)
    skill_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None
    result = package_skill(skill_path, output_dir)
    sys.exit(0 if result else 1)


if __name__ == "__main__":
    main()
