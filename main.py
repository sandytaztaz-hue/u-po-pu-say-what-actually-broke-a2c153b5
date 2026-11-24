import os

LINE = "We fixed the crash by deleting the feature that crashed. Roll back to yesterday's version to get it back. The crash comes back too, but so does your work."


def main():
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
