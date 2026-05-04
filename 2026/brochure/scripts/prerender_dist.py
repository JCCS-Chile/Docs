#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST_INDEX = ROOT / "dist" / "index.html"
PAGE_HTML = ROOT / "src" / "page.html"


def main() -> None:
    index = DIST_INDEX.read_text(encoding="utf-8")
    page = PAGE_HTML.read_text(encoding="utf-8").strip()
    marker = '<div id="root"></div>'
    if marker not in index:
        raise RuntimeError("No se encontró el contenedor root vacío en dist/index.html")
    DIST_INDEX.write_text(index.replace(marker, f'<div id="root">{page}</div>'), encoding="utf-8")
    print("dist/index.html pre-renderizado desde src/page.html.")


if __name__ == "__main__":
    main()
