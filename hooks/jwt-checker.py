from __future__ import annotations

import argparse
import re
from typing import Sequence

BLACKLIST_REGEX = [
    re.compile(b"ey.*\\..+"),
]


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to check")
    args = parser.parse_args(argv)

    private_key_files = []

    for filename in args.filenames:
        with open(filename, "rb") as f:
            content = f.read()
            if any(regex.search(content) for regex in BLACKLIST_REGEX):
                private_key_files.append(filename)

    if private_key_files:
        for private_key_file in private_key_files:
            print(f"Private key found: {private_key_file}")
        return 1
    else:
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
