# JCCS 2026 Site

Este directorio contiene el sitio JCCS 2026 en **Astro + React Islands**, sin versionar binarios ni assets generados.

La home conserva temporalmente el cuerpo heredado de `src/page.html`, extraído desde el `index.html` exportado por Next. Astro aporta el layout común, las rutas del sitio y deja React reservado para islas interactivas pequeñas, como la cuenta regresiva.

## Cómo usar

```bash
cd 2026
npm install
npm run sync
npm run dev
npm run build
```

## Qué hace `sync`

El script `scripts/sync_from_export.py`:

1. Limpia los assets generados.
2. Copia CSS, fuentes y logos desde `jccs-2026-site`.
3. Reescribe rutas internas de CSS para que funcionen como assets locales.
4. Copia las imágenes del CFP hacia `public/CFP/images`.
5. Genera `legacy-index.html` como referencia del export original sin usarlo como fuente principal.

## Editar la página

- Edita `src/page.html` para cambios directos sobre el cuerpo heredado de la home.
- Edita `src/components/SiteHeader.astro` y `src/components/SiteFooter.astro` para navegación y footer compartidos.
- Edita `src/styles/site.css` para ajustes propios del sitio Astro.
- Usa `scripts/extract_page_html.py` solo si necesitas regenerar `src/page.html` desde el export de Next.
- `CFP/index.md` y `PRIVACY.md` son las fuentes Markdown de `/CFP/` y `/privacy/`.
- `npm run build` genera el sitio estático en `dist/`.

## Notas

- Se evita agregar binarios al PR mediante `.gitignore`.
- Esta sigue siendo una base puente: desde aquí se pueden ir migrando secciones de `src/page.html` a componentes Astro más pequeños.

## Configuración del enlace de registro

- **Variable:** `PUBLIC_REGISTRATION_SITE` — URL pública al formulario de inscripción (ej. https://inguandes.typeform.com/to/gtDo6MI8#source=xxxxx).
- **Dónde se usa:** el `SiteHeader` y `SiteFooter` leen esta variable en tiempo de build/cliente y mostrarán un botón `Regístrate` que abre la URL en una nueva pestaña. Si no está definida, se usa el fallback local `CFP/`.
- **Cómo configurarla (desarrollo):** crea un fichero `.env` en el root con:

```env
PUBLIC_REGISTRATION_SITE=https://inguandes.typeform.com/to/gtDo6MI8#source=xxxxx
```

- **Nota:** Astro (Vite) expone sólo las variables con prefijo `PUBLIC_` al cliente. Reinicia el servidor de desarrollo (`npm run dev`) después de cambiar `.env`.
- **Producción:** configura la variable de entorno `PUBLIC_REGISTRATION_SITE` en tu proveedor de hosting (Netlify, Vercel, etc.) para que la URL esté disponible en el build.
- **Ejemplo:** ya existe un `.env.example` con el valor de ejemplo.
