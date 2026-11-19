#!/usr/bin/env python3
"""Contraste WCAG de una paleta.

Saca los colores de los archivos que le pases (CSS, DESIGN.md, tokens, lo que
sea), los cruza contra los fondos y dice cuáles no pasan AA. Sin dependencias.

    python contraste.py src/**/*.css --fondo "#F6F2EC,#FFFFFF"
    python contraste.py DESIGN.md                 # adivina los fondos
    python contraste.py tokens.css --json         # para encadenar

Un color que falla no siempre es un bug: AA (4.5:1) es para texto normal, AA
grande (3:1) vale desde 18.66px en negrita o 24px normal, y los estados
deshabilitados están exentos. El script marca el número; la decisión de si ese
color es texto que alguien tiene que leer es tuya, y hay que mirarla en el
código antes de cambiar nada.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

HEX = re.compile(r"#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})\b")
# Nombre del token justo antes del color: --papel-crema: #F6F2EC / papel: "#F6F2EC"
NOMBRE = re.compile(r"(?:--)?([a-zA-Z][\w-]{2,40})\s*[:=]\s*[\"']?\s*$")

# En Windows la consola es cp1252 y se atraganta con los acentos de la tabla.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

AA, AA_GRANDE = 4.5, 3.0


def normaliza(h: str) -> str:
    h = h.lstrip("#").lower()
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return "#" + h


def luminancia(h: str) -> float:
    h = normaliza(h).lstrip("#")
    canales = []
    for i in (0, 2, 4):
        v = int(h[i : i + 2], 16) / 255
        canales.append(v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4)
    r, g, b = canales
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contraste(a: str, b: str) -> float:
    l1, l2 = sorted((luminancia(a), luminancia(b)), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)


def extrae(rutas: list[Path]) -> dict[str, dict]:
    """{color: {"nombres": {...}, "veces": n}} en orden de aparición."""
    hallados: dict[str, dict] = {}
    for ruta in rutas:
        try:
            texto = ruta.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            print(f"  (no se pudo leer {ruta}: {e})", file=sys.stderr)
            continue
        for linea in texto.splitlines():
            for m in HEX.finditer(linea):
                color = normaliza(m.group(0))
                reg = hallados.setdefault(color, {"nombres": set(), "veces": 0})
                reg["veces"] += 1
                etiqueta = NOMBRE.search(linea[: m.start()])
                if etiqueta:
                    reg["nombres"].add(etiqueta.group(1))
    return hallados


def adivina_fondos(hallados: dict) -> list[str]:
    """Sin --fondo: el color claro más repetido y, si lo hay, el oscuro."""
    claros = [(c, d["veces"]) for c, d in hallados.items() if luminancia(c) > 0.55]
    oscuros = [(c, d["veces"]) for c, d in hallados.items() if luminancia(c) < 0.08]
    fondos = []
    if claros:
        fondos.append(max(claros, key=lambda x: x[1])[0])
    if oscuros:
        fondos.append(max(oscuros, key=lambda x: x[1])[0])
    return fondos or ["#ffffff"]


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("archivos", nargs="+", help="CSS, DESIGN.md, tokens… admite globs del shell")
    p.add_argument("--fondo", help="Fondos separados por coma. Si falta, se adivinan.")
    p.add_argument("--umbral", type=float, default=AA, help=f"Por defecto {AA} (AA texto normal)")
    p.add_argument("--json", action="store_true")
    args = p.parse_args()

    rutas = [Path(a) for a in args.archivos if Path(a).is_file()]
    if not rutas:
        print("No encontré ninguno de esos archivos.", file=sys.stderr)
        return 2

    hallados = extrae(rutas)
    if not hallados:
        print("No hay colores hex en esos archivos.", file=sys.stderr)
        return 2

    fondos = [normaliza(f.strip()) for f in args.fondo.split(",")] if args.fondo else adivina_fondos(hallados)

    filas = []
    for color, datos in hallados.items():
        if color in fondos:
            continue
        ratios = {f: round(contraste(color, f), 2) for f in fondos}
        filas.append(
            {
                "color": color,
                "nombre": sorted(datos["nombres"])[0] if datos["nombres"] else "",
                "veces": datos["veces"],
                "ratios": ratios,
                "mejor": max(ratios.values()),
                "pasa_aa": max(ratios.values()) >= args.umbral,
                "pasa_aa_grande": max(ratios.values()) >= AA_GRANDE,
            }
        )
    filas.sort(key=lambda f: f["mejor"])

    if args.json:
        print(json.dumps({"fondos": fondos, "colores": filas}, indent=1, ensure_ascii=False))
        return 0

    print(f"\nFondos: {', '.join(fondos)}   ·   umbral {args.umbral}\n")
    ancho = max((len(f["nombre"] or f["color"]) for f in filas), default=10)
    for f in filas:
        etiqueta = (f["nombre"] or f["color"]).ljust(ancho)
        cifras = "  ".join(f"{v:5.2f} sobre {k}" for k, v in f["ratios"].items())
        if f["pasa_aa"]:
            marca = "ok   "
        elif f["pasa_aa_grande"]:
            marca = "SOLO GRANDE"
        else:
            marca = "FALLA"
        print(f"  {etiqueta}  {f['color']}  {cifras}   {marca}  ({f['veces']}x)")

    fallan = [f for f in filas if not f["pasa_aa"]]
    print(f"\n{len(fallan)} de {len(filas)} no llegan a {args.umbral}:1 contra ningún fondo.")
    if fallan:
        print("Siguiente paso: busca cada uno en el código y mira si es texto que")
        print("alguien tiene que leer. Si lo es, súbelo. Si es un punto, un icono,")
        print("un borde o un estado deshabilitado, déjalo y anótalo en DESIGN.md.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
