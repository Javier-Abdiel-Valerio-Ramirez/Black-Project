# Decisiones de Diseño — ERP Django
## Espiral 2 · Modelo Entidad-Relación

---

### D-01: Producto → Categoria usa on_delete=PROTECT
**Decisión:** No permitir borrar una categoría si tiene productos asociados.
**Consecuencia:** Para borrar una categoría, primero se deben reasignar sus productos. Evita perder histórico.

---

### D-02: Producto → Proveedor usa on_delete=SET_NULL, null=True
**Decisión:** Un producto puede existir sin proveedor asignado (ej. productos de fabricación propia).
**Justificación:** Al borrar un proveedor, los productos quedan registrados pero sin proveedor asignado.

---

### D-03: Venta → Cliente usa on_delete=PROTECT
**Decisión:** No borrar un cliente con historial de ventas.
**Justificación legal:** El historial de ventas es un registro contable y fiscal. Se debe usar `activo=False` para desactivar al cliente.

---

### D-04: Venta.total es propiedad calculada (NO campo de BD)
**Decisión:** `total` se calcula dinámicamente mediante `@property` sumando los subtotales de `DetalleVenta`.
**Justificación:** Guardar el total violaría la 3FN (dependencia transitiva). Evita inconsistencias si se modifica una línea de detalle.

---

### D-05: DetalleVenta → Producto usa on_delete=PROTECT
**Decisión:** No borrar un producto que tuvo ventas históricas.
**Justificación:** Los reportes de ventas necesitan mantener la referencia al producto. Se usa `activo=False` para descontinuarlo.

---

### D-06: DetalleVenta.precio_unitario es campo almacenado
**Decisión:** Almacenar el precio al momento exacto de la venta, no derivarlo de `Producto.precio`.
**Justificación:** El precio de catálogo de un producto cambia con el tiempo. La venta debe reflejar lo que realmente se cobró en ese momento.

---

### D-07: ConfiguracionERP como singleton
**Decisión:** Una sola fila para la configuración global del sistema (`pk=1`).
**Justificación:** Se sobrescribe el método `save()` para forzar `pk=1` y garantizar una única instancia de configuración.