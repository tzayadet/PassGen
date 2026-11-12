from html.parser import HTMLParser
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.scripts = []
        self.current_script = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.append(attrs["id"])
        if tag == "script":
            self.current_script = [] if "src" not in attrs else None

    def handle_data(self, data):
        if self.current_script is not None:
            self.current_script.append(data)

    def handle_endtag(self, tag):
        if tag == "script" and self.current_script is not None:
            self.scripts.append("".join(self.current_script))
            self.current_script = None


def main():
    parser = PageParser()
    parser.feed((ROOT / "index.html").read_text(encoding="utf-8"))

    duplicates = sorted({value for value in parser.ids if parser.ids.count(value) > 1})
    if duplicates:
        raise SystemExit(f"Duplicate HTML IDs: {duplicates}")

    if len(parser.scripts) != 1:
        raise SystemExit(f"Expected one inline application script, found {len(parser.scripts)}")

    source = parser.scripts[0]
    if "crypto.getRandomValues" not in source or "function secureRandomInt" not in source:
        raise SystemExit("Password generation must use the Web Crypto API.")
    if "Math.random" in source[source.find("function secureRandomInt"):source.find("function secureShuffle")]:
        raise SystemExit("Math.random must not be used by the secure random integer helper.")

    with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8", delete=False) as handle:
        handle.write(source)
        script_path = Path(handle.name)

    try:
        subprocess.run(["node", "--check", str(script_path)], check=True)
    finally:
        script_path.unlink(missing_ok=True)

    print("Password generator HTML and cryptographic RNG checks passed.")


if __name__ == "__main__":
    main()
