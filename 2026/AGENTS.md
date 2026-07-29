# AGENTS.md

Guia operativa para agentes de codigo trabajando en el sitio JCCS 2026.

## Resumen del proyecto

Este proyecto es un sitio estatico de JCCS 2026 construido con Astro y React Islands.

- Astro controla rutas, layout comun y build estatico.
- React se usa solo para islas interactivas pequenas. Actualmente la isla principal es la cuenta regresiva en `src/components/Countdown.jsx`.
- La home conserva temporalmente HTML heredado en `src/page.html`. La pagina Astro `src/pages/index.astro` extrae el cuerpo de ese HTML y reemplaza header/footer por componentes compartidos.
- El CFP y la politica de privacidad se mantienen como Markdown fuente en la raiz del contenido y se renderizan dentro del layout Astro.

## Dependencias principales

- `astro`: framework principal y generador estatico.
- `@astrojs/react`: integracion para usar islas React.
- `react` y `react-dom`: runtime de las islas React.
- `serve`: utilidad legacy para servir archivos estaticos cuando haga falta.
- `typescript`: disponible como herramienta de soporte, aunque el codigo actual es JS/Astro.

La configuracion Astro vive en `astro.config.mjs` y usa `output: "static"`.

## Estructura importante

- `src/pages/index.astro`: ruta `/`; compone el layout comun con el cuerpo heredado de `src/page.html`.
- `src/pages/CFP/index.astro`: ruta `/CFP/`; renderiza `CFP/index.md`.
- `src/pages/privacy/index.astro`: ruta `/privacy/`; renderiza `PRIVACY.md`.
- `src/layouts/SiteLayout.astro`: HTML base, metadata y hojas CSS heredadas desde `assets/css`.
- `src/components/SiteHeader.astro`: header compartido y navegacion principal.
- `src/components/SiteFooter.astro`: footer compartido, enlaces e instituciones.
- `src/data/schedule.json`: fuente de la agenda visible en la home; `src/components/Schedule.astro` la renderiza. Para cambios de horarios, actividades, duraciones o expositores, editar este archivo.
- `src/config/site.js`: configuracion central; lee `PUBLIC_REGISTRATION_SITE`.
- `src/utils/markdown.js`: renderer Markdown simple usado por CFP y privacidad.
- `src/styles/site.css`: estilos propios del sitio Astro y ajustes del wrapper.
- `CFP/index.md`: fuente de contenido del llamado a contribuciones.
- `CFP/images/`: imagenes fuente del CFP.
- `PRIVACY.md`: fuente de contenido para `/privacy/`.

## Comandos

Comandos esperados desde la raiz `2026`:

```bash
npm install
npm run dev
npm run build
npm run preview
```

Los scripts `dev`, `build` y `preview` desactivan telemetry de Astro con `ASTRO_TELEMETRY_DISABLED=1`, porque algunos entornos sandbox no permiten escribir preferencias fuera del workspace.

No hay scripts de sincronizacion legacy en el flujo actual. Si reaparece un directorio `scripts/` en una rama futura, verifica su estado antes de documentarlo o depender de el.

## Assets y archivos generados

No versionar:

- `node_modules/`
- `dist/`
- `.astro/`
- `public/assets/`
- `public/CFP/images/`
- `legacy-index.html`

Los assets visibles en produccion deben estar disponibles desde `public/` durante el build. Las imagenes fuente del CFP viven en `CFP/images/`; si se copian a `public/CFP/images/`, ese destino es generado e ignorado por Git.

## Variables de entorno

Variable publica:

```env
PUBLIC_REGISTRATION_SITE=https://inguandes.typeform.com/to/gtDo6MI8#source=xxxxx
```

Uso:

- `SiteHeader.astro` muestra el boton `Regístrate`.
- `SiteFooter.astro` usa la misma URL para `Inscribirse`.
- Si la variable no existe, ambos componentes vuelven al fallback local `CFP/`.

Solo variables con prefijo `PUBLIC_` se exponen al cliente en Astro/Vite. Reinicia `npm run dev` despues de cambiar `.env`.

## Reglas de edicion

- Para cambiar navegacion, CTAs globales o logos del footer, editar `SiteHeader.astro` y `SiteFooter.astro`.
- Para cambiar metadata global, hojas CSS heredadas o estructura HTML base, editar `SiteLayout.astro`.
- Para cambios de contenido del CFP, editar `CFP/index.md`.
- Para cambios de privacidad, editar `PRIVACY.md`.
- Para cambios estructurales de la home, preferir migrar trozos desde `src/page.html` hacia componentes Astro nuevos. Evita agrandar mas el HTML heredado salvo cambios puntuales.
- Para cambios en la agenda visible, editar `src/data/schedule.json`; actualizar tambien `src/page.html` solo si se necesita conservar consistente el bloque heredado de la home.
- Para interactividad nueva, usar una isla React solo cuando sea necesaria; lo estatico debe quedarse en Astro.
- El renderer de Markdown en `src/utils/markdown.js` es deliberadamente simple. Si necesitas Markdown mas completo, considera migrar a soporte Markdown nativo de Astro o a una libreria/pipe de remark antes de agregar regex ad hoc complejas.

## Verificacion antes de cerrar cambios

Ejecutar, cuando sea posible:

```bash
npm run build
```

Luego revisar que existan las rutas estaticas esperadas:

- `dist/index.html`
- `dist/CFP/index.html`
- `dist/privacy/index.html`

Si se levanta servidor local, comprobar:

- `/`
- `/CFP/`
- `/privacy/`
- assets del CFP como `/CFP/images/header.png`

## Deploy

El deploy de GitHub Pages vive en `.github/workflows/deploy-pages.yml`, en la raiz del repositorio.

- Construye el sitio desde `2026/`.
- Usa `PUBLIC_BASE_PATH=/Docs/2026/` para que los assets de Astro funcionen bajo GitHub Pages.
- Lee `PUBLIC_REGISTRATION_SITE` desde las repository variables de GitHub Actions.
- Publica el build de 2026 dentro de `_site/2026/` y preserva `2023/` si existe.

## Contexto de migracion

Este sitio sigue siendo una base puente. La direccion deseada es ir reduciendo `src/page.html` y reemplazarlo gradualmente por componentes Astro pequenos y mantenibles, conservando header/footer compartidos y usando React Islands solo para comportamiento interactivo.
