---
name: auditar-diseno
description: Revisa una página web, un HTML o una hoja de estilos que ya existe y dice, con números, si el texto se lee bien (contraste WCAG 2.1 AA, el que exige la Resolución 1519 de 2020 de MinTIC a las entidades públicas en Colombia) y si las animaciones están ordenadas. Úsala cuando pidan "revisar accesibilidad", "auditar el diseño", "¿se lee bien esta página?", "¿cumple WCAG?", "mejorar el diseño" o "unificar la estética" sobre algo que ya está hecho. No es para diseñar desde cero (para eso está pieza-ciudadana).
---

# Auditar un diseño que ya existe

> Versión light del método de Jordan Rojas para el curso *IA Generativa para la
> Gestión Pública* (Uniandes). Créditos completos en `CREDITOS.md` del repositorio.

Rediseñar sin medir es cambiar de opinión, no de sistema. Esta habilidad convierte
"esto se ve desordenado" o "creo que no se lee" en una lista de números con los que
se puede conversar en la entidad.

## Quién la usa y cómo hablarle

Quien te pide esto casi siempre es un servidor público, no un programador. Por eso:

- Explica cada hallazgo en una frase sencilla antes del número.
  Bien: "El gris de las notas al pie se lee con dificultad: 3,1 a 1, y la norma pide 4,5 a 1".
- No le pidas que corra comandos. Córrelos tú.
- Termina siempre con **qué hacer** y **qué no hace falta tocar**.

## Las dos herramientas

Hay dos scripts en `scripts/`, en Python y sin nada que instalar:

```
python scripts/contraste.py <archivos o carpeta> --fondo "#FFFFFF"
python scripts/motion.py   <archivos o carpeta> --velocidades 2 --curvas 1
```

- `contraste.py` saca los colores y dice cuáles **no** llegan a 4,5:1 (texto normal)
  o 3:1 (texto grande: desde 24 px, o 18,66 px en negrita).
- `motion.py` cuenta cuántas duraciones y curvas de animación distintas hay, y avisa
  si falta el bloque `prefers-reduced-motion` (personas a las que el movimiento marea).

Los dos aceptan `--json`. Si la persona solo pegó un HTML o un enlace, guarda el
contenido en un archivo y córrelos sobre ese archivo.

Si no puedes ejecutar código, haz el cálculo de contraste a mano con la fórmula de
luminancia relativa de WCAG 2.1 y dilo así: "calculado a mano, conviene confirmarlo
con un verificador como el de WebAIM".

## El método, en cinco pasos

### 1. Medir antes de opinar
Corre los dos scripts antes de proponer un solo cambio. Lo típico en un sitio que
creció sin sistema: ocho duraciones, cinco curvas y dos o tres colores de texto que
no llegan a AA. Eso ya es el diagnóstico.

### 2. Un número es una pregunta, no un error
Antes de declarar un fallo, mira dónde se usa ese color o esa animación y responde:
**¿esto lo lee alguien?** Un punto decorativo de 6 px que "falla" 3:1 no falla nada:
WCAG mide texto. Un texto gris de ayuda en un formulario de trámite sí falla, y es grave.

### 3. Prioriza por impacto en la ciudadanía
Ordena los hallazgos así:
1. Texto que la gente necesita para hacer un trámite (requisitos, plazos, botones).
2. Texto de navegación y formularios.
3. Texto decorativo o secundario.

### 4. Pocas decisiones, no muchos valores
Un sistema sano tiene **dos velocidades** de animación ("lo que responde al clic",
unos 160 ms, y "lo que entra en escena", unos 500 ms) y **una sola curva**. Si no
sabes explicar en una frase por qué dos valores son distintos, son el mismo.

### 5. El movimiento siempre se puede apagar
Toda página con animación necesita este bloque. Restringe la transición en vez de
quitarla: los cambios de color no marean a nadie.

```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation: none !important;
    transition-property: color, background-color, border-color, opacity !important;
    transition-duration: 160ms !important;
  }
}
```

## Qué entregar

Un informe corto en lenguaje claro con:

1. **Resumen en tres líneas**: ¿se lee?, ¿se mueve bien?, ¿qué es lo urgente?
2. **Tabla de contraste**: color, dónde se usa, relación, ¿pasa AA?, qué hacer.
   Propón el color corregido más cercano que sí pase.
3. **Tabla de movimiento**: cuántas velocidades y curvas hay, cuáles quedarían.
4. **Lo que no hace falta tocar**, con su razón.
5. Si la persona lo pide, el CSS corregido listo para copiar.

Cierra recordando que esto es una revisión automática de dos criterios (contraste y
movimiento) y que la accesibilidad completa (lectores de pantalla, teclado,
subtítulos, lenguaje claro) pide una revisión más amplia con el Anexo 1 de la
Resolución 1519 de 2020.

## Relacionadas

- `referencias-visuales`: para comparar contra un sitio bien hecho.
- `pieza-ciudadana`: para crear una página nueva que nazca cumpliendo.
