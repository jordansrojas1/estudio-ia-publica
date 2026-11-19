#!/usr/bin/env bash
# Vuelve a crear los ZIP de descargas/ a partir de las habilidades.
# Cada ZIP lleva la carpeta de la habilidad en la raíz (así lo pide claude.ai).
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p descargas
rm -f descargas/*.zip
cd plugins/diseno-publico/skills
for s in */; do
  s="${s%/}"
  zip -qrX "../../../descargas/$s.zip" "$s" -x '*.DS_Store' -x '*__pycache__*'
done
cd ../../..
zip -qj descargas/kit-completo.zip descargas/*.zip CREDITOS.md
ls -la descargas
