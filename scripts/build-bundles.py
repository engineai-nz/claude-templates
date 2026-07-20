#!/usr/bin/env python3
"""
Build distributable bundles from the three-tier source layout.

For each (industry, stack) pair this script:

1. Merges core/primitives/mcp.json + stacks/<stack>/mcp.json + stacks/neutral/mcp.json
   + industries/<industry>/mcp.json into a single claude_desktop_config.json.
2. Copies industries/<industry>/skills/ into the bundle.
3. Copies claude-code-settings/ into the bundle.
4. Writes a developer_settings.json that enables Chrome DevTools.
5. Writes a bundle manifest (version, contents, build timestamp).
6. Tarballs the bundle to dist/bundles/<industry>-<stack>.tar.gz.

Outputs live at dist/bundles/ and are intended for attachment to a GitHub release.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import shutil
import sys
import tarfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DIST_DIR = REPO_ROOT / "dist" / "bundles"

STACKS = ["google", "microsoft"]
# Industries to build. Scanned from industries/ but skip placeholders without manifest.json.
DEFAULT_INDUSTRIES = sorted(
    p.parent.name for p in (REPO_ROOT / "industries").glob("*/manifest.json")
)


def load_json(path: Path) -> dict:
    if not path.is_file():
        return {}
    with path.open() as f:
        return json.load(f)


def merge_mcp_servers(*configs: dict) -> dict:
    """Merge mcpServers dicts, later configs override earlier ones."""
    merged = {}
    for cfg in configs:
        servers = cfg.get("mcpServers", {})
        for name, spec in servers.items():
            merged[name] = spec
    return {"mcpServers": merged}


def build_bundle(industry: str, stack: str, version: str) -> Path:
    industry_dir = REPO_ROOT / "industries" / industry
    manifest_path = industry_dir / "manifest.json"
    if not manifest_path.is_file():
        raise SystemExit(f"No manifest.json for industry '{industry}'")

    manifest = load_json(manifest_path)
    bundle_name = f"{industry}-{stack}"
    out_dir = DIST_DIR / bundle_name
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)

    # --- Merge MCP config ---
    primitives = load_json(REPO_ROOT / "core" / "primitives" / "mcp.json")
    stack_cfg = load_json(REPO_ROOT / "stacks" / stack / "mcp.json")
    neutral_cfg = load_json(REPO_ROOT / "stacks" / "neutral" / "mcp.json")
    industry_cfg = load_json(industry_dir / "mcp.json")

    merged = merge_mcp_servers(primitives, stack_cfg, neutral_cfg, industry_cfg)
    (out_dir / "claude_desktop_config.json").write_text(
        json.dumps(merged, indent=2) + "\n"
    )

    # --- developer_settings.json ---
    (out_dir / "developer_settings.json").write_text(
        json.dumps({"allowDevTools": True}, indent=2) + "\n"
    )

    # --- Copy skills ---
    skills_dst = out_dir / "skills"
    skills_dst.mkdir()
    industry_skills = industry_dir / "skills"
    copied_skills = []
    for skill_name in manifest.get("skills", []):
        src = industry_skills / skill_name
        if not src.is_dir():
            print(f"  WARN: declared skill '{skill_name}' not found at {src}")
            continue
        shutil.copytree(src, skills_dst / skill_name)
        copied_skills.append(skill_name)

    # --- Copy Claude Code settings ---
    cc_dst = out_dir / "claude-code"
    cc_dst.mkdir()
    cc_src = REPO_ROOT / "claude-code-settings"
    for f in ("settings.json", "permissions.json"):
        src = cc_src / f
        if src.is_file():
            shutil.copy2(src, cc_dst / f)

    # --- Bundle manifest ---
    bundle_manifest = {
        "bundle": bundle_name,
        "industry": industry,
        "stack": stack,
        "version": version,
        "built_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "mcp_servers": sorted(merged["mcpServers"].keys()),
        "skills": copied_skills,
    }
    (out_dir / "manifest.json").write_text(json.dumps(bundle_manifest, indent=2) + "\n")

    return out_dir


def tar_bundle(bundle_dir: Path) -> Path:
    tarball = DIST_DIR / f"{bundle_dir.name}.tar.gz"
    if tarball.exists():
        tarball.unlink()
    with tarfile.open(tarball, "w:gz") as tar:
        for entry in sorted(bundle_dir.rglob("*")):
            tar.add(entry, arcname=entry.relative_to(bundle_dir))
    return tarball


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", default=os.environ.get("BUNDLE_VERSION", "0.0.0-dev"))
    parser.add_argument(
        "--industries",
        nargs="*",
        default=DEFAULT_INDUSTRIES,
        help="Industries to build (default: every industry with a manifest.json)",
    )
    parser.add_argument(
        "--stacks", nargs="*", default=STACKS, help="Stacks to build (default: google microsoft)"
    )
    args = parser.parse_args()

    DIST_DIR.mkdir(parents=True, exist_ok=True)

    checksums: list[tuple[str, str]] = []
    for industry in args.industries:
        for stack in args.stacks:
            bundle_name = f"{industry}-{stack}"
            print(f"Building {bundle_name} ({args.version})...")
            bundle_dir = build_bundle(industry, stack, args.version)
            tarball = tar_bundle(bundle_dir)
            digest = sha256(tarball)
            checksums.append((tarball.name, digest))
            print(f"  -> {tarball.relative_to(REPO_ROOT)}  ({digest[:12]}...)")

    checksums_file = DIST_DIR / "checksums.txt"
    checksums_file.write_text(
        "\n".join(f"{digest}  {name}" for name, digest in checksums) + "\n"
    )
    print(f"\nChecksums written to {checksums_file.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
