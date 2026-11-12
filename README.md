# PASS://GENERATOR

Generador de contraseñas aleatorias con controles configurables y generación criptográfica desde el navegador.

**Demo:** https://tzayadet.github.io/PassGen/  
**Código:** https://github.com/tzayadet/PassGen

## Funcionalidades

- Longitud configurable.
- Selección de mayúsculas, minúsculas, números y símbolos.
- Exclusión de caracteres visualmente similares o ambiguos.
- Opción para garantizar la presencia de los grupos de caracteres seleccionados.
- Generación de varias contraseñas en una operación.
- Copia individual o conjunta al portapapeles.
- Exportación de resultados a TXT.
- Interfaz adaptable con validación de configuración.

## Uso

Abre la [demo](https://tzayadet.github.io/PassGen/), configura los grupos de caracteres, la longitud y la cantidad, y genera las contraseñas.

También puedes descargar el repositorio y abrir `index.html` localmente.

## Tecnología y seguridad

La generación utiliza la API criptográfica del navegador (`Crypto.getRandomValues`). No se necesita una cuenta ni un backend propio.

La seguridad de una contraseña también depende de su almacenamiento y del servicio donde se utilice. No reutilices contraseñas y evita guardar las generadas en ubicaciones compartidas o sin protección.

## Despliegue

Aplicación estática publicada mediante GitHub Pages. La generación se realiza en el navegador.

## Licencia

Consulta [LICENSE](LICENSE).
