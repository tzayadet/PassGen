<p align="center">
  <img src="https://img.shields.io/badge/SECURITY_UTILITY-PASSWORD_GENERATOR-101010?style=for-the-badge&labelColor=050805&color=00FF41" alt="Password Generator"/>
  <img src="https://img.shields.io/badge/BROWSER-NATIVE_CRYPTO-101010?style=for-the-badge&logo=googlechrome&logoColor=00FF41" alt="Browser native crypto"/>
</p>

# Password Generator

Generador de contraseñas en el navegador con controles de longitud, composición y exportación. Utiliza la API criptográfica del navegador y no necesita backend.

<p align="center">
  <a href="https://tzayadet.github.io/PassGen/"><strong>LIVE DEMO ↗</strong></a> ·
  <a href="https://github.com/tzayadet/PassGen"><strong>SOURCE CODE</strong></a>
</p>

[![Pages deployment](https://github.com/tzayadet/PassGen/actions/workflows/static.yml/badge.svg)](https://github.com/tzayadet/PassGen/actions/workflows/static.yml)

## Features

- Longitud y cantidad configurables.
- Selección de mayúsculas, minúsculas, números y símbolos.
- Exclusión de caracteres ambiguos.
- Inclusión garantizada de los grupos seleccionados.
- Copia individual o conjunta.
- Exportación de resultados a TXT.

## Use it

Abre la [demo web](https://tzayadet.github.io/PassGen/) en un navegador moderno o descarga el repositorio y abre `index.html`.

No necesita instalación, cuenta ni servidor.

## Security & privacy

La generación utiliza `Crypto.getRandomValues()` en el navegador. Las contraseñas se generan localmente y no se envían a un backend.

La seguridad de una contraseña también depende de su longitud, unicidad, almacenamiento y del servicio donde se utilice. No reutilices contraseñas ni guardes exportaciones en ubicaciones compartidas o sin protección.

## Technology

- HTML5
- CSS3
- JavaScript
- Web Crypto API
- Clipboard API

## Deployment

Aplicación estática publicada mediante GitHub Pages. El navegador ejecuta toda la funcionalidad; no hay backend propio.

## License

See [LICENSE](LICENSE).
