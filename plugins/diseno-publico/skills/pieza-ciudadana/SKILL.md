---
name: pieza-ciudadana
description: Crea una página web de una sola pieza (un archivo HTML que se abre con doble clic) para explicarle a la ciudadanía un trámite, un servicio, una política o un programa público, en lenguaje claro, accesible (WCAG 2.1 AA) y con animaciones suaves que se pueden apagar. Úsala cuando pidan "haz una página para explicar…", "una landing del trámite…", "una pieza para la ciudadanía", "un micrositio", "una infografía interactiva" o "presenta esta política de forma visual".
---

# Pieza ciudadana

> Versión light del método de diseño de Jordan Rojas para el curso *IA Generativa
> para la Gestión Pública* (Uniandes). Créditos completos en `CREDITOS.md`.

El resultado es **un solo archivo `.html`** que funciona sin internet, sin instalar
nada y en el celular. Se abre con doble clic y se puede enviar por correo o publicar.

Parte de `plantilla.html` (en esta misma carpeta). Ya cumple todas las reglas de
abajo: **cambia el contenido, no rompas el sistema**.

## 1. Pregunta antes de escribir (máximo tres preguntas)

Si la persona no lo dijo, pregunta solo esto:
1. ¿Qué trámite, servicio o política es y **qué tiene que hacer la persona** al final?
2. ¿Quién la va a leer? (adultos mayores, jóvenes, empresarios, población rural…)
3. ¿Hay plazos, requisitos o cifras oficiales? Pide la fuente.

Si la persona prefiere que avances, avanza y marca con `[VERIFICAR]` todo dato que
no venga de ella o de una norma que puedas citar.

## 2. Cuida los datos

- **Nunca uses datos personales reales** (cédulas, nombres de ciudadanos, teléfonos).
  Si la persona pega uno, no lo pongas en la página y avísale.
- Cita la norma de cada plazo o requisito (por ejemplo, "Ley 1755 de 2015, art. 14").
- Si la entidad es inventada para practicar, dilo en la página ("ejemplo ficticio").
  Si es real, no inventes canales, teléfonos ni horarios: deja `[VERIFICAR]`.

## 3. Escribe en lenguaje claro

- Titular que diga el beneficio, no el nombre del trámite.
  Bien: "Pide lo que necesitas a la Alcaldía. Tenemos que responderte."
  Mal: "Procedimiento de radicación de peticiones, quejas y reclamos".
- Frases de menos de 25 palabras. Segunda persona ("tú" o "usted", según la entidad).
- Pasos numerados, de tres a cinco. Un verbo al inicio de cada paso.
- Nada de siglas sin explicar.

## 4. Las reglas de diseño (ya están en la plantilla)

| Regla | Por qué |
|---|---|
| Contraste de 4,5:1 o más en todo el texto | WCAG 2.1 AA, exigido por la Resolución 1519 de 2020 de MinTIC |
| **Un solo color de acento**, solo para la acción principal y la frase clave | Si todo resalta, nada resalta |
| Dos velocidades: 160 ms (responde al clic) y 500 ms (entra en escena) | Orden que se siente aunque no se vea |
| Una sola curva: `cubic-bezier(.22, 1, .36, 1)` | Coherencia |
| `prefers-reduced-motion` apaga el movimiento | A algunas personas el movimiento las marea |
| Enlace "Saltar al contenido", foco visible, funciona con teclado | Accesibilidad básica |
| Sin librerías externas ni fuentes descargadas | Carga rápido en conexiones lentas |

Para cambiar el color de la entidad, cambia solo `--acento` y comprueba que tenga
4,5:1 o más sobre blanco (con `auditar-diseno` o con el verificador de WebAIM).

## 5. Bloques disponibles en la plantilla

Usa los que sirvan y borra los demás:

- **Portada** con titular, entrada y dos botones.
- **Cifras que cuentan solas** (plazos, cobertura, beneficiarios).
- **Pasos numerados** que aparecen al bajar.
- **Lista de chequeo** interactiva con barra de progreso (no envía nada).
- **Preguntas frecuentes** desplegables.
- **Aviso** en recuadro (para la fuente, una advertencia o el "ejemplo ficticio").

## 6. Entrega

1. Guarda el archivo con un nombre claro: `tramite-derecho-de-peticion.html`.
2. Si puedes ejecutar código, corre `auditar-diseno` sobre el archivo y corrige.
3. Dile a la persona, en tres líneas: qué creaste, cómo abrirlo (doble clic) y qué
   tiene marcado `[VERIFICAR]`.
4. Conserva en el pie de página el crédito del kit y del método.

## Ideas para practicar en el curso

- El trámite más consultado de tu entidad, explicado en 4 pasos.
- Una política pública en una página: el problema, la meta en cifras, qué cambia
  para la gente.
- La rendición de cuentas del año: tres cifras que cuentan y lo que viene.
- La convocatoria de un programa: requisitos como lista de chequeo.
