"""Real-Life Patch Notes entry runner.

Writes the locked one-line patch note to entry.txt in the output
directory (MAKEFUN_OUTPUT_DIR, default /output).
End-to-end check: verified by running — entry.txt is UTF-8, 133 bytes,
133 characters, one line, no newline, not whitespace-only.
"""

import os
from pathlib import Path

ENTRY = "v3.2.0: fixed a bug where the left knee reported 'ready to run' each morning, then crashed on the first stair. Affects users over 30."


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
