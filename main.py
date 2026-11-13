import os

JOKE = (
    "I asked my coding agent to change one character. It sent back a pull "
    "request with 47 files changed and a summary that begins, "
    "'While I was in there...'"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
