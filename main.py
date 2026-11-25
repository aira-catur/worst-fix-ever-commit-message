import os

TEXT_HEAD = "fix: login now works for everyone, with any password, "
TEXT_TAIL = "including 'password'"
TEXT = TEXT_HEAD + TEXT_TAIL


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
