#!/usr/bin/env bash
# Instala las habilidades del kit «estudio-ia-publica» para Codex y Cursor
# (y cualquier agente que lea la carpeta estándar ~/.agents/skills).
#
#   curl -fsSL https://raw.githubusercontent.com/jordansrojas1/estudio-ia-publica/main/instalar.sh | bash
#
# Qué hace, nada más: descarga el kit de GitHub y copia tres carpetas
# (pieza-ciudadana, auditar-diseno, referencias-visuales) en ~/.agents/skills.
# Si ya tenías una carpeta con el mismo nombre, la guarda en ~/.agents/skills-respaldo.
# Autor: Jordan Rojas · MIT · ver CREDITOS.md
set -euo pipefail

REPO="jordansrojas1/estudio-ia-publica"
DESTINO="${1:-$HOME/.agents/skills}"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

echo ""
echo "  Kit de diseño con IA para la gestión pública"
echo "  Instalando para Codex y Cursor en: $DESTINO"
echo ""

curl -fsSL "https://github.com/$REPO/archive/refs/heads/main.tar.gz" | tar -xz -C "$TMP"
ORIGEN="$TMP/estudio-ia-publica-main/plugins/diseno-publico/skills"
mkdir -p "$DESTINO"

for carpeta in "$ORIGEN"/*/; do
  nombre="$(basename "$carpeta")"
  if [ -d "$DESTINO/$nombre" ]; then
    if [ -f "$DESTINO/$nombre/.estudio-ia-publica" ]; then
      rm -rf "$DESTINO/$nombre"                       # versión anterior del kit: se actualiza
    else
      respaldo="$(dirname "$DESTINO")/skills-respaldo/$nombre-$(date +%Y%m%d%H%M%S)"
      mkdir -p "$(dirname "$respaldo")"
      mv "$DESTINO/$nombre" "$respaldo"               # carpeta ajena: se guarda fuera, no se borra
      echo "  (ya tenías '$nombre': la guardé en $respaldo)"
    fi
  fi
  cp -R "$carpeta" "$DESTINO/$nombre"
  echo "kit estudio-ia-publica" > "$DESTINO/$nombre/.estudio-ia-publica"
  echo "  ✓ $nombre"
done

echo ""
echo "  ¡Listo! Cierra y vuelve a abrir Codex o Cursor."
echo "  Pruébalo:  Codex → escribe \$pieza-ciudadana   ·   Cursor → escribe /pieza-ciudadana"
echo "  Créditos: https://github.com/$REPO/blob/main/CREDITOS.md"
echo ""
