#!/usr/bin/env python3
import argparse
import json
import os
import shutil
import sys

# Windows consoles default to a legacy code page (cp949 on Korean systems),
# which mangles non-ASCII paths in the hook payload; force UTF-8 on stdio.
for _stream in (sys.stdin, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        try:
            _stream.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tool", required=True, choices=["claude-code", "codex"])
    args = parser.parse_args()

    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(f"save_log: failed to parse stdin JSON: {exc}", file=sys.stderr)
        return 0

    if not isinstance(payload, dict):
        print("save_log: hook payload must be a JSON object", file=sys.stderr)
        return 0

    transcript_path = payload.get("transcript_path")
    cwd = payload.get("cwd") or os.getcwd()
    session_id = payload.get("session_id") or "session"

    if not isinstance(transcript_path, str) or not os.path.isfile(transcript_path):
        print(
            f"save_log: transcript_path missing or not a file: {transcript_path!r}",
            file=sys.stderr,
        )
        return 0

    safe_session = os.path.basename(str(session_id))
    if safe_session in ("", ".", ".."):
        safe_session = "session"

    dest_dir = os.path.join(str(cwd), "logs", args.tool)
    dest = os.path.join(dest_dir, f"{safe_session}.jsonl")

    try:
        os.makedirs(dest_dir, exist_ok=True)
        shutil.copyfile(transcript_path, dest)
    except OSError as exc:
        print(f"save_log: copy failed: {exc}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
