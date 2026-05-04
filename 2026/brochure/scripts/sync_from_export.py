#!/usr/bin/env python3
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT.parent / "jccs-2026-site"
TARGET = ROOT

COPY_MAP = {
    SOURCE / "_next/static/css": TARGET / "assets/css",
    SOURCE / "_next/static/chunks": TARGET / "assets/js",
    SOURCE / "_next/static/chunks/app": TARGET / "assets/js",
    SOURCE / "_next/static/chunks/pages": TARGET / "assets/js",
    SOURCE / "_next/static/media": TARGET / "assets/media",
    SOURCE / "logos": TARGET / "assets/logos",
}

REPLS = {
    '/jccs-2026/_next/static/css/': './assets/css/',
    '/jccs-2026/_next/static/chunks/app/': './assets/js/',
    '/jccs-2026/_next/static/chunks/pages/': './assets/js/',
    '/jccs-2026/_next/static/chunks/': './assets/js/',
    '/jccs-2026/_next/static/media/': './assets/media/',
    '/jccs-2026/logos/': './assets/logos/',
}


def ensure_clean_assets() -> None:
    assets = TARGET / "assets"
    if assets.exists():
        shutil.rmtree(assets)
    assets.mkdir(parents=True, exist_ok=True)


def copy_assets() -> None:
    for src_dir, dst_dir in COPY_MAP.items():
        dst_dir.mkdir(parents=True, exist_ok=True)
        if not src_dir.exists():
            raise FileNotFoundError(f"No existe el origen requerido: {src_dir}")
        for path in src_dir.glob("*"):
            if path.is_file():
                shutil.copy2(path, dst_dir / path.name)


def generate_index() -> None:
    raw = (SOURCE / "index.html").read_text(encoding="utf-8")
    for old, new in REPLS.items():
        raw = raw.replace(old, new)
    (TARGET / "index.html").write_text(raw, encoding="utf-8")


def main() -> None:
    if not SOURCE.exists():
        raise FileNotFoundError(f"No se encontró el sitio origen: {SOURCE}")
    ensure_clean_assets()
    copy_assets()
    generate_index()
    print("Brochure sincronizado en 2026/brochure (index.html + assets/*).")


if __name__ == "__main__":
    main()
