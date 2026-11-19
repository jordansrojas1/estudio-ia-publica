#!/usr/bin/env python3
"""Inventario de motion: cuántas velocidades y cuántas curvas hay de verdad.

Lee los archivos que le pases (CSS, TSX, config de Tailwind, lo que sea), saca
cada duración y cada curva de transición o animación, y las cuenta. Sin
dependencias.

    python motion.py src/
    python motion.py src/index.css --velocidades 2 --curvas 1
    python motion.py src/ --json              # para encadenar

Un sistema sano tiene dos o tres velocidades y una curva. Diez duraciones
distintas no es riqueza expresiva: es que nadie decidió. El script cuenta; qué
se unifica y qué se deja lo decides mirando el código.

También avisa de dos cosas que no son cuestión de gusto: `transition: all`
(anima propiedades que no pensabas animar, incluido el layout) y la ausencia de
un bloque `prefers-reduced-motion`.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

# En Windows la consola es cp1252 y se atraganta con las flechas de la tabla.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

EXTENSIONES = {".css", ".scss", ".ts", ".tsx", ".js", ".jsx", ".vue", ".svelte", ".html"}
IGNORA = {"node_modules", "dist", "build", ".git", ".next", "coverage"}

# Línea que habla de movimiento. Fuera de aquí, un "0.3s" es otra cosa.
CONTEXTO = re.compile(r"transition|animation|animate-|\bduration-|\bease-|motion", re.I)

DURACION_CSS = re.compile(r"(?<![\w.-])(\d*\.?\d+)(ms|s)(?![\w-])")
DURACION_TW = re.compile(r"(?<![\w-])duration-(?:\[([^\]]+)\]|(\d+)|([a-z][\w-]*))")
CUBIC = re.compile(r"cubic-bezier\(([^)]*)\)")
# `ease:` con dos puntos es la propiedad de Framer Motion, no una curva de CSS:
# en CSS la palabra nunca va seguida de dos puntos.
PALABRA = re.compile(r"(?:\bease-)?\b(ease-in-out|ease-out|ease-in|linear|ease)\b(?![-:])")
VAR_CSS = re.compile(r"var\(\s*(--[\w-]+)\s*\)")
# Variables que pone la librería en tiempo de ejecución (Radix, Tailwind). No son
# decisiones de diseño de nadie, así que no cuentan como tokens del sistema.
VAR_AJENA = re.compile(r"^--(radix|tw|shiki|chakra|mantine)-")
TODO = re.compile(r"transition(?:-property)?\s*:\s*[^;}]*\ball\b")
REDUCIDO = re.compile(r"prefers-reduced-motion")


def a_ms(valor: str, unidad: str) -> float:
    n = float(valor)
    return n * 1000 if unidad == "s" else n


def normaliza_curva(bruta: str) -> str:
    """cubic-bezier( .22 , 1,.36 ,1 ) y cubic-bezier(0.22,1,0.36,1) son la misma."""
    partes = []
    for p in bruta.split(","):
        p = p.strip()
        try:
            partes.append(f"{float(p):g}")
        except ValueError:
            partes.append(p)
    return "cubic-bezier(" + ", ".join(partes) + ")"


def recoge(rutas: list[Path]) -> dict:
    duraciones: dict[str, list] = defaultdict(list)
    curvas: dict[str, list] = defaultdict(list)
    tokens: dict[str, list] = defaultdict(list)
    transiciones_all: list[str] = []
    tiene_reducido = False

    for ruta in rutas:
        try:
            texto = ruta.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            print(f"  (no se pudo leer {ruta}: {e})", file=sys.stderr)
            continue
        if REDUCIDO.search(texto):
            tiene_reducido = True

        for n, linea in enumerate(texto.splitlines(), 1):
            donde = f"{ruta}:{n}"
            if TODO.search(linea):
                transiciones_all.append(donde)
            if not CONTEXTO.search(linea):
                continue

            for m in DURACION_CSS.finditer(linea):
                duraciones[f"{a_ms(m.group(1), m.group(2)):g}ms"].append(donde)

            for m in DURACION_TW.finditer(linea):
                crudo, numero, nombre = m.groups()
                if numero:
                    duraciones[f"{float(numero):g}ms"].append(donde)
                elif crudo:
                    d = DURACION_CSS.search(crudo)
                    clave = f"{a_ms(d.group(1), d.group(2)):g}ms" if d else crudo
                    duraciones[clave].append(donde)
                else:
                    # duration-fast, duration-mid: nombres del tema de Tailwind.
                    # Son el sistema, no una excepción, así que van aparte.
                    tokens[f"duration-{nombre}"].append(donde)

            for m in VAR_CSS.finditer(linea):
                if not VAR_AJENA.match(m.group(1)):
                    tokens[m.group(1)].append(donde)

            # Un token llamado --hub-ease lleva la palabra "ease" dentro. Si se
            # busca la curva sobre la línea entera, el token se denuncia a sí
            # mismo y la cuenta de curvas en crudo sube cada vez que el sistema
            # se usa bien. Se tapan los var(...) antes de buscar.
            limpia = VAR_CSS.sub(lambda m: " " * len(m.group(0)), linea)
            for m in CUBIC.finditer(limpia):
                curvas[normaliza_curva(m.group(1))].append(donde)
            for m in PALABRA.finditer(limpia):
                curvas[m.group(1)].append(donde)

    return {
        "duraciones": duraciones,
        "curvas": curvas,
        "tokens": tokens,
        "transiciones_all": transiciones_all,
        "tiene_reducido": tiene_reducido,
    }


def expande(entradas: list[str]) -> list[Path]:
    rutas: list[Path] = []
    for e in entradas:
        p = Path(e)
        if p.is_dir():
            rutas += [q for q in p.rglob("*") if q.is_file() and q.suffix in EXTENSIONES]
        elif p.is_file():
            rutas.append(p)
    # node_modules y dist se cuelan con un glob del shell descuidado.
    return [r for r in rutas if not any(x in r.parts for x in IGNORA)]


def tabla(titulo: str, grupo: dict[str, list], aceptadas: int) -> None:
    if not grupo:
        return
    orden = sorted(grupo.items(), key=lambda kv: -len(kv[1]))
    print(f"\n{titulo} — {len(orden)} distintas")
    ancho = max(len(k) for k, _ in orden)
    for i, (clave, sitios) in enumerate(orden):
        marca = "  " if i < aceptadas else "→ "
        print(f"  {marca}{clave.ljust(ancho)}  {len(sitios):3}x   {sitios[0]}")


def main() -> int:
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    p.add_argument("archivos", nargs="+", help="Archivos o directorios")
    p.add_argument("--velocidades", type=int, default=3, help="Duraciones que aceptas (por defecto 3)")
    p.add_argument("--curvas", type=int, default=1, help="Curvas que aceptas (por defecto 1)")
    p.add_argument("--json", action="store_true")
    args = p.parse_args()

    rutas = expande(args.archivos)
    if not rutas:
        print("No encontré archivos que mirar.", file=sys.stderr)
        return 2

    r = recoge(rutas)

    if args.json:
        print(
            json.dumps(
                {
                    "archivos": len(rutas),
                    "duraciones": {k: {"veces": len(v), "sitios": v[:8]} for k, v in r["duraciones"].items()},
                    "curvas": {k: {"veces": len(v), "sitios": v[:8]} for k, v in r["curvas"].items()},
                    "tokens": {k: len(v) for k, v in r["tokens"].items()},
                    "transiciones_all": r["transiciones_all"],
                    "tiene_reducido": r["tiene_reducido"],
                },
                indent=1,
                ensure_ascii=False,
            )
        )
        return 0

    print(f"\n{len(rutas)} archivos mirados.")
    tabla("Duraciones en crudo", r["duraciones"], args.velocidades)
    tabla("Curvas en crudo", r["curvas"], args.curvas)

    if r["tokens"]:
        print(f"\nPor token — {len(r['tokens'])} distintos (esto es el sistema, no la excepción)")
        for clave, sitios in sorted(r["tokens"].items(), key=lambda kv: -len(kv[1])):
            print(f"    {clave}  {len(sitios)}x")

    n_dur, n_cur = len(r["duraciones"]), len(r["curvas"])
    print("\n—")
    if n_dur > args.velocidades:
        print(f"  {n_dur} duraciones en crudo para {args.velocidades} velocidades de sistema.")
        print("  Las marcadas con → son las candidatas a desaparecer: busca cada una,")
        print("  decide a qué velocidad pertenece y cámbiala por el token.")
    else:
        print(f"  {n_dur} duraciones en crudo. Dentro de lo que pediste.")

    if n_cur > args.curvas:
        print(f"  {n_cur} curvas distintas. Una interfaz con una sola curva se siente de una")
        print("  pieza; con cinco se siente ensamblada. Deja solo las excepciones que")
        print("  tengan una razón escrita al lado.")

    if r["transiciones_all"]:
        print(f"\n  `transition: all` en {len(r['transiciones_all'])} sitios:")
        for d in r["transiciones_all"][:6]:
            print(f"    {d}")
        print("  Anima también lo que no querías, incluido el layout. Nombra las propiedades.")

    if not r["tiene_reducido"]:
        print("\n  No hay ningún bloque `prefers-reduced-motion`. Para quien marcó esa")
        print("  preferencia en su sistema, el movimiento no es decoración: marea.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
