# Envío de recordatorios a speakers

Este directorio contiene el flujo local para enviar recordatorios mediante
[`mailmerge`](https://github.com/awdeorio/mailmerge). El contenido HTML está en
`speakers/template-reminder-20260728.mailmerge.html`; el archivo
`speakers/template-reminder-20260728.email.mailmerge` agrega las cabeceras de
correo necesarias para el envío (destinatario, remitente y asunto).

## Datos locales y privacidad

Los CSV de speakers y de pruebas contienen datos personales. No deben subirse al
repositorio ni enviarse fuera del proceso de mail merge. Los archivos de datos,
la configuración SMTP, el entorno virtual y las salidas locales ya están
excluidos en `.gitignore`.

- CSV real: `speakers/2026-speaker-info.csv` (local e ignorado).
- CSV de prueba: `speakers/2026-speaker-test-recipients.csv` (local e ignorado).
- Configuración SMTP local: `mailmerge_server.conf` (local e ignorada).

No guarde contraseñas en archivos. `mailmerge` la solicitará de manera
interactiva al realizar un envío real.

## Preparación

Desde `2026/mailings`, cree o actualice el entorno virtual:

```bash
python3 -m venv .venv-mailmerge
.venv-mailmerge/bin/python -m pip install -r requirements-mailmerge.txt
```

Prepare la configuración SMTP local a partir del ejemplo y complete los datos
entregados por el proveedor de correo:

```bash
cp mailmerge_server.conf.example mailmerge_server.conf
```

El valor de `From` está definido en
`speakers/template-reminder-20260728.email.mailmerge`. Antes de enviar, confirme
que corresponde a la cuenta SMTP configurada y que el servidor permite usarlo.

### Google Workspace

Para Google Workspace, configure `host = smtp.gmail.com`, `port = 465` y
`security = SSL/TLS`. El usuario debe ser la dirección completa de la cuenta.
Google exige autenticación y, para este tipo de cliente SMTP, normalmente se usa
una contraseña de aplicación en lugar de la contraseña habitual de la cuenta.
No la guarde en `mailmerge_server.conf`: el comando la solicitará al enviar.

## Previsualización obligatoria

Ejecute primero una simulación con el CSV de prueba. No establece conexión SMTP
ni envía correos:

```bash
.venv-mailmerge/bin/mailmerge \
  --dry-run \
  --template speakers/template-reminder-20260728.email.mailmerge \
  --database speakers/2026-speaker-test-recipients.csv \
  --config mailmerge_server.conf \
  --output-format text
```

Revise en la salida el destinatario, el asunto, el bloque de participación, los
saltos de línea y el recordatorio de presentación. En el CSV de prueba,
`Entrega Presentación=TRUE`, por lo que el recordatorio PPT/PDF debe aparecer.

## Envío real

Después de validar la simulación, haga una última revisión del CSV real y ejecute
el envío. `--no-limit` es necesario para procesar todos los registros; sin esa
opción, `mailmerge` procesa sólo el primero.

```bash
.venv-mailmerge/bin/mailmerge \
  --no-dry-run \
  --no-limit \
  --template speakers/template-reminder-20260728.email.mailmerge \
  --database speakers/2026-speaker-info.csv \
  --config mailmerge_server.conf \
  --output-format text
```

Este comando envía correos reales y solicitará la contraseña SMTP. Si el proceso
se interrumpe, retómelo desde el siguiente registro con `--resume N`, donde `N`
es el número de mensaje que falta por enviar.

## Reglas del template

- El destinatario se toma de `Correo Electrónico Directo`.
- `Entrega Presentación=TRUE` muestra el recordatorio de enviar PPT o PDF;
  `FALSE` lo oculta.
- Los saltos de línea de `Participación Bloque/Panel` se convierten en `<br>`.

## Notificaciones de resultado CFP

Las plantillas en `cfp/template-notification-20260803.email.mailmerge` y
`cfp/template-notification-20260803.mailmerge.html` notifican el resultado de la
convocatoria usando `cfp/2026-cfp_speaker-info.csv`.

- Los CSV real y de prueba (`cfp/2026-cfp_speaker-info.csv` y
  `cfp/2026-cfp-test-recipients.csv`) contienen datos personales y están
  excluidos del repositorio.
- La columna `Aceptada` determina el contenido: `TRUE` envía la notificación de
  aceptación y `FALSE` la de no aceptación.
- Para contribuciones aceptadas, la plantilla personaliza el título y horario de
  presentación; además solicita una biografía de hasta 80 palabras y las
  diapositivas antes del sábado 8 de agosto a las 23:59 hrs.
- La plantilla no debe enviarse sin previsualizar cada una de las dos ramas.

Previsualización local, sin envío SMTP:

```bash
.venv-mailmerge/bin/mailmerge \
  --dry-run \
  --template cfp/template-notification-20260803.email.mailmerge \
  --database cfp/2026-cfp-test-recipients.csv \
  --config mailmerge_server.conf \
  --output-format text
```
