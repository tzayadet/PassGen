# Password Generator

A browser-based password generator using the Web Crypto API. It runs locally in the browser and does not require an account, backend or installation.

<p align="center">
  <a href="https://tzayadet.github.io/PassGen/"><img src="https://img.shields.io/badge/LIVE_DEMO-OPEN-00a86b?style=flat-square" alt="Live demo"></a>
  <a href="https://github.com/tzayadet/PassGen"><img src="https://img.shields.io/badge/SOURCE-GITHUB-161b22?style=flat-square&logo=github" alt="Source"></a>
</p>

[![Pages deployment](https://github.com/tzayadet/PassGen/actions/workflows/static.yml/badge.svg)](https://github.com/tzayadet/PassGen/actions/workflows/static.yml)

[![Quality checks](https://github.com/tzayadet/PassGen/actions/workflows/quality.yml/badge.svg)](https://github.com/tzayadet/PassGen/actions/workflows/quality.yml)

## Features

- Configurable password length and quantity.
- Uppercase, lowercase, numeric and symbol character sets.
- Optional exclusion of ambiguous characters.
- Ensures selected character groups are represented.
- Individual or bulk clipboard copy.
- TXT export.

## Use it

Open the [live demo](https://tzayadet.github.io/PassGen/) or download the repository and open `index.html` in a modern browser.

## Technology

- HTML5 and CSS3
- JavaScript
- Web Crypto API
- Clipboard API

## Security and privacy

Generation uses `crypto.getRandomValues()` in the browser. Passwords are generated locally and are not sent to a project backend.

Password security also depends on length, uniqueness, storage and the service where a password is used. Avoid reuse and protect exported files.

## Validation

The quality workflow checks the inline JavaScript syntax and verifies that password generation uses the Web Crypto API:

```bash
python scripts/validate_site.py
```

Requires Python 3.11+ and Node.js 22+.

## Deployment

Static browser application published through GitHub Pages. No project backend is required.

## License

See [LICENSE](LICENSE) for the repository's licensing terms.
