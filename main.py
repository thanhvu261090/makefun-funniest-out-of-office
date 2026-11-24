"""The Funniest Out-of-Office: one-line auto-reply entry.

Writes the entry line to /output/entry.txt, enforcing the kit gate:
UTF-8 text, 1 to 140 characters, not only whitespace, a single line.
"""

ENTRY = "Out of office until Monday \u2014 I left my inbox with my cat, who has already replied \u201cno\u201d to everyone, including my boss."

MAX_CHARS = 140


def gate_check(text):
    """Return True only if text passes the kit gate."""
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= MAX_CHARS:
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    if text != text.strip():
        return False
    if any(ord(ch) < 32 for ch in text):
        return False
    # The entry is one line of text and nothing else: no link, no image.
    lowered = text.lower()
    if "http://" in lowered or "https://" in lowered or "www." in lowered:
        return False
    return True


def main():
    if not gate_check(ENTRY):
        raise SystemExit("gate check failed: entry does not satisfy the 1-140 char single-line gate")
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
