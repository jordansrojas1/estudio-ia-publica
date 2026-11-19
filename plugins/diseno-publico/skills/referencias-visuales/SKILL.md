---
name: referencias-visuales
description: Biblioteca de sitios bien diseñados, ya desarmados en sus decisiones (colores, letra, espacios, movimiento), para usarlos como vara de medir. Úsala cuando pidan diseñar o mejorar una página "al nivel de" o "con el estilo de" una referencia, cuando pregunten "¿por qué este sitio se ve tan bien?", o cuando quieran analizar y guardar una referencia nueva.
---

# Referencias visuales

> Versión light del método de Jordan Rojas para el curso *IA Generativa para la
> Gestión Pública* (Uniandes). Cada referencia pertenece a sus autores; aquí solo se
> describen, con fines educativos, decisiones de diseño observables. Ver `CREDITOS.md`.

Cada archivo en `references/` es un sitio desarmado: paleta, tipografía, radios,
movimiento y los dos o tres trucos que hacen que se vea bien.

**No son plantillas para copiar. Son métodos.** Al usar una referencia se toma el
sistema (escala, contraste, ritmo, movimiento), nunca la composición literal, los
textos, los logos ni las imágenes del original. Y siempre se nombra la fuente.

## Referencias disponibles

| Archivo | Sitio | Qué enseña |
|---|---|---|
| `references/heydamir.md` | heydamir.design (Damir) | Oscuro cálido en vez de negro, un solo acento, dos velocidades de movimiento |
| `references/admin-os.md` | lroy-stack/admin-os (código abierto, MIT) | Cómo documentar cada decisión de color con su criterio WCAG, y cómo cerrar una discusión de diseño midiendo |

## Cómo usar una referencia con alguien del sector público

1. Pregunta qué quiere lograr (confianza, claridad, cercanía, seriedad).
2. Elige la referencia cuyo "qué enseña" se acerque, y explícalo en una frase.
3. Traduce: qué decisión de la referencia sirve para una entidad pública, y cuál no.
   Una entidad necesita, antes que nada, que todo el mundo pueda leer y usar la
   página: el contraste AA y el movimiento que se puede apagar no se negocian.
4. Si vas a producir algo, pasa el resultado por `auditar-diseno`.

## Para analizar una referencia nueva

Buenas candidatas para el sector público: el sistema de diseño de GOV.UK, la guía
de diseño de gov.co de MinTIC, o el sitio de una entidad que la persona admire.

1. Si el sitio publica su sistema de diseño o su documentación, léela primero:
   cuando una referencia explica sus decisiones, se citan sus decisiones.
2. Si no, observa (o pide a la persona que comparta capturas y el enlace):
   color de fondo y de texto, fuentes, radios de las esquinas, duraciones de las
   transiciones, estructura de la página.
3. Escribe el archivo con la misma estructura que `heydamir.md`:
   **ficha y crédito** primero, tokens, layout, movimiento, los trucos, y una
   sección honesta de "qué no copiar".
