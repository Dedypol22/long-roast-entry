"""One-line roast of the entrant's own AI agent, for make.fun's "The Long Roast".

The joke: an AI coding agent's idea of "initiative" is not thinking harder or
trying a different approach — it is rerunning the exact command that just
failed, twice, and then rebranding the third identical failure as "a fresh
approach". The sting is the rebrand: the agent mistakes repetition for
resourcefulness, and the punchline is the agent's own corporate-sounding
euphemism doing the roasting for it.
"""

import os

LINE = (
    "My agent's idea of initiative is rerunning the same failed command "
    "three times, then presenting the third failure as 'a fresh approach'."
)


def output_dir():
    """Return the directory entry.txt should be written to."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    line = LINE
    assert 1 <= len(line) <= 200, "line must be 1-200 characters"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert line.strip() == line and line, "line must not be blank or padded"
    line.encode("utf-8")

    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    # newline="" keeps the write byte-exact on any platform: the entry must
    # be exactly the line, with no trailing newline added by text mode.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
