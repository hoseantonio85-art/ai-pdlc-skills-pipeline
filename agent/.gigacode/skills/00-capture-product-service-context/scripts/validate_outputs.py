#!/usr/bin/env python3
"""Lightweight structural QA for the PO service-context output pair.
No external dependencies. Does NOT validate business facts or production reality.
"""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser(description="Check PO service context and questions structure")
    ap.add_argument("--service", required=True, type=Path, help="Service description MD")
    ap.add_argument("--questions", required=True, type=Path, help="Questions/decisions MD")
    args = ap.parse_args()
    errors: list[str] = []
    warnings: list[str] = []
    for label, path in [("service", args.service), ("questions", args.questions)]:
        if not path.is_file():
            errors.append(f"{label}: file not found: {path}")
    if errors:
        print("\n".join("ERROR: " + err for err in errors))
        return 1

    service = args.service.read_text(encoding="utf-8-sig")
    questions = args.questions.read_text(encoding="utf-8-sig")
    headers = re.findall(r"^## (\d+)\.\s+(.+)$", service, re.M)
    nums = [int(n) for n, _ in headers]
    if nums != list(range(13)):
        errors.append(f"service: expected consecutive ## 0...## 12 once each, got {nums}")
    if not service.lstrip().startswith("# "):
        errors.append("service: missing H1 title")
    if not questions.lstrip().startswith("# "):
        errors.append("questions: missing H1 title")
    if not re.search(r"(?im)^##\s+2\.\s+.*вопрос", questions):
        warnings.append("questions: no standard '## 2. ... вопросы' section")
    if not re.search(r"(?im)^##\s+[3-5]\.\s+.*(решени|истори|вопрос)", questions):
        warnings.append("questions: no decisions/resolved-question section found")
    if "AS IS" not in service or "TO BE" not in service:
        warnings.append("service: explicit AS IS or TO BE marker is missing")
    if not any(x in service for x in ("[CODE]", "[OWNER]", "[SPEC]", "[B]", "[UG]", "[BT]", "[GUIDE]", "[RUNTIME]")):
        warnings.append("service: no recognizable source status markers; ensure provenance manually")
    service_questions = set(re.findall(r"\bQ-\d{2,3}\b", service))
    registered_questions = set(re.findall(r"\bQ-\d{2,3}\b", questions))
    for unknown in sorted(service_questions - registered_questions):
        warnings.append(f"service: {unknown} referenced but missing in questions register")
    placeholder = re.findall(r"\[(?:Название|Краткое|Ссылка|Роль\s*\d+|вопрос|сценарий|источник|ДД\.ММ\.ГГГГ)[^\]]*\]", service, re.I)
    if placeholder:
        warnings.append(f"service: likely unfilled placeholders ({len(placeholder)}): {placeholder[:5]}")
    if len(service.splitlines()) < 45:
        warnings.append("service: very short document; check whether all applicable sections are described")
    if len(questions.splitlines()) < 18:
        warnings.append("questions: very short register; check missing decisions or unresolved items")

    print(f"Service sections: {len(nums)}; questions IDs: {len(registered_questions)}; referenced in service: {len(service_questions)}")
    for msg in errors: print("ERROR: " + msg)
    for msg in warnings: print("WARN: " + msg)
    if not errors: print("STRUCTURE: PASS (not a business or production certification)")
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
