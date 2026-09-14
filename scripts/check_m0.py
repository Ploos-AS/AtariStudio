#!/usr/bin/env python3
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

required = [
    "README.md",
    "ROADMAP.md",
    "LICENSE",
    "docs/ARCHITECTURE.md",
    "profiles/targets.json",
    "include/ataristudio/backend.h",
    "src/backend.c",
    "tests/test_backend.c",
]

for rel in required:
    if not (ROOT / rel).is_file():
        errors.append(f"missing required file: {rel}")

try:
    data = json.loads((ROOT / "profiles/targets.json").read_text())
except Exception as exc:
    errors.append(f"cannot parse target profiles: {exc}")
    data = {}

if data.get("format_version") != 1:
    errors.append("target profile format_version must be 1")

expected = {
    "atari-st": "68000",
    "atari-ste": "68000",
    "atari-tt": "68030",
    "atari-falcon": "68030",
}
actual = {t.get("id"): t.get("cpu") for t in data.get("targets", [])}
for target_id, cpu in expected.items():
    if actual.get(target_id) != cpu:
        errors.append(f"missing/invalid profile: {target_id} ({cpu})")

arch = (ROOT / "docs/ARCHITECTURE.md").read_text() if (ROOT / "docs/ARCHITECTURE.md").exists() else ""
if "RetroStudio must never depend on AtariStudio" not in arch:
    errors.append("dependency direction rule is missing")
if "Hatari" not in arch:
    errors.append("Hatari-first emulator strategy is missing")

header = (ROOT / "include/ataristudio/backend.h").read_text() if (ROOT / "include/ataristudio/backend.h").exists() else ""
if "ATARISTUDIO_RETROSTUDIO_TARGET_API_VERSION 1u" not in header:
    errors.append("RetroStudio target API version marker is missing")

if errors:
    print("M0 CHECK: FAIL")
    for error in errors:
        print(f"  FAIL: {error}")
    sys.exit(1)

print("M0 CHECK: PASS")
print("  PASS: AtariStudio foundation present")
print("  PASS: ST/STE/TT/Falcon baseline profiles present")
print("  PASS: backend API boundary versioned")
print("  PASS: dependency direction documented")
print("  PASS: Hatari-first strategy documented")
