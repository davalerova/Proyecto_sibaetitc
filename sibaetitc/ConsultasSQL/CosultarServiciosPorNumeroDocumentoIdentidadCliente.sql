SELECT nombre_servicio
FROM Servicios_servicio
INNER JOIN afiliacion_afiliacion_servicio
ON afiliacion_afiliacion_servicio.servicio_afiliacion_id=Servicios_servicio.id
INNER JOIN cliente_cliente
ON cliente_cliente.id=afiliacion_afiliacion_servicio.cliente_afiliacion_id
WHERE cliente_cliente.numero_documento_identidad_cliente='1014221407'