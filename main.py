"""Till Firmware Do Us Part — make.fun one-line entry writer.

When run, this program saves a single robot wedding vow — one funny,
heartfelt sentence, 127 characters — to /output/entry.txt so the
make.fun gate can read it. It is fully deterministic, uses only the
standard library, and touches nothing on the network.
"""

import os


VOW = (
    "I updated my firmware on our anniversary. "
    "Now I love you in version 2.0 \u2014 same heart, fewer bugs, "
    "and I still forget to charge."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    """Create /output if needed and write the vow with no trailing newline."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(VOW)
    # Read the file back and confirm it holds exactly the vow we meant.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        saved = handle.read()
    if saved != VOW:
        raise SystemExit("entry.txt does not match the vow")


if __name__ == "__main__":
    main()
