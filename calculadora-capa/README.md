# Calculadora Capa / El taller en 3D

Calculadora de producción 3D sin dependencias ni claves API: placas, filamentos, consumo eléctrico, insumos, precios por unidad y presupuesto imprimible.

## Uso

Abrir dist/index.html, o ejecutar `python -m http.server 8765 --directory dist` y visitar http://localhost:8765. Para publicar, usar dist como raíz del sitio estático. Los archivos tools y SECURITY.md no necesitan estar en la raíz pública.

Los presupuestos pertenecen al navegador y al origen: no se trasladan automáticamente al cambiar de dominio. Exportar los presupuestos necesarios antes de una migración.

Consultar SECURITY.md antes de publicar o incorporar integraciones. Ejecutar `python tools/update_csp.py` después de modificar el CSS o JavaScript inline.
