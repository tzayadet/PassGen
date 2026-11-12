# Password Generator

Generador de contraseñas aleatorias en el navegador, con controles de longitud, composición y exportación. La generación utiliza la API criptográfica del navegador; no necesita backend.

[![Pages deployment](https://github.com/tzayadet/PassGen/actions/workflows/static.yml/badge.svg)](https://github.com/tzayadet/PassGen/actions/workflows/static.yml)

**Demo:** [abrir Password Generator](https://tzayadet.github.io/PassGen/) · **Código:** [repositorio](https://github.com/tzayadet/PassGen)

## Funciones

- Longitud y cantidad configurables.
- Mayúsculas, minúsculas, números y símbolos seleccionables.
- Exclusión de caracteres ambiguos.
- Garantía de inclusión de los grupos elegidos.
- Copia individual o conjunta y exportación TXT.

## Uso

Abre la demo, ajusta la composición y genera las contraseñas. También puedes descargar el repositorio y abrir `index.html` localmente.

## Seguridad y privacidad

La generación usa `Crypto.getRandomValues()` en el navegador. No se envían las contraseñas a un backend. Evita reutilizarlas y no guardes los resultados en ubicaciones compartidas o sin protección.

## Despliegue

Sitio estático publicado mediante GitHub Pages. No requiere servidor.

## Licencia

Consulta [LICENSE](LICENSE).
