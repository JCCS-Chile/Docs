#!/usr/bin/env python3
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT.parent / "jccs-2026-site"
TARGET = ROOT
PUBLIC = TARGET / "public"

COPY_MAP = {
    SOURCE / "_next/static/css": PUBLIC / "assets/css",
    SOURCE / "_next/static/media": PUBLIC / "assets/media",
    SOURCE / "logos": PUBLIC / "assets/logos",
}

REPLS = {
    '/jccs-2026/_next/static/css/': './assets/css/',
    '/jccs-2026/_next/static/chunks/app/': './assets/js/',
    '/jccs-2026/_next/static/chunks/pages/': './assets/js/',
    '/jccs-2026/_next/static/chunks/': './assets/js/',
    '/jccs-2026/_next/static/media/': './assets/media/',
    '/jccs-2026/logos/': './assets/logos/',
}

CSS_REPLS = {
    '/jccs-2026/_next/static/media/': '../media/',
}


def ensure_clean_assets() -> None:
    for assets in (TARGET / "assets", PUBLIC / "assets"):
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
                dst = dst_dir / path.name
                shutil.copy2(path, dst)
                if dst.suffix == ".css":
                    css = dst.read_text(encoding="utf-8")
                    for old, new in CSS_REPLS.items():
                        css = css.replace(old, new)
                    dst.write_text(css, encoding="utf-8")


def generate_index() -> None:
    raw = (SOURCE / "index.html").read_text(encoding="utf-8")
    for old, new in REPLS.items():
        raw = raw.replace(old, new)
    (TARGET / "legacy-index.html").write_text(raw, encoding="utf-8")


def main() -> None:
    if not SOURCE.exists():
        raise FileNotFoundError(f"No se encontró el sitio origen: {SOURCE}")
    ensure_clean_assets()
    copy_assets()
    generate_index()
    print("Brochure sincronizado en 2026/brochure (public/assets/* + legacy-index.html).")


if __name__ == "__main__":
    main()
