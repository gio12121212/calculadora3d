# Seguridad de Calculadora Capa

Alcance: calculadora estática en `dist/index.html`. No incluye la tienda El taller en 3D ni su administración.

## Arquitectura

No utiliza claves API, backend, cuentas de usuario ni dependencias JavaScript externas. Los cálculos se realizan en el navegador. Los presupuestos se guardan en localStorage: no están cifrados y son accesibles para quien use el mismo perfil del navegador. No almacenar contraseñas, documentos ni datos sensibles de clientes.

La política CSP permite únicamente el script y la hoja de estilos cuyos hashes coinciden con esta versión. Bloquea conexiones de la aplicación a APIs, scripts externos, manejadores HTML en línea, formularios, marcos y objetos. Los nombres proporcionados por usuarios se presentan mediante textContent/value, no como HTML. Las plantillas innerHTML solo interpolan constantes e identificadores numéricos generados internamente.

## Al modificar el archivo

Ejecutar `python tools/update_csp.py` tras cambiar el JavaScript o CSS. No reemplazar los hashes por unsafe-inline ni unsafe-eval. Comprobar cálculo, guardado, copiar, impresión y navegación en el navegador después del cambio.

## Publicación

Publicar únicamente el directorio dist como web. El paquete para GitHub excluye .git, metadatos del alojamiento, archivos de trabajo, capturas y presupuestos. La revisión por patrones del historial disponible no detectó credenciales; no es una garantía de detección de todos los secretos.

No colocar secretos en HTML, JavaScript, localStorage ni variables de compilación expuestas al cliente. Si una futura integración necesita una clave privada, utilizar un backend con secretos del servidor, permisos mínimos, validación y límites de solicitudes. Cifrar una clave y distribuir su descifrado con el frontend no la mantiene privada.

El .gitignore previene algunos errores, pero no elimina archivos ya versionados ni reemplaza un escáner de secretos. Una credencial expuesta debe revocarse o rotarse, aunque se quite del archivo o historial.

## Límites y configuración del alojamiento

La CSP se entrega por meta para conservar compatibilidad con alojamiento estático. No incluye protección frame-ancestors: esa directiva solo funciona como cabecera HTTP. En un proveedor que permita cabeceras, configurar Content-Security-Policy frame-ancestors para los orígenes autorizados, X-Content-Type-Options: nosniff y Permissions-Policy para desactivar cámara, micrófono y geolocalización. Verificar su respuesta real tras desplegar. No bloquear todos los marcos si se mantiene la calculadora integrada en la tienda.

Usar HTTPS, autenticación de dos factores en la cuenta de GitHub y revisar los permisos de colaboradores. La seguridad de la cuenta y del alojamiento no fue auditada. No se realizaron pruebas de penetración contra infraestructura ni se garantiza inmunidad a ataques.

Referencias: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP y https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository
