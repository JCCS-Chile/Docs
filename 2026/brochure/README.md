# JCCS 2026 Brochure

Este directorio contiene una migración inicial del brochure a **React + Vite**, sin versionar binarios ni assets generados.

La página visible vive en `src/page.html`, extraída desde el `index.html` exportado por Next. Vite la monta con React y el `postbuild` la deja pre-renderizada dentro de `dist/index.html`, para que el resultado sea similar al HTML estático actual.

## Cómo usar

```bash
cd 2026/brochure
npm install
npm run sync
npm run dev
npm run build
```

## Qué hace `sync`

El script `scripts/sync_from_export.py`:

1. Limpia los assets generados.
2. Copia CSS, fuentes y logos desde `../jccs-2026-site`.
3. Reescribe rutas internas de CSS para que funcionen como assets locales.
4. Genera `legacy-index.html` como referencia del export original sin usarlo como fuente principal.

## Editar la página

- Edita `src/page.html` para cambios directos sobre contenido y estructura.
- Edita `src/styles/site.css` para ajustes propios del wrapper React/Vite.
- Usa `scripts/extract_page_html.py` solo si necesitas regenerar `src/page.html` desde el export de Next.
- `npm run build` genera `dist/index.html` con el contenido ya pre-renderizado.

## Notas

- Se evita agregar binarios al PR mediante `.gitignore`.
- Esta es una base puente: desde aquí se pueden ir migrando secciones de `src/page.html` a componentes React más pequeños.
