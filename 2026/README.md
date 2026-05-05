# JCCS 2026 Site

Sitio web de la **3ª Jornada Chilena de Ciberseguridad en Salud 2026**.

El proyecto está construido con **Astro** y usa **React Islands** sólo para interactividad puntual, como la cuenta regresiva de la home. El sitio se genera como HTML estático en `dist/`.

## Requisitos

- Node.js compatible con Astro 6
- npm

## Desarrollo

```bash
npm install
npm run dev
```

El servidor local queda disponible en:

```text
http://127.0.0.1:4321/
```

## Build

```bash
npm run build
```

El build estático se genera en `dist/`.

Para revisar el build localmente:

```bash
npm run preview
```

## Arquitectura

- `src/pages/index.astro` genera la home (`/`).
- `src/pages/CFP/index.astro` genera el llamado a contribuciones (`/CFP/`).
- `src/pages/privacy/index.astro` genera la política de privacidad (`/privacy/`).
- `src/layouts/SiteLayout.astro` define el HTML base, metadata y hojas CSS heredadas.
- `src/components/SiteHeader.astro` y `src/components/SiteFooter.astro` son compartidos por todas las páginas.
- `src/components/Countdown.jsx` es la isla React que actualiza la cuenta regresiva.
- `src/config/site.js` centraliza configuración pública del sitio.
- `src/styles/site.css` contiene estilos propios del wrapper Astro y ajustes adicionales.

La home todavía conserva parte del HTML heredado en `src/page.html`. `src/pages/index.astro` toma ese contenido y reemplaza el header/footer por componentes Astro compartidos. La intención es migrar gradualmente ese HTML a componentes Astro más pequeños.

## Contenido

- Edita `src/page.html` para cambios puntuales en el cuerpo heredado de la home.
- Edita `CFP/index.md` para actualizar el contenido del CFP.
- Edita `PRIVACY.md` para actualizar la política de privacidad.
- Edita `SiteHeader.astro` y `SiteFooter.astro` para navegación, CTAs globales y footer.

Las imágenes fuente del CFP viven en `CFP/images/`.

## Variables públicas

El sitio usa variables públicas de Astro para enlaces que se muestran a participantes:

```env
PUBLIC_CFP_FORM_URL=https://inguandes.typeform.com/to/gp4aQlp7
PUBLIC_CONTACT_EMAIL=jccs.contacto@proton.me
PUBLIC_REGISTRATION_SITE=https://inguandes.typeform.com/to/gtDo6MI8#source=xxxxx
```

En desarrollo, crea un archivo `.env` en la raíz. Hay un `.env.example` como referencia.

Si `PUBLIC_CFP_FORM_URL` o `PUBLIC_CONTACT_EMAIL` no están definidas, sus enlaces y botones no se renderizan. Si `PUBLIC_REGISTRATION_SITE` no está definida, el sitio usa `/CFP/` como fallback. Astro sólo expone al cliente variables con prefijo `PUBLIC_`; reinicia `npm run dev` después de cambiar `.env`.

En producción, configura estas variables en el proveedor de hosting antes del build.

## Deploy en GitHub Pages

El workflow `.github/workflows/deploy-pages.yml` publica el sitio en GitHub Pages al hacer push a `main`.

- El sitio 2026 se compila desde este directorio y se publica bajo `/Docs/2026/`.
- El workflow usa `PUBLIC_BASE_PATH=/Docs/2026/` para que Astro genere rutas correctas de assets.
- `PUBLIC_CFP_FORM_URL`, `PUBLIC_CONTACT_EMAIL` y `PUBLIC_REGISTRATION_SITE` se leen desde **Settings → Secrets and variables → Actions → Variables** como variables de repositorio.
- Si no configuras `PUBLIC_REGISTRATION_SITE`, el sitio usa `/CFP/` como fallback para registro.

En GitHub Pages, configura el source como **GitHub Actions**.

## Archivos generados

No se versionan:

- `node_modules/`
- `.astro/`
- `dist/`
- `public/assets/`
- `public/CFP/images/`
- `legacy-index.html`

## Guía para agentes

Las instrucciones operativas para herramientas como Codex, Claude u otros agentes están en `AGENTS.md`.
