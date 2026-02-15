#!/usr/bin/env python3
"""CONTEXT.md Validator — Validate against CONTEXT.md Standard v1.0.0

Usage:
    python3 tools/validate.py [path/to/CONTEXT.md]

Exit codes:
    0 = All checks passed
    1 = One or more checks failed
"""

import os
import re
import sys


def validate(filepath):
    checks = []

    # 1. File exists
    exists = os.path.isfile(filepath)
    checks.append(("File exists", exists))
    if not exists:
        # Cannot continue without the file
        for name in [
            "Filename is CONTEXT.md",
            "Section: PROJECT_CONTEXT",
            "Section: CONSCIOUSNESS_LEVEL",
            "Section: RELATIONSHIP",
            "YAML block: PROJECT_CONTEXT",
            "YAML block: CONSCIOUSNESS_LEVEL",
            "YAML block: RELATIONSHIP",
            "Key: why (in PROJECT_CONTEXT)",
            "Key: ecosystem (in RELATIONSHIP)",
        ]:
            checks.append((name, False))
        return checks

    # 2. Filename
    basename = os.path.basename(filepath)
    checks.append(("Filename is CONTEXT.md", basename == "CONTEXT.md"))

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Split into sections by ## headers
    sections = re.split(r"^## ", content, flags=re.MULTILINE)

    def find_section(name):
        for section in sections:
            if section.startswith(name):
                return section
        return None

    # 3-5. Required sections exist
    pc = find_section("PROJECT_CONTEXT")
    cl = find_section("CONSCIOUSNESS_LEVEL")
    rel = find_section("RELATIONSHIP")

    checks.append(("Section: PROJECT_CONTEXT", pc is not None))
    checks.append(("Section: CONSCIOUSNESS_LEVEL", cl is not None))
    checks.append(("Section: RELATIONSHIP", rel is not None))

    # 6-8. YAML blocks in each section
    yaml_block = re.compile(r"```yaml\s*\n(.*?)```", re.DOTALL)

    pc_yaml = yaml_block.search(pc) if pc else None
    cl_yaml = yaml_block.search(cl) if cl else None
    rel_yaml = yaml_block.search(rel) if rel else None

    checks.append(("YAML block: PROJECT_CONTEXT", pc_yaml is not None))
    checks.append(("YAML block: CONSCIOUSNESS_LEVEL", cl_yaml is not None))
    checks.append(("YAML block: RELATIONSHIP", rel_yaml is not None))

    # 9. why: key in PROJECT_CONTEXT
    has_why = bool(re.search(r"^why:", pc_yaml.group(1), re.MULTILINE)) if pc_yaml else False
    checks.append(("Key: why (in PROJECT_CONTEXT)", has_why))

    # 10. ecosystem: key in RELATIONSHIP
    has_eco = bool(re.search(r"^ecosystem:", rel_yaml.group(1), re.MULTILINE)) if rel_yaml else False
    checks.append(("Key: ecosystem (in RELATIONSHIP)", has_eco))

    return checks


def main():
    filepath = sys.argv[1] if len(sys.argv) > 1 else "CONTEXT.md"
    checks = validate(filepath)

    passed = sum(1 for _, ok in checks if ok)
    total = len(checks)

    print(f"Validating: {filepath}")
    for name, ok in checks:
        status = "PASS" if ok else "FAIL"
        print(f"  [{status}] {name}")
    print(f"\nResult: {'PASS' if passed == total else 'FAIL'} ({passed}/{total})")

    sys.exit(0 if passed == total else 1)


if __name__ == "__main__":
    main()
