from __future__ import annotations

import argparse
import re
from typing import Sequence

BLACKLIST_REGEX = [
    re.compile(b"ey\\w*\\..+"),
]


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to check")
    args = parser.parse_args(argv)

    files_with_jwt = []

    for filename in args.filenames:
        with open(filename, "rb") as f:
            content = f.read()
            for match in re.finditer(BLACKLIST_REGEX[0], content):
                line = content[:match.start()].count(b"\n") + 1
                files_with_jwt.append((filename, line))

    if files_with_jwt:
        for file_with_jwt, line in files_with_jwt:
            print(f"JWT found in {file_with_jwt}, line {line}")
        return 1
    else:
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
