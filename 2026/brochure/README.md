# JCCS 2026 Brochure (sin binarios versionados)

Este directorio ahora contiene **solo archivos fuente de mantenimiento**.

Los binarios y archivos generados (`assets/*`, `index.html`) se reconstruyen localmente desde `2026/jccs-2026-site`.

## Cómo usar

```bash
cd 2026/brochure
npm run sync
npm run start
```

## Qué hace `sync`

El script `scripts/sync_from_export.py`:

1. Limpia `assets/` en `2026/brochure`.
2. Copia CSS, JS, media y logos desde `../jccs-2026-site`.
3. Genera `index.html` ajustando rutas `/jccs-2026/...` a `./assets/...`.

## Notas

- Se evita agregar binarios al PR mediante `.gitignore`.
- Esta es una base para seguir migrando el brochure hacia HTML/CSS/JS mantenible manualmente.
