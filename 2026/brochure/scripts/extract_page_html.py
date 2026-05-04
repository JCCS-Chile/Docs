#!/usr/bin/env python3
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_INDEX = ROOT.parent / "jccs-2026-site" / "index.html"
TARGET_PAGE = ROOT / "src" / "page.html"

REPLS = {
    '/jccs-2026/logos/': './assets/logos/',
    '/jccs-2026/_next/static/media/': './assets/media/',
}


class MainExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=False)
        self.depth = 0
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "main":
            self.depth = 1
        elif self.depth:
            self.depth += 1
        if self.depth:
            self.parts.append(self.get_starttag_text())

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "main":
            self.depth = 1
        if self.depth:
            self.parts.append(self.get_starttag_text())

    def handle_endtag(self, tag: str) -> None:
        if not self.depth:
            return
        self.parts.append(f"</{tag}>")
        self.depth -= 1

    def handle_data(self, data: str) -> None:
        if self.depth:
            self.parts.append(data)

    def handle_entityref(self, name: str) -> None:
        if self.depth:
            self.parts.append(f"&{name};")

    def handle_charref(self, name: str) -> None:
        if self.depth:
            self.parts.append(f"&#{name};")


def main() -> None:
    if not SOURCE_INDEX.exists():
        raise FileNotFoundError(f"No se encontró el sitio origen: {SOURCE_INDEX}")

    parser = MainExtractor()
    parser.feed(SOURCE_INDEX.read_text(encoding="utf-8"))
    html = "".join(parser.parts)
    if not html.startswith("<main"):
        raise RuntimeError("No se pudo extraer <main> desde index.html")

    for old, new in REPLS.items():
        html = html.replace(old, new)

    TARGET_PAGE.write_text(html + "\n", encoding="utf-8")
    print(f"Página React actualizada: {TARGET_PAGE.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
